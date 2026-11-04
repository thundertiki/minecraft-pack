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
| `naturalist` | 2.0.9 | Gentle wildlife (bears, deer, butterflies). Optional, off by default: Alex's Mobs already adds many creatures. |
| `dragon-mounts-legacy` | 1.2.3-beta | Sarah's old mod; beta. |
| `waystones-teleport-pets` | 1.2 | Pets follow Waystones teleports. |

### Create core and add-ons
| Slug | Found | Notes |
|---|---|---|
| `create` | 6.0.8 | The tech spine: visual, non-linear automation. |
| `createaddition` | 1.3.3 | Electricity and wiring bridge. |
| `create-steam-n-rails` | 1.7.3 | Trains and steam. |
| `create-new-age` | 1.2.0 | Power generation. |
| `create-connected` | 1.2.3 | Quality of life blocks (more gearbox, shaft and belt variants). |
| `create-deco` | 2.0.3 | Decoration blocks (bars, catwalks). |
| `create-framed` | 1.7.1 | Glass and framed blocks. |
| `create-central-kitchen` | 1.5.1 | Create automation for Farmer's Delight; ties the tech and cozy halves together. |
| `create-enchantment-industry` | 2.5.4b | Automated enchanting and XP. |
| `create-jetpack` | 4.4.6 | Jetpack and brass backpack. |
| `create-ore-excavation` | 1.6.6 | Drills for ore veins. Keep alongside `ore-excavation` (different job). |
| `create-confectionery` | 1.1.3 | Sweets and baking. Cozy. |
| `create-tfmg` | 1.0.2f | The Factory Must Grow: steel, oil, diesel engines. Moved from Tier 2 (Ben, 2026-11-03); the tech depth. |
| `create-tweaked-controllers` | 1.2.7 | Gamepad control for contraptions. Optional. |
| `bellsandwhistles` | 0.4.5 | Create visual add-ons. Optional. |
Not on Modrinth under the slugs tried: Create Crafts & Additions is `createaddition` (above); `create-slice-and-dice`,
`create-hypertube`, `create-interactive` returned no project.

### Cozy base and food (Sarah's old list)
| Slug | Found | Notes |
|---|---|---|
| `farmers-delight` | 1.3.4 | Cooking/farming backbone. |
| `cooking-for-blockheads` | 16.0.15 | |
| `farming-for-blockheads` | 14.0.4 | |
| `gravestone-mod` | 1.0.35 | |
| `sophisticated-backpacks` | 3.26.19 | |
| `small-ships` | 2.0.2 | |
| `artifacts` | 9.5.19 | Needs Curios. |
| `curios` | 5.14.1 | |
| `waystones` | 14.1.21 | |
| `lootr` | 0.7.35 | |
| `botania` | 456 | Sarah's pick; heavy magic mod. Keep unless the laptop struggles. |
| `simple-backups` | 3.1.24 | Automatic world backups (Create contraptions and a beta dragon mod can corrupt a world). |

### World and structures
| Slug | Found | Notes |
|---|---|---|
| `terralith` | 2.5.4 | Terrain/biome overhaul. |
| `tectonic` | 3.0.17 | Terrain shaping, Terralith-compatible. |
| `regions-unexplored` or `biomes-o-plenty` | 0.5.6 / 19.0.0.96 | One of the two, only if more biomes are wanted. |
| `yungs-api` | 4.0.6 | Library for the YUNG's mods. |
| `yungs-better-caves` | 2.0.7 | |
| `yungs-better-dungeons` | 4.0.4 | |
| `yungs-better-mineshafts` | 4.0.4 | |
| `yungs-better-strongholds` | 4.0.3 | |
| `yungs-better-ocean-monuments` | 3.0.4 | |
| `better-village` | 3.3.1 | Sarah's old pick. `ct-overhaul-village` 3.4.14 is the alternative. |
| `valhelsia-structures` | 1.1.2 | Sarah's old pick; extra structures. |
| `natures-compass` | 1.12.0 | |

### Quality of life
| Slug | Found | Notes |
|---|---|---|
| `jei` | 15.74.0 | |
| `journeymap` | 6.0.7 | |
| `appleskin` | 2.5.1 | |
| `jade` | 11.13.3 | |
| `mouse-tweaks` | 2.25.1 | |
| `clumps` | 12.0.0.4 | |
| `swing-through-grass` | 1.1.0 | |
| `snow-under-trees` | 1.4.12 | |
| `ore-excavation` | 1.13.170 | Sarah's old pick; vein mining. Keep alongside `create-ore-excavation`. |

### Performance and shaders
| Slug | Found | Notes |
|---|---|---|
| `embeddium` | 0.3.31 | Renderer (or `rubidium` 0.7.1). |
| `oculus` | 1.8.0 | Shader loader; Eclipse needs 1.6.11 or newer. |
| `canary` | 0.3.3 | Logic optimizations. |
| `ferrite-core` | 6.0.1 | Memory. |
| `modernfix` | 5.27.91 | Startup and memory. |
| `entityculling` | 1.11.3 | Helps with Create contraptions and many animals. |
| `chunky` | 1.3.146 | Pre-generate the world on the PC server (Terralith + Tectonic chunks are slow to generate). Optional. |
| `dynamic-fps` | 3.11.4 | Optional for the laptop. |

## Tier 2: optional depth (heavier; PC first)
| Slug | Found | Notes |
|---|---|---|
| `create-diesel-generators` | 1.3.12 | Fuel power. |
| `create-encased` | 1.8-ht2 | More encased machinery. |
| `create-bits-n-bobs` | 0.0.41 | Extra building/utility blocks. |
| `create-dragons-plus` | 1.11.9 | Dragon-themed Create content. |
| `ae2` | 15.4.12 | Applied Energistics 2 storage/autocrafting. |

## Dropped
GregTech-based packs (linear), Cobblemon and Pixelmon (one creature mod only), `create-oxidized` (tiny), Create Slice & Dice
(no project found), FTB Quests and any quest mod (Ben, 2026-11-03: no quests).

Dropped in the 2026-11-03 review: `immediatelyfast` (only 1.21.x builds, wrongly tagged), `create-design-n-decor` (last
1.20.1 build 0.4.0b from 2024, before Create 6), `create-ultimine` (overlaps Ore Excavation), Pam's HarvestCraft 2
(crops and trees mods missing on 1.20.1 Forge; Farmer's Delight covers food), `mekanism` (heavy, a second tech chain),
Goblin Traders and Curious Elytra (no Modrinth project), ExpandAbility (no 1.20.1 build), Valhelsia Tweaks, Useful
Backpacks (Sophisticated Backpacks instead), Essential (not needed with Prism),
Adorable Hamster Pets, Animal Garden Owl and Pet Shop (Ben, 2026-11-03: not needed). Library Ferret, Caelus API,
EnchantmentDescriptions, Bookshelf, U Team Core and Cloth Config are libraries: packwiz adds them only if a mod needs
them.
