# World timelapse (BlueMap renders of backups)

Each frame is one Simple Backups zip rendered by the BlueMap 5.3 CLI (Java 17; the 5.29 CLI needs Java 25) and
stitched into a top-down PNG, 1 pixel per block, 3000 x 3000 around 0,0 (`--radius`).

- Script: `tools/timelapse/render_backup.py [zip]` (newest backup if none; skips a date already rendered). Run it with
  `C:\Users\Benjamen\venvs\mc-timelapse\Scripts\python.exe -I` (Pillow is installed there).
- Machine files (not in the repo): `C:\MinecraftServer\timelapse\` holds the CLI jar, `config/` (absolute paths,
  hires layer not saved, `accept-download: true`), `data/` (Minecraft client jar), `frames/` (the output).
- Modded blocks: the script hard-links the server's `mods/*.jar` into `config/packs` before each render.
- Video: `ffmpeg -framerate 8 -pattern_type glob -i "frames/*.png" -vf "scale=1080:-2" -pix_fmt yuv420p timelapse.mp4`
  run in `C:\MinecraftServer\timelapse` (the glob pattern needs ffmpeg's glob support; else list the files).

## Long-term plan
- Frames are the archive: rendering the newest backup once a day keeps a frame per day without keeping old zips.
- Keep one zip a month in `timelapse/archive/` for re-rendering later with a different area or a 3D view.
- Watch disk use after pre-generating: a world 3000 blocks wide is a few GB, and Simple Backups keeps 40 full zips.
