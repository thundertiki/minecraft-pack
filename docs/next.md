# Next (one block per task in flight)

## Opus review of the proposed modlist
Read `docs/design.md` and `docs/modlist.md` (1.20.1 Forge, Create + Alex's Mobs). Verify the "Check" items, answer the
open questions in `design.md`, decide the Tier 2 question, then say what to cut for the 8 GB laptop.

## Create the packwiz pack
Install packwiz (`go install github.com/packwiz/packwiz@latest`; Go is on the laptop), then
`packwiz init` for 1.21.1 / NeoForge and add the Tier 1 mods from `docs/modlist.md`. Wire the Prism instance's
pre-launch command to the packwiz installer bootstrap. Test on the laptop first.

## Test Eclipse
Iris 1.8.14-beta.1 for 1.21.1 NeoForge exists. Eclipse's README names 1.21.11; confirm it loads on 1.21.1.
