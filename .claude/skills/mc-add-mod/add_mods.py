"""Add Modrinth mods to the packwiz pack without packwiz.

Usage: python -I add_mods.py <repo> <slug>[@<version_id>] ... [--side slug=client|both] [--jars <dir>] [--dry]
Picks the newest Forge 1.20.1 release (or the given version id), reads META-INF/mods.toml from the jar, stops if a
mandatory dependency is missing from the pack, then writes mods/<slug>.pw.toml, adds a sorted index entry and
updates the index hash in pack.toml. Never writes side = "server": singleplayer worlds need server mods too.
"""
import glob, hashlib, io, json, os, re, sys, tempfile, urllib.parse, urllib.request, zipfile

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
MC, LOADER = '1.20.1', 'forge'
JAR_DIRS = [r'C:\MinecraftServer\mods',
            os.path.expandvars(r'%APPDATA%\PrismLauncher\instances\BenAndSarah-1.20.1\minecraft\mods')]
BUILTIN = {'forge', 'minecraft', 'java'}


def get(url, raw=False):
    r = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'minecraft-pack-mc-add-mod'}))
    return r.read() if raw else json.load(r)


def jar_info(data):
    """Return (mod ids in the jar, mandatory dependency ids). Jars without mods.toml (mixin libraries) give empty sets."""
    nested = set()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        # Jar-in-jar libraries count as provided (Flywheel and Ponder in Create's META-INF/jarjar,
        # Expandability in Artifacts' META-INF/jars).
        for n in z.namelist():
            if n.startswith('META-INF/') and n.endswith('.jar'):
                try:
                    nested |= jar_info(z.read(n))[0]
                except Exception:
                    pass
        if 'META-INF/mods.toml' not in z.namelist():
            return nested, []
        t = z.read('META-INF/mods.toml').decode('utf-8', 'replace')
    # Own ids come only from [[mods]] sections; dependency sections also have modId lines.
    ids = set(nested)
    for sec in re.split(r'^\s*\[\[mods\]\]', t, flags=re.M)[1:]:
        sec = re.split(r'^\s*\[', sec, maxsplit=1, flags=re.M)[0]
        ids |= set(re.findall(r'^\s*modId\s*=\s*"([^"]+)"', sec, re.M))
    deps = []
    for blk in re.split(r'\[\[dependencies\.[^\]]+\]\]', t)[1:]:
        m = re.search(r'modId\s*=\s*"([^"]+)"', blk)
        man = re.search(r'mandatory\s*=\s*(true|false)', blk)
        typ = re.search(r'type\s*=\s*"(\w+)"', blk)
        if m and ((man and man.group(1) == 'true') or (typ and typ.group(1).lower() == 'required')):
            deps.append(m.group(1))
    return ids, deps


def main():
    args = sys.argv[1:]
    dry = '--dry' in args
    sides = {}
    while '--side' in args:
        i = args.index('--side'); k, v = args[i + 1].split('='); sides[k] = v; del args[i:i + 2]
    while '--jars' in args:  # extra jar folder, e.g. a test server already on a branch's mods
        i = args.index('--jars'); JAR_DIRS.append(args[i + 1]); del args[i:i + 2]
    args = [a for a in args if a != '--dry']
    repo, specs = args[0], args[1:]
    have = set()
    for d in JAR_DIRS:
        for j in glob.glob(os.path.join(d, '*.jar')):
            try:
                have |= jar_info(open(j, 'rb').read())[0]
            except Exception:
                pass
    if not have:
        print('WARNING: no installed jars found; dependency check only covers the new mods')
    new = []
    for spec in specs:
        slug, _, vid = spec.partition('@')
        p = get(f'https://api.modrinth.com/v2/project/{slug}')
        if vid:
            v = get(f'https://api.modrinth.com/v2/version/{vid}')
        else:
            q = urllib.parse.urlencode({'loaders': json.dumps([LOADER]), 'game_versions': json.dumps([MC])})
            vs = [v for v in get(f'https://api.modrinth.com/v2/project/{slug}/version?{q}')
                  if LOADER in v['loaders'] and MC in v['game_versions'] and v['version_type'] == 'release']
            if not vs:
                sys.exit(f'{slug}: no {LOADER} {MC} release on Modrinth')
            v = vs[0]
        f = next((f for f in v['files'] if f['primary']), v['files'][0])
        data = get(f['url'], raw=True)
        if hashlib.sha512(data).hexdigest() != f['hashes']['sha512']:
            sys.exit(f'{slug}: sha512 mismatch')
        ids, deps = jar_info(data)
        have |= ids
        side = sides.get(slug) or ('client' if p['server_side'] == 'unsupported' else 'both')
        if side not in ('client', 'both'):
            sys.exit(f'{slug}: side must be client or both')
        new.append(dict(slug=slug, title=p['title'], pid=p['id'], vid=v['id'], ver=v['version_number'], f=f,
                        side=side, deps=deps))
    missing = False
    for n in new:
        miss = [d for d in n['deps'] if d not in have and d not in BUILTIN]
        missing |= bool(miss)
        print(f"{n['slug']:<32} {n['ver'][:26]:<26} side={n['side']:<6} {'MISSING ' + str(miss) if miss else 'deps ok'}")
    if missing:
        sys.exit('Stopped: add the missing dependencies first (find their Modrinth slugs).')
    if dry:
        return
    ip = os.path.join(repo, 'index.toml')
    idx = open(ip, encoding='utf-8', newline='').read()
    head, _, rest = idx.partition('[[files]]')
    blocks = ['[[files]]' + b.rstrip('\n') + '\n' for b in ('[[files]]' + rest).split('[[files]]')[1:]] if rest else []
    for n in new:
        f = n['f']
        body = (f'name = "{n["title"]}"\nfilename = "{f["filename"]}"\nside = "{n["side"]}"\n\n[download]\n'
                f'url = "{f["url"]}"\nhash-format = "sha512"\nhash = "{f["hashes"]["sha512"]}"\n\n'
                f'[update]\n[update.modrinth]\nmod-id = "{n["pid"]}"\nversion = "{n["vid"]}"\n')
        fn = f'mods/{n["slug"]}.pw.toml'
        if any(f'file = "{fn}"' in b for b in blocks):
            sys.exit(f'{fn} is already in index.toml')
        open(os.path.join(repo, fn), 'w', encoding='utf-8', newline='').write(body)
        blocks.append(f'[[files]]\nfile = "{fn}"\nhash = "{hashlib.sha256(body.encode()).hexdigest()}"\nmetafile = true\n')
    blocks.sort(key=lambda b: re.search(r'file = "([^"]+)"', b).group(1))
    idx = head.rstrip('\n') + '\n\n' + '\n'.join(blocks)
    open(ip, 'w', encoding='utf-8', newline='').write(idx)
    pk = os.path.join(repo, 'pack.toml')
    t = open(pk, encoding='utf-8', newline='').read()
    t2 = re.sub(r'(\[index\][^\[]*?hash = ")[0-9a-f]+', lambda m: m.group(1) + hashlib.sha256(idx.encode()).hexdigest(),
                t, flags=re.S)
    if t2 == t:
        sys.exit('pack.toml index hash not updated: check its [index] block')
    open(pk, 'w', encoding='utf-8', newline='').write(t2)
    print(f'Wrote {len(new)} mod files; index has {len(blocks)} entries.')


if __name__ == '__main__':
    main()
