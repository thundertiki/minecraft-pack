# Setup: Prism clients and the PC server

The pack is `pack.toml` + `index.toml` + `mods/*.pw.toml`. Machines install it with packwiz-installer, which reads
`pack.toml` from a URL and downloads the jars from Modrinth.

## Pack URL
The repo is public (2026-11-03), so every machine uses
`https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml`. Only `main` reaches players: merge
before expecting an update. Bootstrap used: packwiz-installer-bootstrap v0.0.3.

## Prism client (laptop, Ben's PC, Sarah's PC)
1. Create an instance: Minecraft 1.20.1, Forge 47.4.28. Memory: 4 to 5 GB on the laptop, 8 GB on a PC.
2. Put `packwiz-installer-bootstrap.jar` (GitHub releases of `packwiz/packwiz-installer-bootstrap`) in the instance's
   `minecraft` folder. The laptop instance `BenAndSarah-1.20.1` was set up this way on 2026-11-03 (4.5 GB max).
3. Edit instance > Settings > Custom commands > Pre-launch command:
   `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml`
4. Launch. It installs or updates the mods every start.

## PC server
1. Install the Forge 1.20.1 47.4.28 server in its own folder; give it 6 to 8 GB.
2. Put `packwiz-installer-bootstrap.jar` there and run before each start:
   `java -jar packwiz-installer-bootstrap.jar -g -s server https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml` (skips client-only mods such as Embeddium).
3. Pre-generate with Chunky once: `chunky radius 3000`, then `chunky start`.

## Shaders
Eclipse is not in the pack. On machines that want it, put the zip in the instance's `shaderpacks` folder.
