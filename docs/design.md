# Design (proposed 2026-11-02, for Opus review)

## Goals
- A pack for Ben and Sarah (maybe others later) that mixes tech progression (Ben liked GregTech New Horizons) with a
  cozy base (Sarah's earlier pack: farming, food, Botania, exploration, pets).
- Non-linear. Quests are optional: a tech questline for Ben, a small cozy/Cobblemon questline Sarah can ignore.
- Runs on the work laptop (8 GB total RAM) and the PC. Shaders (Eclipse) optional.

## Decisions
- **One creature mod, not both (Ben, 2026-11-03):** Cobblemon or Alex's Mobs. That decides the version, so two lines
  are proposed in `modlist.md`; **Opus picks one**:
  - **Line A: 1.21.1 NeoForge + Cobblemon.** Current Cobblemon (1.8.4, with riding) only exists here. No official
    Alex's Mobs on this version. Shoulder pets come from Perch, Adorable Hamster Pets and the Animal Garden mods.
    Gains the 1.21 vanilla additions (trial chambers, mace, Crafter).
  - **Line B: 1.20.1 Forge + Alex's Mobs.** Official Alex's Mobs (monkey on the shoulder) and Naturalist. Keeps most of
    Sarah's old list (Botania, Dragon Mounts Legacy, Ore Excavation, Steam 'n Rails). Cobblemon here is stuck at 1.5.2
    (no riding, no Mega Showdown), so it is not in this line.
  - My lean: Line A if Cobblemon is the hook, Line B if Sarah's old mods and the monkey matter more.
- **Cobblemon, not Pixelmon (Line A).** Cobblemon is free and open source, runs on Fabric or NeoForge, and is lighter.
  Pixelmon is closed source, NeoForge only, heavier, and brings its own gym/league structure that we do not want.
- **Create as the tech base, not GregTech.** Lighter on RAM, visual, non-linear. AE2 and Mekanism are optional tier 2.
- **Custom pack instead of ATM10 / Enigmatica 10 / StoneBlock 4.** ATM10 lists 8 GB RAM minimum; none fits the
  laptop and none has the Cobblemon + cozy mix.
- **packwiz + Prism.** One Git repo is the source of truth; each Prism instance runs the packwiz installer bootstrap as
  a pre-launch command and updates on every start.
- Target about 100 mods including libraries. (An earlier chat estimate of 150 to 200 was too high for 8 GB.)

## Laptop vs PC
| | Laptop (8 GB total) | PC |
|---|---|---|
| Game RAM | 4 to 5 GB | 8 GB or more |
| Render distance | 8 to 10 | 12 to 16 |
| Shaders | off, or Eclipse on its lowest profile | Eclipse on |
| Optional heavy mods | off | Tier 2 on |
Same pack for both; only Prism instance settings differ. If a mod is too heavy for the laptop, drop it from the pack.

## Creatures
- **Why not both:** Cobblemon has its own species and spawns, and Alex's Mobs adds about 89 animals; together they
  crowd biomes and dilute Cobblemon spawns. An old 2024 report also shows Alex's Mobs in a crash log with Cobblemon 1.5
  (not confirmed for current versions). Ben chose one.
- **Line A (Cobblemon):** shoulder pets for Sarah come from `perch` (parrots), `adorable-hamster-pets`,
  `animal-garden-owl` and `animal-garden-olive-baboon` (a monkey-like animal; **Check** whether it sits on the shoulder).
  Cobblemon creatures themselves do not sit on your shoulder as far as the research found. Cobblemon 1.7+ has built-in
  riding (inferred from the Modrinth page of the old side mod "Cobblemon: Ride On!", which says it does not work on
  Cobblemon 1.7 or later). Check in play whether riding covers what Sarah wants.
- **Line B (Alex's Mobs):** the capuchin monkey sits on the owner's shoulder after a shift-right-click and is removed by
  crouching (wiki, [Capuchin Monkey](https://alexs-mobs-unofficial.fandom.com/wiki/Capuchin_Monkey)). Tame it with
  bananas. If the 89 animals feel too many, trim spawns in the Alex's Mobs config.

## Quests
- FTB Quests is not on Modrinth (the FTB mods are on CurseForge). Options: add it with `packwiz curseforge add`, or use
  Cobblemon Quests (Modrinth, `cobblemon-quests`) for the Cobblemon side and a different quest mod for tech. Opus to decide.
- Planned shape: one tech questline (Create first, then optional AE2/Mekanism), one cozy questline (farming, cooking,
  Cobblemon), both optional and not gating each other.

## World
- Terralith + Tectonic as the baseline, with Regions Unexplored or Biomes O' Plenty added only if the biome mix
  is not enough (stacking works with TerraBlender generation weights, but biomes get rarer).
- YUNG's structure mods, Lootr, and Overhauled Villages (replaces Better Village, which was not found).

## Open questions
1. **Which line, A or B?** (Cobblemon on 1.21.1 vs Alex's Mobs on 1.20.1.)
2. Quest mod: FTB Quests from CurseForge, or an all-Modrinth route? (Line B has none chosen on Modrinth.)
3. Botania is only on Modrinth for 1.20.1 (Line B). For Line A, is it on CurseForge, and does it fit the RAM budget?
4. Tier 2 (AE2, Mekanism): include from the start or wait until the base pack runs well on the laptop?
5. Pam's HarvestCraft 2 on 1.21.1 has small download counts (about 70K to 280K). Is it maintained and balanced against
   Farmer's Delight, or do we skip it?
