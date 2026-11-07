"""Render one world backup with the BlueMap CLI and save a dated top-down frame for a timelapse.

Usage (Pillow lives in the venv):
  C:\\Users\\Benjamen\\venvs\\mc-timelapse\\Scripts\\python.exe -I tools/timelapse/render_backup.py [backup.zip] [--radius 1500]
Without a zip it renders the newest Simple Backups zip. See docs/timelapse.md.
"""
import argparse, glob, os, re, shutil, subprocess, sys, zipfile
from PIL import Image

SERVER = r'C:\MinecraftServer'
TL = os.path.join(SERVER, 'timelapse')
JAVA = r'C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin\java.exe'
CLI = os.path.join(TL, 'bluemap-5.3-cli.jar')
CONFIG = os.path.join(TL, 'config')
WORK = os.path.join(TL, 'work')
MAPDIR = os.path.join(TL, 'web', 'maps', 'world')
FRAMES = os.path.join(TL, 'frames')


def newest_backup():
    zips = sorted(glob.glob(os.path.join(SERVER, 'simplebackups', '*.zip')), key=os.path.getmtime)
    if not zips:
        sys.exit('no backups in simplebackups')
    return zips[-1]


def link_mod_packs():
    """BlueMap reads block models and textures for modded blocks from jars in config/packs."""
    packs = os.path.join(CONFIG, 'packs')
    shutil.rmtree(packs, ignore_errors=True)
    os.makedirs(packs)
    for j in glob.glob(os.path.join(SERVER, 'mods', '*.jar')):
        os.link(j, os.path.join(packs, os.path.basename(j)))


def lowres_tiles():
    """Lod-1 lowres tiles: one PNG per 500x500 blocks; the top half is colour, the bottom half height data."""
    tiles = {}
    for p in glob.glob(os.path.join(MAPDIR, 'tiles', '1', '**', '*.png'), recursive=True):
        rel = os.path.relpath(p, os.path.join(MAPDIR, 'tiles', '1'))
        m = re.match(r'x(-?[\d\\/]+)[\\/]z(-?[\d\\/]+)\.png$', rel)
        if not m:
            continue
        tx, tz = (int(re.sub(r'[\\/]', '', g)) for g in m.groups())
        tiles[(tx, tz)] = p
    return tiles


def stitch(tiles, radius, out):
    size = None
    canvas = None
    for (tx, tz), p in tiles.items():
        im = Image.open(p).convert('RGBA')
        w = im.width
        colour = im.crop((0, 0, w, im.height // 2))
        if canvas is None:
            size = w - 1 if w % 2 else w  # tiles overlap by one pixel at the edge
            canvas = Image.new('RGBA', (2 * radius, 2 * radius), (0, 0, 0, 255))
        x0, z0 = tx * size + radius, tz * size + radius
        canvas.paste(colour, (x0, z0), colour)  # paste clips tiles outside the frame
    canvas.convert('RGB').save(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('zip', nargs='?')
    ap.add_argument('--radius', type=int, default=1500, help='blocks around 0,0 kept in every frame')
    a = ap.parse_args()
    z = a.zip or newest_backup()
    stamp = re.search(r'(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})', os.path.basename(z))
    name = (stamp.group(1) if stamp else os.path.splitext(os.path.basename(z))[0]) + '.png'
    os.makedirs(FRAMES, exist_ok=True)
    if os.path.exists(os.path.join(FRAMES, name)):
        print('already rendered:', name)  # safe to run daily
        return

    shutil.rmtree(WORK, ignore_errors=True)
    with zipfile.ZipFile(z) as f:
        f.extractall(WORK)  # backups hold a top-level world/ folder
    shutil.rmtree(MAPDIR, ignore_errors=True)  # every frame is a full, fresh render
    link_mod_packs()
    r = subprocess.run([JAVA, '-jar', CLI, '-c', CONFIG, '-v', '1.20.1', '-r', '-f', '-m', 'world'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        sys.exit('BlueMap CLI failed:\n' + (r.stdout + r.stderr)[-3000:])
    tiles = lowres_tiles()
    if not tiles:
        sys.exit('BlueMap produced no lowres tiles:\n' + (r.stdout + r.stderr)[-3000:])
    out = os.path.join(FRAMES, name)
    stitch(tiles, a.radius, out)
    shutil.rmtree(WORK, ignore_errors=True)
    print(out)


if __name__ == '__main__':
    main()
