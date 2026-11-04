# Design (updated 2026-11-03, for Opus review)

## Goals
- A pack for Ben and Sarah (maybe others later) that mixes tech progression (Ben liked GregTech New Horizons) with a
  cozy base (Sarah's earlier pack: farming, food, Botania, exploration, pets).
- Non-linear, normal Create progression: no quests and no recipe locks (Ben, 2026-11-03).
- Runs on the work laptop (8 GB total RAM) and the PC. Shaders (Eclipse) optional.

## Decisions
- **Focus: Create + Alex's Mobs (Ben, 2026-11-03).** One creature mod only, so no Cobblemon. This fixes the version.
- **Minecraft 1.20.1, Forge.** Official Alex's Mobs (1.22.9) and the largest Create add-on pool live here, and most of
  Sarah's old list still exists. Shaders: Embeddium + Oculus 1.8.0 (Eclipse needs Iris or Oculus 1.6.11 or newer).
  Trade-off: no 1.21 vanilla content (trial chambers, mace, Crafter); unofficial backports exist.
- **Create as the tech base, not GregTech.** Lighter on RAM, visual, non-linear. For GTNH-style depth, `create-tfmg` (The
  Factory Must Grow: steel, oil, engines) is in Tier 1 (Ben, 2026-11-03); AE2 stays optional Tier 2;
  Mekanism dropped.
- **Custom pack instead of ATM10 / Enigmatica 10 / StoneBlock 4.** ATM10 lists 8 GB RAM minimum; none fits the
  laptop or this Create + cozy mix. Create-first packs to study for pacing: Create: Above and Beyond, Create: Astral.
- **packwiz + Prism.** One Git repo is the source of truth; each Prism instance runs the packwiz installer bootstrap as
  a pre-launch command and updates on every start.
- Target about 100 mods including libraries. Create add-ons are the biggest RAM risk: keep Tier 1 to about 16 Create mods.

## Laptop vs PC
The server runs on the PC (Ben, 2026-11-03). The laptop is only a client, used by Ben or Sarah; Sarah will later play
on her own PC.

| | Laptop (8 GB total) | PC |
|---|---|---|
| Game RAM | 4 to 5 GB | 5 GB (PC has 16 GB and also hosts the server, HA VM, Jellyfin) |
| Render distance | 8 to 10 | 12 to 16 |
| Shaders | off; if wanted, MakeUp Ultra Fast | Complementary Reimagined (or Eclipse) |
| Optional heavy mods | off | Tier 2 on |
Same pack for both; only Prism instance settings differ. If a mod is too heavy for the laptop, drop it from the pack.
Laptop hardware: Ryzen 5 7535U with integrated Radeon graphics, which reserves 2 GB of the 8 GB as video memory.

## Shaders (2026-11-03; zips installed per machine, never in the pack)
- PC: Complementary Reimagined r5.9.3 (vanilla look, good mod support); Complementary Unbound or BSL for a
  stronger look; Eclipse if Ben still wants it.
- Laptop: off by default. If wanted, MakeUp Ultra Fast 9.6 on a low preset; Complementary Reimagined on its Potato
  profile is the fallback.
- Test moving Create contraptions with the shader on before settling on one.
Large Create contraptions are the main performance cost; Flywheel (a Create dependency) helps, and so do Entity Culling and
Embeddium.

## Creatures: Alex's Mobs
- Alex's Mobs adds about 89 animals. The capuchin monkey sits on the owner's shoulder after a shift-right-click and is
  removed by crouching (wiki, [Capuchin Monkey](https://alexs-mobs-unofficial.fandom.com/wiki/Capuchin_Monkey)). Tame
  with bananas.
- No extra pet mods (Ben, 2026-11-03); the capuchin monkey is the shoulder pet.
- Danger is fine (Ben, 2026-11-03): keep Alex's Mobs hostiles at default. If the animals feel too many, trim spawns
  in the Alex's Mobs config. Naturalist is optional.

## Progression
- Normal Create recipes, no quests, no KubeJS recipe locks. TFMG gates itself by materials: steel needs a coke
  oven and blast furnace, and its oil and engine machines need steel.

## World
- Terralith + Tectonic as the baseline, with Regions Unexplored or Biomes O' Plenty added only if the biome mix
  is not enough (stacking works with TerraBlender generation weights, but biomes get rarer).
- YUNG's structure mods, Lootr, and Better Village (Sarah's pick) or the CT Overhauled Village alternative.

## Settled in the 2026-11-03 review
- Keep both ore mods: Create Ore Excavation (vein drills) and Ore Excavation (vein mining) do different jobs.
- Botania and Pam's HarvestCraft 2 are Sarah's non-negotiables (2026-11-03). Pam's crops and trees come from
  CurseForge; food core and extended from Modrinth. Pam's sits alongside Farmer's Delight and Central Kitchen.
- Sarah's unchecked mods: see Dropped in `modlist.md`.
- Sarah has not seen the list yet; she knows it is tech plus cozy.
