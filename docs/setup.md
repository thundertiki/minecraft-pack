# Setup: Prism clients and the PC server

The pack is `pack.toml` + `index.toml` + `mods/*.pw.toml`. Machines install it with packwiz-installer, which reads
`pack.toml` from a URL and downloads the jars from Modrinth.

## Pack URL
The repo is public (2026-11-03), so every machine uses
`https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml`. Only `main` reaches players: merge
before expecting an update. Bootstrap used: packwiz-installer-bootstrap v0.0.3.

## Prism client (laptop, Ben's PC, Sarah's PC)
1. Create an instance: Minecraft 1.20.1, Forge 47.4.28. Memory: 4 to 5 GB on the laptop, 8 GB on a PC with 24 GB
   or more. Ben's PC (DESKTOP-T95IN58, 16 GB, RTX 2070 Super) also runs the server, HA VM and Jellyfin, so its
   instance `BenAndSarah-1.20.1` (set up 2026-11-03) uses 5 GB max, 2 GB min.
   Java: point the instance at a Java 17 (Java path in instance settings). Ben's PC uses Temurin 17
   (`winget install EclipseAdoptium.Temurin.17.JDK`), which does not go first on PATH (Java 21 stays the default).
2. Put `packwiz-installer-bootstrap.jar` (GitHub releases of `packwiz/packwiz-installer-bootstrap`) in the instance's
   `minecraft` folder. The laptop instance `BenAndSarah-1.20.1` was set up this way on 2026-11-03 (4.5 GB max).
3. Edit instance > Settings > Custom commands > Pre-launch command:
   `"$INST_JAVA" -jar packwiz-installer-bootstrap.jar https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml`
   Type it in Prism's settings field. If editing `instance.cfg` by hand, escape the inner quotes
   (`PreLaunchCommand="\"$INST_JAVA\" -jar ..."`) or Prism drops them and the Java path with spaces breaks.
4. Launch. It installs or updates the mods every start.

## PC server
1. Java 17 on the PC (`java -version`). Make a folder, for example `C:\MinecraftServer`.
2. Download `https://maven.minecraftforge.net/net/minecraftforge/forge/1.20.1-47.4.28/forge-1.20.1-47.4.28-installer.jar`
   into it and run `java -jar forge-1.20.1-47.4.28-installer.jar --installServer`.
3. Put `packwiz-installer-bootstrap.jar` in the folder. In `user_jvm_args.txt` add `-Xmx8G` on its own line (the
   file has no trailing newline). Ben's PC (16 GB) uses `-Xmx4G`.
4. Create `start.bat`. If Java 17 is not first on PATH (Ben's PC), add the `set "PATH=..."` line so `run.bat` gets it:
   ```
   @echo off
   set "PATH=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin;%PATH%"
   java -jar packwiz-installer-bootstrap.jar -g -s server https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml
   call run.bat nogui
   ```
5. Run `start.bat` once; it stops at the EULA. Set `eula=true` in `eula.txt`, run it again. Allow Java on private
   networks when Windows asks.
6. Join from clients at the PC's LAN IP or its Tailscale name (port 25565).
7. Pre-generate with Chunky once in the server console: `chunky radius 3000`, then `chunky start`.

## Shaders
Never in the pack. Download the zip (PC: Photon v1.4 from modrinth.com/shader/photon-shader; Modrinth lists
1.20.1 for it; installed on Ben's PC 2026-11-03) into the instance's
`minecraft/shaderpacks` folder, then in game: Options > Video Settings > Shader Packs.
