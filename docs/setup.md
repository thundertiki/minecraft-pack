# Setup: Prism clients and the PC server

The pack is `pack.toml` + `index.toml` + `mods/*.pw.toml`. Machines install it with packwiz-installer, which reads
`pack.toml` from a URL and downloads the jars from Modrinth.

## Pack URL
The repo is public (2026-11-03), so every machine uses
`https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml`. Only `main` reaches players: merge
before expecting an update. Bootstrap used: packwiz-installer-bootstrap v0.0.3.
GitHub caches `main` for a few minutes after a push. To test a commit at once, point packwiz at
`https://raw.githubusercontent.com/thundertiki/minecraft-pack/<commit sha>/pack.toml`.

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
   cd /d "%~dp0"
   set "PATH=C:\Program Files\Eclipse Adoptium\jdk-17.0.21.9-hotspot\bin;%PATH%"
   java -jar packwiz-installer-bootstrap.jar -g -s server https://raw.githubusercontent.com/thundertiki/minecraft-pack/main/pack.toml
   call "%~dp0run.bat" nogui
   ```
5. Run `start.bat` once; it stops at the EULA. Set `eula=true` in `eula.txt`, run it again. Allow Java on private
   networks when Windows asks.
6. Join from clients at the PC's LAN IP or its Tailscale name (port 25565). Ben's PC: LAN `10.10.1.135`, Tailscale
   `100.112.253.99` or `desktop`.
7. Pre-generate with Chunky once in the server console: `chunky radius 3000`, then `chunky start`.

## Server settings (only in `C:\MinecraftServer`, not in the pack)
- Ops: Ben is `Thunder_Tiki` (not `thundertiki`, a different account), Sarah is `s0ulta`. Op from the server
  window: `op <name>`.
- `server.properties`: `allow-flight=true` (jetpacks and dragons).
- `config/simplebackups-common.toml`: `timer = 30`, `backupsToKeep = 40`. Backups go to `simplebackups/`,
  which Google Drive for desktop copies off the PC (Ben, 2026-11-07). Drive mirrors deletions, so that copy only
  holds the newest 40; the full archive is `G:\My Drive\Minecraft\world-backups` (below).

## Services on the PC (move every one when switching computers)
Checklist for a new server computer; each line says where it lives and how to recreate it.
1. **Java:** Temurin 17 (`winget install EclipseAdoptium.Temurin.17.JDK`); Forge 1.20.1 needs 17, don't upgrade.
2. **Minecraft server:** `C:\MinecraftServer` (Forge 47.4.28, `start.bat`, `user_jvm_args.txt` `-Xmx4G`, ops,
   `server.properties`, `eula.txt`): steps under PC server. Move the `world` folder (or restore the newest backup).
3. **Firewall:** inbound rule "Minecraft Server 25565" (TCP, Private) and Windows' allow rule for Temurin's
   `java.exe` (Windows asks on first start).
4. **Tailscale:** the server and web map are reached at the PC's Tailscale IP `100.112.253.99`. A new PC gets a new
   IP: update `config/bluemap/webserver.conf` `ip:` and this file.
5. **BlueMap web map:** server mod plus `config/bluemap/` (section above).
6. **Backups:** Simple Backups (in the pack) writes `C:\MinecraftServer\simplebackups`; Google Drive for desktop
   backs that folder up; scheduled task **"Minecraft backup archive"** (hourly, current user) copies every zip to
   `G:\My Drive\Minecraft\world-backups` and never deletes. Recreate it with
   `tools/backup-archive/install-task.ps1`; log `C:\MinecraftServer\logs\archive-backups.log`.
7. **Timelapse renders (not scheduled):** `C:\MinecraftServer\timelapse\` (BlueMap 5.3 CLI, config, frames) and
   the venv `C:\Users\Benjamen\venvs\mc-timelapse` (Pillow). See `docs/timelapse.md`.
8. **Clients:** Prism instance `BenAndSarah-1.20.1` with the packwiz pre-launch command (Prism client section).
9. **Test copy:** `C:\MinecraftServer-test` (worldgen test of 2026-11-07, ports 25566/8101) can be deleted.

## Web map (BlueMap, server only)
- Open `http://100.112.253.99:8100` (or `http://desktop:8100`) on any Tailscale device while the server runs.
  JourneyMap's own web map only runs inside a game client, so it is not used.
- `config/bluemap/webserver.conf`: `ip: "100.112.253.99"`, so it listens only on Tailscale (not the LAN). No
  firewall rule needed: Windows already allows Temurin 17's `java.exe` inbound.
- `config/bluemap/core.conf`: `accept-download: true` (BlueMap downloads Minecraft's client jar under Mojang's EULA
  for textures), `render-thread-count: 2` (the PC also runs HA and Jellyfin).
- Commands in the server console: `bluemap` (status), `bluemap reload`, `bluemap freeze world` to pause rendering.
  Modded blocks without a standard model show plain or missing.

## Troubleshooting
- Red flashes in menus and black flashes in game: the Sunshine/Apollo virtual display. Close it while playing.
- White flashes in game and menus (even with shaders off): Dynamic FPS with Oculus. Removed 2026-11-07; see
  `dead-ends.md`.

## Shaders
Never in the pack. Download the zip (PC: Photon v1.4 from modrinth.com/shader/photon-shader; Modrinth lists
1.20.1 for it; installed on Ben's PC 2026-11-03) into the instance's
`minecraft/shaderpacks` folder, then in game: Options > Video Settings > Shader Packs.
