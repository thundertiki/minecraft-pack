# Register the hourly "Minecraft backup archive" task for the current user (no admin needed).
# Rerun on a new computer after cloning the repo. Runs only while the user is signed in (Google Drive needs that too).
$script = Join-Path $PSScriptRoot 'archive-backups.ps1'
$action = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval (New-TimeSpan -Hours 1)
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Hours 2)
Register-ScheduledTask -TaskName 'Minecraft backup archive' -Action $action -Trigger $trigger -Settings $settings `
    -Description 'Copies C:\MinecraftServer\simplebackups zips to G:\My Drive\Minecraft\world-backups (minecraft-pack tools/backup-archive)' -Force
