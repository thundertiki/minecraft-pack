# Modlist (proposed 2026-11-02, two candidate lines)

Decision from Ben: **one creature mod, not both**: Cobblemon or Alex's Mobs. That splits the pack into two lines:
- **Line A: Minecraft 1.21.1, NeoForge, Cobblemon** (no Alex's Mobs).
- **Line B: Minecraft 1.20.1, Forge, Alex's Mobs** (no Cobblemon).

"Found" is the newest Modrinth version tagged with that Minecraft version and loader, checked with the Modrinth API on
2026-11-02. `none` = no build for that version and loader. **Check** = not confirmed, verify before adding. Packwiz adds
required library dependencies (Citadel, GeckoLib, Balm, Architectury and so on) automatically; they are not listed.
Counts are mods before libraries.

## Why Cobblemon is not in Line B
Cobblemon on 1.20.1 Forge stops at 1.5.2 (2026-11-02). Riding, which arrives in Cobblemon 1.7 and later, and the Mega
Showdown add-on need 1.21.1. So Line B would be an old Cobblemon, not the current one. If Cobblemon is the hook, pick Line A.

## Why Alex's Mobs is not in Line A
There is no official 1.21.1 NeoForge build on Modrinth (the official project stops at 1.20.1). Community ports exist
(`alexs-mobs-continued` 2.2.4 and `alexs-mobs-1.21.1` 1.22.17); they are unofficial. Line A therefore uses small shoulder-pet
mods instead (below) and no Alex's Mobs.

## Shared mods (same role in both lines; versions differ)

### Creatures and pets
| Slug | A: 1.21.1 NeoForge | B: 1.20.1 Forge | Notes |
|---|---|---|---|
| `cobblemon` | 1.8.4 | not used | **Line A core.** Open source, Showdown battles, riding built in (1.7+). |
| `cobblemon-mega-showdown` | 1.3.3 | none | A only. Optional. |
| `rctmod` (+ `rctapi`) | 0.19.2-beta | not used | A only. NPC trainers. Beta. |
| `more-radical-trainers` | 1.8.1 | not used | A only. Optional. |
| `cobbledollars` | 2.0.0 Beta | not used | A only. Currency/shops. Beta. |
| `cobblemon-quests` | 1.2.0 | not used | A only. Cobblemon questline. |
| `alexs-mobs` | none (community ports only) | 1.22.9 | **Line B core.** About 89 animals; capuchin monkey rides on the shoulder. Needs Citadel. |
| `naturalist` | Check | 2.0.9 | B. Gentle wildlife (bears, deer, butterflies). |
| `perch` | 2.1.0 | none | Parrots on the shoulder. Tiny mod (about 5K downloads). |
| `adorable-hamster-pets` | 3.7.0 | 3.7.0 | Hamsters; shoulder launch. About 5.7M downloads. |
| `animal-garden-owl` | 1.2.2 | 1.1.0 | Owls rest on the shoulder (per the mod page). |
| `animal-garden-olive-baboon` | 1.0.0 | 1.0.0 | **Check** whether it sits on the shoulder; about 6K downloads. |
| `pet-shop` | Check | 0.2.2 | Parrot "Stay" puts it on the shoulder. |
| `dmr` / `dragon-mounts-legacy` | `dmr` 1.9.2 | `dragon-mounts-legacy` 1.2.3-beta | Sarah's Dragon Mounts Legacy has no 1.21.1 build; `dmr` replaces it. |
| `waystones-teleport-pets` | 1.2 | 1.2 | Pets follow Waystones teleports. |

Left out: `cobblemon-fight-or-flight-reborn` (makes wild creatures aggressive; not cozy).

### Tech (Create base)
| Slug | A | B | Notes |
|---|---|---|---|
| `create` | 6.0.10 | 6.0.8 | Tech spine: visual, non-linear. |
| `createaddition` | 1.7.2 | 1.3.3 | Electricity bridge. |
| `create-steam-n-rails` | none | 1.7.3 | Trains. |
| `create-new-age` | 1.2.0 | 1.2.0 | Power generation. |
| `create-design-n-decor` | 2.2b | 0.4.0b | Decoration blocks. |

### Cozy base and food (mostly Sarah's old list)
| Slug | A | B | Notes |
|---|---|---|---|
| `farmers-delight` | 1.3.4 | 1.3.4 | Cooking/farming backbone. |
| `cooking-for-blockheads` | 21.1.24 | 16.0.15 | |
| `farming-for-blockheads` | 21.1.14 | 14.0.4 | |
| `pams-harvestcraft-2-food-core` | 1.0.2 | 1.0.5 | |
| `pams-harvestcraft-2-food-extended` | 1.0.0 | 1.0.0 | |
| `pams-harvestcraft-2-crops`, `-trees` | 1.0.0, 1.0.4 | none | Pam's has small download counts; balance against Farmer's Delight or skip. |
| `gravestone-mod` | 1.0.40 | 1.0.35 | |
| `sophisticated-backpacks` | 3.26.19 | 3.26.19 | |
| `small-ships` | 2.0.2 | 2.0.2 | |
| `artifacts` | 13.2.5 | 9.5.19 | |
| `curios` | 9.5.1 | 5.14.1 | |
| `waystones` | 21.1.46 | 14.1.21 | |
| `lootr` | 1.11.38 | 0.7.35 | |
| `botania` | none on Modrinth (check CurseForge) | 456 (1.20.1) | Heavy; may not suit the laptop. |

### World and structures
| Slug | A | B | Notes |
|---|---|---|---|
| `terralith` | 2.6.2 | 2.5.4 | Terrain/biome overhaul. |
| `tectonic` | 3.0.28 | 3.0.17 | Terrain shaping, Terralith-compatible. |
| `regions-unexplored` or `biomes-o-plenty` | 0.6.3 / 21.1.0.14 | 0.5.6 / 19.0.0.96 | One of the two, only if more biomes are wanted. |
| `yungs-api` | 5.1.9 | 4.0.6 | Library for the YUNG's mods. |
| `yungs-better-caves` | 3.1.6 | 2.0.7 | |
| `yungs-better-dungeons` | 5.1.4 | 4.0.4 | |
| `yungs-better-mineshafts` | 5.1.1 | 4.0.4 | |
| `yungs-better-strongholds` | 5.1.3 | 4.0.3 | |
| `yungs-better-ocean-monuments` | 4.1.2 | 3.0.4 | |
| `ct-overhaul-village` | 3.6.3 | 3.4.14 | Village overhaul. `better-village` 3.3.1 also exists on 1.20.1 (Sarah's old pick). |
| `natures-compass` | 3.4.0 | 1.12.0 | |

### Quality of life
| Slug | A | B | Notes |
|---|---|---|---|
| `jei` | 19.70 | 15.74 | |
| `journeymap` | 6.0.9 | 6.0.7 | |
| `appleskin` | 3.0.9 | 2.5.1 | |
| `jade` | 15.10.6 | 11.13.3 | |
| `mouse-tweaks` | 2.26.1 | 2.25.1 | |
| `clumps` | 19.0.0.1 | 12.0.0.4 | |
| `swing-through-grass` | 1.1.0 | 1.1.0 | |
| `snow-under-trees` | 1.5.1 | 1.4.12 | |
| `ore-excavation` | none (newest is 1.21) | 1.13.170 | Sarah's old pick. In Line A use `veinminer` (**Check**). |
| `veinminer` | Check | 1.1.0 | |

### Performance and shaders
| Slug | A | B | Notes |
|---|---|---|---|
| Renderer | `sodium` 0.8.13 | `embeddium` 0.3.31 (or `rubidium` 0.7.1) | |
| Shader loader | `iris` 1.8.14-beta.1 | `oculus` 1.8.0 | Eclipse needs 1.6.11 or newer; both satisfy it. |
| Logic | `lithium` 0.15.4 | `canary` 0.3.3 | |
| `ferrite-core` | 7.0.3 | 6.0.1 | |
| `modernfix` | 5.27.27 | 5.27.91 | |
| `entityculling` | Check | 1.11.3 | |
| `immediatelyfast` | Check | 1.5.5 (tagged 1.20.4; **Check**) | |
| `dynamic-fps` | Check | 3.11.4 | |

### Quests
`ftb-quests` is not on Modrinth for either line; add with `packwiz curseforge add` (**Check** that CurseForge allows
third-party download for it). Line A can also use `cobblemon-quests`. Line B has no Modrinth quest mod chosen yet.

## Tier 2 (optional, heavier)
| Slug | A | B |
|---|---|---|
| `ae2` | 19.2.18 | 15.4.12 |
| `mekanism` | 10.7.19 | 10.4.16.80 |
Probably PC only.

## Line comparison
| | Line A: 1.21.1 NeoForge + Cobblemon | Line B: 1.20.1 Forge + Alex's Mobs |
|---|---|---|
| Creatures | Current Cobblemon with riding; shoulder pets via Perch, hamster, owl, baboon (**Check**) | Official Alex's Mobs (monkey on shoulder) and Naturalist; no Pokémon-style mod |
| Sarah's old list | Loses Botania (maybe CurseForge), Ore Excavation, Dragon Mounts Legacy (replaced), Create Steam 'n Rails | Keeps nearly everything: Botania, Dragon Mounts Legacy, Ore Excavation, Steam 'n Rails; Pam's crops/trees missing |
| Vanilla | Trial chambers, mace, Crafter | 1.20.1 vanilla only (backports exist, unofficial) |
| Risk | Newer ecosystem, fewer old mods | Older versions; Cobblemon stuck at 1.5.2 if swapped back in |

## Not checked from Sarah's old list, Opus to decide
Goblin Traders (no Modrinth project under that slug), Curious Elytra (same), ExpandAbility (no 1.20.1 build found),
Valhelsia Structures (1.1.2 exists on 1.20.1) and Tweaks, Useful Backpacks (2.0.1 exists on 1.20.1; replaced by
Sophisticated Backpacks), Essential Mod (not needed with Prism), Library Ferret, Caelus API (3.2.0 exists on 1.20.1),
EnchantmentDescriptions, Bookshelf, U Team Core, Cloth Config.

## Dropped
GregTech-based packs (linear), Pixelmon (heavier, own gym structure), running both Cobblemon and Alex's Mobs.
