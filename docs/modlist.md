# Modlist (proposed 2026-11-02)

Platform: Minecraft 1.21.1, NeoForge. "Found" is the newest Modrinth version tagged 1.21.1 + neoforge on 2026-11-02
(Modrinth API). Anything marked **Check** was not confirmed and must be verified before it is added. Packwiz adds
required library dependencies (Architectury-style libs, Citadel, GeckoLib, Balm and so on) automatically; they are not
listed.

## Tier 1: the base pack (about 60 mods before libraries)

### Creatures
| Slug | Found | Role / risk |
|---|---|---|
| `cobblemon` | 1.8.4NF | The core. Pokémon-style creatures spawn in biomes; open source, Showdown battle engine. |
| `cobblemon-mega-showdown` | 1.3.3+1.8.4 | Mega evolution and extra battle mechanics. Optional. |
| `rctmod`, `rctapi` | 0.19.2-beta, 0.16.2-beta | Radical Cobblemon Trainers: NPC trainers and structures. Beta. |
| `more-radical-trainers` | 1.8.1 | Extra trainers for the above. Optional. |
| `cobbledollars` | 2.0.0 Beta | Currency and shops for Cobblemon. Beta. |
| `cobblemon-quests` | 1.2.0 | Cobblemon-specific quests (the cozy questline). |
| `alexs-mobs-continued` | 2.2.4 | Community port of Alex's Mobs; the capuchin monkey rides on the shoulder. **Unofficial.** Alternative port: `alexs-mobs-1.21.1` 1.22.17. Requires Citadel. |
| `perch` | 2.1.0 | Parrots on the shoulder. Small mod (about 5K downloads). |
| `dmr` | 1.9.2 | Dragon Mounts Respawned, replacing Sarah's Dragon Mounts Legacy (which has no NeoForge 1.21.1 build). |
| `waystones-teleport-pets` | Check | Addon so pets follow Waystones teleports. |

Left out on purpose: `cobblemon-fight-or-flight-reborn` (makes wild creatures aggressive; not cozy).
`cobblemon-create-industries` and `berryharvester` (Create + Cobblemon crossovers, found in search, versions not verified): Check.

### Tech (Create base)
| Slug | Found | Role / risk |
|---|---|---|
| `create` | 6.0.10 | The tech spine: visual, non-linear automation. |
| `createaddition` | 1.7.2 | Create Crafts & Additions: electricity bridge. |
| `create-new-age` | Check | Create addon for power generation. |
| `create-design-n-decor` | Check | Building/decoration blocks. |
| `create-diesel-generators` | Check | Fuel power. Optional. |

Not available on 1.21.1 NeoForge (Modrinth): `create-steam-n-rails` (newest build shows 1.20.1). Check CurseForge.

### Cozy base and food
| Slug | Found | Role / risk |
|---|---|---|
| `farmers-delight` | 1.3.4 | The cooking and farming backbone, matches the Cobblemon berry/cooking packs. |
| `cooking-for-blockheads` | 21.1.24 | From Sarah's pack. |
| `farming-for-blockheads` | 21.1.14 | From Sarah's pack. |
| `pams-harvestcraft-2-crops`, `-food-core`, `-food-extended`, `-trees` | 1.0.0 to 1.0.4 | From Sarah's pack. Small download counts on 1.21.1; balance against Farmer's Delight. |
| `gravestone-mod` | 1.0.40 | From Sarah's pack. |
| `sophisticated-backpacks` | 3.26.19 | From Sarah's pack. |
| `small-ships` | 2.0.2 | From Sarah's pack. |
| `artifacts` | 13.2.5 | From Sarah's pack. Needs Curios. |
| `curios` | 9.5.1 | Library for Artifacts and Backpacks. |
| `waystones` | 21.1.46 | Fast travel. |
| `lootr` | 1.11.38 | Per-player loot chests. |
| Botania | **Not on Modrinth for 1.21.1 NeoForge** | Check CurseForge. Heavy; may not fit the laptop. |

### World and structures
| Slug | Found | Role / risk |
|---|---|---|
| `terralith` | 2.6.2 | Terrain/biome overhaul (95+ biomes). |
| `tectonic` | 3.0.28 | Terrain shaping, Terralith-compatible. |
| `regions-unexplored` or `biomes-o-plenty` | 0.6.3 / 21.1.0.14 | One of them, only if more biomes are wanted. Stacking needs weight tuning. |
| `yungs-api` | 1.21.1-NeoForge-5.1.9 | Library for the YUNG's mods. |
| `yungs-better-caves` | 3.1.6 | |
| `yungs-better-dungeons` | 5.1.4 | |
| `yungs-better-mineshafts` | 5.1.1 | |
| `yungs-better-strongholds` | 5.1.3 | |
| `yungs-better-ocean-monuments` | 4.1.2 | |
| `ct-overhaul-village` | 3.6.3 | Replaces Better Village (not found). |
| `natures-compass` | 1.21.1-3.4.0 | |

### Quality of life
| Slug | Found | Role / risk |
|---|---|---|
| `jei` | 19.70 | Recipe viewer. |
| `journeymap` | 6.0.9 | Map. |
| `appleskin` | 3.0.9 | |
| `jade` | Check | Block/mob tooltip. |
| `mouse-tweaks` | Check | |
| `clumps` | 19.0.0.1 | XP orb merging. |
| `swing-through-grass` | 1.1.0 | |
| `snow-under-trees` | 1.5.1 | |
| `veinminer` | Check | Replaces Ore Excavation, which has no 1.21.1 build (newest 1.21). |

### Performance
| Slug | Found | Role / risk |
|---|---|---|
| `sodium` | 0.8.13 | Rendering. |
| `iris` | 1.8.14-beta.1 | Shader loader; Eclipse needs 1.6.11 or newer. |
| `lithium` | 0.15.4 | Game logic. |
| `ferrite-core` | 7.0.3 | Memory. |
| `modernfix` | 5.27.27 | Startup and memory. |
| `entityculling`, `immediatelyfast`, `dynamic-fps` | Check | Optional extras for the laptop. |

### Quests
`ftb-quests` is not on Modrinth. **Check** CurseForge (`packwiz curseforge add`) or an alternative.

## Tier 2 (optional, heavier)
| Slug | Found | Notes |
|---|---|---|
| `ae2` | 19.2.18 | Applied Energistics 2: storage/autocrafting. |
| `mekanism` | 10.7.19 | Heavy tech chain. Probably PC only. |

## Not checked (Sarah's old list), Opus to decide
Caelus API, Curious Elytra, Goblin Traders, Valhelsia Structures/Tweaks, Useful Backpacks (replaced by Sophisticated
Backpacks), ExpandAbility, Essential Mod (not needed with Prism), Library Ferret, Oculus and Rubidium (replaced by Iris and
Sodium on NeoForge), EnchantmentDescriptions, Bookshelf, U Team Core, Cloth Config.

## Dropped
GregTech-based packs (linear), Pixelmon (heavier, own gym structure), Ore Excavation (no 1.21.1 build),
Dragon Mounts Legacy (no NeoForge 1.21.1 build; `dmr` replaces it).
