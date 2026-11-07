# Copy every Simple Backups zip into Google Drive, never deleting anything there.
# Simple Backups keeps only the newest 40 locally; this folder keeps them all. See docs/setup.md (Services on the PC).
param(
    [string]$Source = 'C:\MinecraftServer\simplebackups',
    [string]$Dest = 'G:\My Drive\Minecraft\world-backups',
    [string]$Log = 'C:\MinecraftServer\logs\archive-backups.log'
)
if (-not (Test-Path 'G:\My Drive')) { Add-Content $Log "$(Get-Date -Format s) Google Drive (G:) not mounted; skipped"; exit 1 }
New-Item -ItemType Directory -Force $Dest | Out-Null
# /XO skips zips already copied; no /MIR or /PURGE, so nothing in $Dest is ever removed.
robocopy $Source $Dest *.zip /XO /R:2 /W:10 /NP /NJH /NDL /LOG+:$Log | Out-Null
if ($LASTEXITCODE -ge 8) { exit $LASTEXITCODE } else { exit 0 }
