# minecraft-pack: Ben and Sarah's modpack (Cobblemon + Create + cozy base, built with packwiz, played in Prism)

Target: undecided between Line A (1.21.1 NeoForge + Cobblemon) and Line B (1.20.1 Forge + Alex's Mobs); one creature mod
only, never both. See `docs/design.md`. Must run on Ben's work laptop (8 GB RAM total, so about 4 to 5 GB for the game) and
his PC. Sarah plays too. Non-linear: no forced tech progression; quests are optional.

## Rules
- The pack is a packwiz repo: mods are `.pw.toml` files, never jars. Add with `packwiz modrinth add <slug>`, or
  `packwiz curseforge add` only when a mod is not on Modrinth (FTB Quests, Botania). Packwiz pulls in required
  dependencies itself.
- Every mod must have a build for the chosen Minecraft version and loader before it is added. Check the Modrinth API, never guess.
  Version/loader check: `docs/modlist.md` has the slug and the version found on 2026-11-02.
- Keep the pack near 100 mods including libraries (laptop RAM). Heavy additions (Mekanism, AE2) are optional tier 2.
- Shaders (Eclipse, needs Iris 1.6.11 or newer) are optional and off by default on the laptop. Never put the shader
  zip in the pack; each machine installs it.
- Sarah's mods that do not exist on 1.21.1 NeoForge get a replacement or are dropped: say so in `docs/modlist.md`.
- Never commit jars, saves, `options.txt` or keys. Notes and plans go in the vault, not here.

## Where things are
- `docs/design.md`: version choice, laptop/PC profiles, Cobblemon + Alex's Mobs plan, quests.
- `docs/modlist.md`: every candidate mod, slug, source, verified version, role, risk.
- `docs/next.md`: what is in flight. `docs/dead-ends.md`: what failed.

## Skills
None yet. Prefix if added: `mc-`.
