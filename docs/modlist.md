# Modlist: Minecraft 1.20.1, Forge, Create + Alex's Mobs (proposed 2026-11-03)

Decision from Ben (2026-11-03): focus on **Create** (tech) and **Alex's Mobs** (creatures); one creature mod only, so
no Cobblemon. That settles the version at **1.20.1 Forge** (official Alex's Mobs and the widest Create add-on pool).
The 1.21.1 NeoForge + Cobblemon alternative is in `dead-ends.md` for reference.

"Found" is the newest Modrinth version tagged 1.20.1 + forge, checked with the Modrinth API on 2026-11-02/03. `none` =
no build. **Check** = not confirmed, verify before adding. Packwiz adds required libraries (Citadel, GeckoLib, Balm,
Flywheel and so on) automatically; they are not listed. Counts are mods before libraries.

## Tier 1: base pack (about 65 mods before libraries)

### Creatures and pets
| Slug | Found | Notes |
|---|---|---|
| `alexs-mobs` | 1.22.9 | Core creature mod. About 89 animals; capuchin monkey rides on the shoulder (shift-right-click; crouch to remove). Needs Citadel. If too many animals, trim spawns in its config. |
| `naturalist` | 2.0.9 | Gentle wildlife (bears, deer, butterflies). Not in the pack (Alex's Mobs already adds many creatures). |
| `waystones-teleport-pets` | 1.2 | Pets follow Waystones teleports. |
| `saints-dragons` | 0.9.88 | Added 2026-11-03. Tameable, rideable animated dragons; the only maintained 1.20.1 Forge dragon mod. Needs GeckoLib (already in). Dragons only, so not a second general creature mod. |
| `alexs-caves` | 2.0.2 | Six rare cave biomes with their own mobs and blocks, by the Alex's Mobs author (Citadel already in). Big (71 MB). Worldgen: underground, new chunks only. Added 2026-11-07 (plan from the Mod Map). |

### Create core and add-ons
| Slug | Found | Notes |
|---|---|---|
| `create` | 6.0.8 | The tech spine. Pinned: 6.0.8 is the newest 1.20.1 build, and Central Kitchen needs exactly it. |
| `createaddition` | 1.3.3 | Electricity and wiring bridge. |
| `create-steam-n-rails` | 1.7.3 | Trains and steam. |
| `create-connected` | 1.2.3 | Quality of life blocks (more gearbox, shaft and belt variants). |
| `create-deco` | 2.0.3 | Decoration blocks (bars, catwalks). |
| `create-framed` | 1.7.1 | Glass and framed blocks. |
| `create-central-kitchen` | 1.5.1 | Create automation for Farmer's Delight; ties the tech and cozy halves together. |
| `create-enchantment-industry` | 2.5.4b | Automated enchanting and XP. |
| `create-jetpack` | 4.4.6 | Jetpack and brass backpack. |
| `create-ore-excavation` | 1.6.6 | Drills for ore veins. Keep alongside `ore-excavation` (different job). |
| `create-confectionery` | 1.1.3 | Sweets and baking. Cozy. |
| `create-tfmg` | 1.0.2f | The Factory Must Grow: steel, oil, diesel engines. Moved from Tier 2 (Ben, 2026-11-03); the tech depth. |
| `bellsandwhistles` | 0.4.5 | Create visual add-ons. Optional. |
| `create-repair` | 1.3.0 | Unofficial Create 1.20.1 patch: backported bug and dupe fixes; restores Create's train map in JourneyMap 6 (JourneyMap asks for it). Added 2026-11-04. |
| `mixinbooster` | 0.1.3+1.20.1 | Lets Create Repair apply its Fabric-mixin fixes on Forge (recommended by Create Repair). Added 2026-11-04. |
| `copycats` | 3.0.10 | Copycats+: copycat blocks in every shape. Added 2026-11-04. |
| `create-garnished` | 2.1.7.c | Nuts and foods made with Create. Worldgen: nut trees in Plains, plants in the Nether, End and some overworld biomes (new chunks only). Added 2026-11-07 (plan from the Mod Map). |
| `create-power-loader` | 2.0.3 | Chunk loaders for trains and contraptions. Added 2026-11-07 (plan from the Mod Map). |
| `create-goggles` | 6.1.1 | Engineer's goggles built into helmets. Added 2026-11-07 (plan from the Mod Map). |
Not on Modrinth under the slugs tried: Create Crafts & Additions is `createaddition` (above); `create-hypertube`,
`create-interactive` returned no project. (Slice & Dice is `slice-and-dice`, not `create-slice-and-dice`.)

### Cozy base and food (Sarah's old list)
| Slug | Found | Notes |
|---|---|---|
| `farmers-delight` | 1.3.4 | Cooking/farming backbone. |
| `cooking-for-blockheads` | 16.0.15 | |
| `farming-for-blockheads` | 14.0.4 | Market, shipping bin, sprinklers. Kept (Ben, 2026-11-03). |
| `gravestone-mod` | 1.0.35 | |
| `sophisticated-backpacks` | 3.26.19 | |
| `small-ships` | 2.0.2 | |
| `artifacts` | 9.5.19 | Needs Curios. |
| `curios` | 5.14.1 | |
| `waystones` | 14.1.21 | |
| `lootr` | 0.7.35 | |
| `botania` | 456 | Sarah's pick, non-negotiable (2026-11-03). Nature magic. |
| `pams-harvestcraft-2-food-core` | 1.0.5 | Sarah's pick, non-negotiable (2026-11-03). Hundreds of foods (sandwiches and more). Modrinth. |
| `pams-harvestcraft-2-food-extended` | 1.0.1 | More Pam's foods. Modrinth. |
| `pams-harvestcraft-2-crops` | 1.0.3 | Pam's garden crops. CurseForge only (no 1.20.1 build on Modrinth). |
| `pams-harvestcraft-2-trees` | 1.0.2 | Pam's fruit and nut trees. CurseForge only. |
| `simple-backups` | 3.1.24 | Automatic world backups (Create contraptions and a beta dragon mod can corrupt a world). |
| `farmers-respite` | 2.1 | Tea and coffee for Farmer's Delight. Added 2026-11-07 (plan from the Mod Map). |
| `botany-pots` | 13.0.43 | Grow crops and trees in pots; needs `bookshelf-lib` 20.2.15. Added 2026-11-07 (plan from the Mod Map). |
| `supplementaries` | 3.1.44 | Decorative and handy blocks (jars, signposts, flags); needs `moonlight` 2.16.39. Some worldgen (wild flax, road signs; new chunks only). Added 2026-11-07 (plan from the Mod Map). |

### World and structures
| Slug | Found | Notes |
|---|---|---|
| `terralith` | 2.5.4 | Terrain/biome overhaul. |
| `tectonic` | 3.0.17 | Terrain shaping, Terralith-compatible. |
| `regions-unexplored` or `biomes-o-plenty` | 0.5.6 / 19.0.0.96 | Not in the pack; add one only if more biomes are wanted. |
| `yungs-api` | 4.0.6 | Library for the YUNG's mods. |
| `yungs-better-caves` | 2.0.7 | |
| `yungs-better-dungeons` | 4.0.4 | |
| `yungs-better-mineshafts` | 4.0.4 | |
| `yungs-better-strongholds` | 4.0.3 | |
| `yungs-better-ocean-monuments` | 3.0.4 | |
| `yungs-better-nether-fortresses` | 2.0.6 | Added 2026-11-04 with the next four. Side `both` like the other YUNG's (singleplayer worlds need them). |
| `yungs-better-end-island` | 2.0.6 | |
| `yungs-better-jungle-temples` | 2.0.5 | |
| `yungs-better-witch-huts` | 3.0.3 | |
| `yungs-better-desert-temples` | 3.0.3 | |
| `better-village` | 3.3.1 | Sarah's old pick. `ct-overhaul-village` 3.4.14 is the alternative. |
| `valhelsia-structures` | 1.1.2 | Sarah's old pick; extra structures. |
| `valhelsia-furniture` | 1.1.3 | Furnishes Valhelsia Structures (it warns without it) and adds craftable furniture. Needs Valhelsia Core 1.1.1+. Added 2026-11-04, before the world was made. |
| `natures-compass` | 1.12.0 | |

### Quality of life
| Slug | Found | Notes |
|---|---|---|
| `jei` | 15.74.0 | |
| `journeymap` | 6.0.7 | Chosen over Xaero's (Ben, 2026-11-03). |
| `appleskin` | 2.5.1 | |
| `jade` | 11.13.3 | |
| `mouse-tweaks` | 2.25.1 | |
| `clumps` | 12.0.0.4 | |
| `snow-under-trees` | 1.4.12 | |
| `polymorph` | 0.49.11 | Choose the result when two mods' recipes clash (food mods, Create). Added 2026-11-03. |
| `just-enough-resources-jer` | 1.4.0.247 | JEI pages for mob drops and ore heights. Added 2026-11-03. |
| `explorers-compass` | 1.4.0 | Finds structures. Added 2026-11-03. |
| `inventory-profiles-next` | 1.10.20 | Inventory sorting; pulls in Kotlin for Forge and libIPN. Added 2026-11-03. |
| `ore-excavation` | 1.13.170 | Sarah's old pick; vein mining. Keep alongside `create-ore-excavation`. |
| `controlling` | 12.0.2 | Search box in the controls menu. Client only; needs `searchables` 1.0.3. Added 2026-11-04. Searchables is side `both` since 2026-11-03: it registers a network channel, so a client-only copy blocks joining ("incompatible FML"). |
| `spark` | 1.10.53 | Side `server` since 2026-11-07. Lag profiler for the server (`/spark profiler`). Idle unless used. Added 2026-11-04. |
| `storagedrawers` | 12.15.1 | Drawer storage. Added 2026-11-07 (plan from the Mod Map). |
| `trashslot` | 15.1.5 | Trash slot in the inventory. Added 2026-11-07 (plan from the Mod Map). |
| `bluemap` | 5.3-forge-1.20 | 3D web map of the server world, over Tailscale (port 8100). Side `server`: it runs only on the PC server, clients never get it. Pinned: 5.12 needs Java 21 (server runs 17). Added 2026-11-07 (JourneyMap's web map only runs inside a client). Setup: `docs/setup.md`. |

### Performance and shaders
| Slug | Found | Notes |
|---|---|---|
| `embeddium` | 0.3.31 | Renderer (or `rubidium` 0.7.1). |
| `oculus` | 1.8.0 | Shader loader; Eclipse needs 1.6.11 or newer. |
| `ferrite-core` | 6.0.1 | Memory. |
| `modernfix` | 5.27.91 | Startup and memory. |
| `entityculling` | 1.11.3 | Helps with Create contraptions and many animals. |
| `memoryleakfix` | 1.1.5 | Fixes memory leaks. Add-on to watch after the Dynamic FPS flash. Added 2026-11-07 (plan from the Mod Map). |
| `chunky` | 1.3.146 | Side `server` since 2026-11-07. Pre-generate the world on the PC server (Terralith + Tectonic chunks are slow to generate). Optional. |

Libraries packwiz added (not listed above): Balm, Citadel, Common Networking, Create Dragons Plus (required by Create
Enchantment Industry), GeckoLib, Kotlin for Forge, libIPN, Library Ferret, Mezz Config, Patchouli, SmartBrainLib,
Sophisticated Core, Valhelsia Core, YUNG's API.

Libraries added by hand on 2026-11-03 (packwiz missed them: the mods declare them only in their jars, not on Modrinth;
the PC server's Forge log listed them): Architectury API 9.2.14 and Cloth Config 11.1.136 (Artifacts), Lithostitched
1.4.11 (Tectonic). Side set to `both` (Modrinth marks Lithostitched server-only, but Tectonic needs it on clients).
After adding a mod, start the server once and check the log for `Missing or unsupported mandatory dependencies`.

## Tier 2: optional depth (heavier)
All four moved into the pack on 2026-11-07 (AE2 with `guideme` 20.1.15). AE2 worldgen: meteorites and quartz, new
chunks only.
| Slug | Found | Notes |
|---|---|---|
| `create-tweaked-controllers` | 1.2.7 | Gamepad control for contraptions. Not in the pack (moved from Tier 1, 2026-11-07). |
| `create-encased` | 1.8-ht2 | More encased machinery. |
| `create-bits-n-bobs` | 0.0.41 | Extra building/utility blocks. |
| `ae2` | 15.4.12 | Applied Energistics 2 storage/autocrafting. |

## Dropped
GregTech-based packs (linear), Cobblemon and Pixelmon (one creature mod only), `create-oxidized` (tiny), FTB Quests and any quest mod (Ben, 2026-11-03: no quests).

Dropped in the 2026-11-03 review: `immediatelyfast` (only 1.21.x builds, wrongly tagged), `create-design-n-decor` (last
1.20.1 build 0.4.0b from 2024, before Create 6), `create-ultimine` (overlaps Ore Excavation), `mekanism` (heavy, a second tech chain),
Goblin Traders and Curious Elytra (no Modrinth project), ExpandAbility (no 1.20.1 build), Valhelsia Tweaks, Useful
Backpacks (Sophisticated Backpacks instead), Essential (not needed with Prism),
Adorable Hamster Pets, Animal Garden Owl and Pet Shop (Ben, 2026-11-03: not needed).

Cut in the 2026-11-03 audit: `create-new-age` (third electricity system next to Crafts & Additions and TFMG),
`canary` (unmaintained since 2024, crash risk), `dragon-mounts-legacy` (unmaintained 2024 beta),
`swing-through-grass` (little value), `create-diesel-generators` (TFMG engines cover it). Library Ferret, Caelus API,
EnchantmentDescriptions, Bookshelf, U Team Core and Cloth Config are libraries: packwiz adds them only if a mod needs
them.

Removed 2026-11-07: `slice-and-dice` (Central Kitchen already turns cutting board recipes into Create sawing and
deploying; any placed Slicers are lost). Kotlin for Forge stays: Create Jetpack and Inventory Profiles Next use it.
Not added 2026-11-07: `noisium` (rewrites part of the chunk generator; small gain, risk to the current world).
