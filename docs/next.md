# Next (one block per task in flight)

## First launch
PC done 2026-11-04: Prism `BenAndSarah-1.20.1` (5 GB, Temurin 17) and the Forge server in `C:\MinecraftServer`
(4 GB). The pack is 90 files at 9d13ea6; the server starts with no missing mods and the world is created.
Next: launch the PC client, check JourneyMap's train-map warning is gone, join the server; then update the
laptop instance and join over Tailscale. Ben still adds the firewall rule (TCP 25565, private) or clicks Allow.
Not verified: the client with the 12 newest mods; the laptop with 90 mods at 4.5 GB.
Read first: docs/setup.md, docs/modlist.md. Don't redo the dependency check (every jar's dependencies are met).

## Test Eclipse
Oculus 1.8.0 with Embeddium on 1.20.1 Forge. Confirm Eclipse loads and check FPS on the laptop's lowest profile.
