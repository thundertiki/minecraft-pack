# minecraft-pack: Ben and Sarah's modpack (Create + Alex's Mobs + cozy base, built with packwiz, played in Prism)

Target: Minecraft 1.20.1 on Forge, focused on Create (tech) and Alex's Mobs (creatures); one creature mod only, so no
Cobblemon. See `docs/design.md`. Must run on Ben's work laptop (8 GB RAM total, so about 4 to 5 GB for the game) and
his PC (which hosts the server). Sarah plays too; Botania and Pam's HarvestCraft 2 are
her non-negotiables. Non-linear: normal Create progression, no quests, no
recipe locks.

## Rules
- The pack is a packwiz repo: mods are `.pw.toml` files, never jars. Add with `packwiz modrinth add <slug>`, or
  `packwiz curseforge add` only when a mod is not on Modrinth. Packwiz pulls in required
  dependencies itself.
- Every mod must have a build for the chosen Minecraft version and loader before it is added. Check the Modrinth API, never guess.
  Version/loader check: `docs/modlist.md` has the slug and the version found on 2026-11-02.
- Keep the pack near 100 mods including libraries (laptop RAM). Heavy additions (AE2) are optional tier 2.
- Shaders (Eclipse, via Oculus 1.6.11 or newer) are optional and off by default on the laptop. Never put the shader
  zip in the pack; each machine installs it.
- Sarah's mods that do not exist on 1.20.1 Forge get a replacement or are dropped: say so in `docs/modlist.md`.
- Every pack change updates `docs/modlist.md` (and `docs/design.md` if a decision changes) in the same commit.
- Never commit jars, saves, `options.txt` or keys. Notes and plans go in the vault, not here.

## Where things are
- `docs/design.md`: version choice, laptop/PC profiles, Alex's Mobs, progression.
- `docs/modlist.md`: every candidate mod, slug, source, verified version, role, risk.
- `docs/setup.md`: Prism client and PC server install.
- `docs/next.md`: what is in flight. `docs/dead-ends.md`: what failed.

## Skills
None yet. Prefix if added: `mc-`.
