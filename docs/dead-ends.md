# Dead ends (failed approaches; add one block each)

- **GregTech New Horizons / GregTech packs:** GTNH is 1.7.10 and cannot run modern shaders or Sarah's mods. Monifactory
  and Star Technology were dropped because Ben does not want a linear pack.
- **Line A: 1.21.1 NeoForge + Cobblemon (not chosen, 2026-11-03):** Ben chose Create + Alex's Mobs instead, so one
  creature mod. Cobblemon on 1.20.1 Forge stops at 1.5.2 (no riding, no Mega Showdown), so keeping Cobblemon would have
  meant 1.21.1. On 1.21.1 there is no official Alex's Mobs on Modrinth (only unofficial ports `alexs-mobs-continued`
  2.2.4 and `alexs-mobs-1.21.1` 1.22.17), Botania has no build, and Dragon Mounts Legacy, Ore Excavation and Create
  Steam 'n Rails are missing. Verified versions for that line: Cobblemon 1.8.4, Create 6.0.10, Terralith 2.6.2,
  Sodium 0.8.13, Iris 1.8.14-beta.1. Revisit if Ben wants Cobblemon later.
- **Alex's Mobs and Cobblemon together:** too many creatures and an old crash report (Cobblemon 1.5 with Alex's Mobs);
  Ben chose one.
- **Quests and Above-and-Beyond-style tiers (dropped 2026-11-03):** Ben chose normal Create progression with no quests;
  TFMG's steel and oil chains give the depth instead of KubeJS-locked machine tiers.
- **`packwiz modrinth add tectonic` picks 2.2.1 (a 1.19.3 multi-loader file):** add it by version id and keep it
  pinned (`packwiz pin tectonic`); unpin only to update by hand.
- **Checking dependencies with the Modrinth API** (2026-11-03, confirmed): missed Architectury, Cloth Config and
  Lithostitched, because Artifacts and Tectonic declare them only in their jars. Read each jar's `META-INF/mods.toml`
  (skill `mc-add-mod` does). Revisit if: never.
- **Running downloaded tool jars** (packwiz CI build 2026-11-04, BlueMap CLI 2026-11-07; confirmed): auto mode blocks
  them as outside code. Mods are added by writing `.pw.toml` files (`mc-add-mod`). Ben allowed the BlueMap CLI on
  2026-11-07, so packwiz may work if he allows it too. Revisit if: Ben installs packwiz or allows it.
- **Dynamic FPS (dynamic-fps 3.11.4) with Oculus 1.8.0 + Embeddium 0.3.31:** white flashing in game and menus on the PC
  (RTX 2070 SUPER), even with shaders off. Removing Oculus or Dynamic FPS stopped it; removed Dynamic FPS on 2026-11-07
  (not the virtual displays: those were disabled and it continued).
- **BlueMap 5.12 (`5.12-mc1.20-6-forge`) on the server** (2026-11-07): built for Java 21 (class version 65); the
  server runs Java 17, so it failed to start. Pinned 5.3 (`5.3-forge-1.20`, Java 17). Revisit if the server moves
  to Java 21.
- **BlueMap CLI 5.29 for timelapse renders** (2026-11-07, confirmed): built for Java 25 (class version 69); this PC
  has 17 and 21. Using CLI 5.3 on Java 17. CLI 5.16 (last Java 21 build) would add flat-only maps and render masks.
  Revisit if: Java 25 is installed just for the CLI.
