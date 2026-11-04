---
name: mc-add-mod
description: Add Modrinth mods to the minecraft-pack packwiz pack on a computer without packwiz - checks each jar's own dependencies, writes the .pw.toml, sorts the index, updates pack.toml, then tests on the PC server. Use when Ben asks to add, install or swap a mod in the pack.
---

# Add mods to the pack (no packwiz)

1. **Check first.** The mod must have a Forge 1.20.1 release (`CLAUDE.md` rules) and not be on the Dropped list in
   `docs/modlist.md`. `git -C <repo> pull`.
2. **Dry run:** `python -I .claude/skills/mc-add-mod/add_mods.py <repo> <slug> [<slug>@<version_id>] --dry`.
   It reads each jar's `META-INF/mods.toml` (Modrinth's dependency list misses some) and compares against jars in
   `C:\MinecraftServer\mods` and the Prism instance. `MISSING` = add that dependency too (find its slug), rerun.
3. **Side:** default `both`; `client` when Modrinth says the server doesn't support it. Override with
   `--side <slug>=client|both`. Never `server`: singleplayer worlds need world-gen mods too. A library a `both` mod
   needs is `both`, whatever Modrinth says (Lithostitched). A "client-only" mod can still register a network
   channel (Searchables): if joining fails with "incompatible FML", find `missing on server` in the client's
   `logs/latest.log` and make that mod `both`. The script skips mods already in the index, so change `side` by hand
   and update the sha256 hashes in `index.toml` and `pack.toml`.
4. **Write:** the same command without `--dry`. Check `git diff --stat`: index.toml only gains lines.
5. **Docs:** one row per mod in `docs/modlist.md` (slug, version, why, date), same commit. Commit, push to `main`.
6. **Server test** against the exact commit (GitHub caches `main` for a few minutes): a temp copy of `start.bat`
   in the scratchpad with the URL `.../minecraft-pack/<sha>/pack.toml` and `run.bat`'s java line in place of
   `call run.bat`. Start it with stdin redirected, wait for `Done (`, then write `stop` to stdin so the world saves.
   Fail on `Missing or unsupported mandatory dependencies` or a crash report. Never force-kill a running world.
7. Report the commit, the mods and their versions, and that the client picks them up on its next launch.
