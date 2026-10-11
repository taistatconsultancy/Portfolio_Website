# Renders pages/brochure.html to assets/brochure/stephen-mulingwa-brochure.pdf
# using headless Edge or Chrome. Starts the local preview server if needed.
#
# Usage:  powershell -ExecutionPolicy Bypass -File scripts/build-brochure.ps1

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$port = 3123
$url = "http://localhost:$port/brochure"
$out = Join-Path $root 'assets\brochure\stephen-mulingwa-brochure.pdf'

$browser = @(
  "${env:ProgramFiles(x86)}\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Microsoft\Edge\Application\msedge.exe",
  "$env:ProgramFiles\Google\Chrome\Application\chrome.exe",
  "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $browser) { throw 'Microsoft Edge or Google Chrome is required to build the brochure PDF.' }

$server = Start-Process python -ArgumentList "scripts/dev_server.py", $port -WorkingDirectory $root -PassThru -WindowStyle Hidden
try {
  for ($i = 0; $i -lt 30; $i++) {
    try { Invoke-WebRequest -Uri $url -UseBasicParsing -TimeoutSec 2 | Out-Null; break } catch { Start-Sleep -Milliseconds 300 }
  }

  New-Item -ItemType Directory -Force -Path (Split-Path $out) | Out-Null
  if (Test-Path $out) { Remove-Item $out -Force }
  $profileDir = Join-Path $env:TEMP "brochure-pdf-profile"
  $browserArgs = @(
    '--headless', '--disable-gpu', '--no-first-run', "--user-data-dir=`"$profileDir`"",
    '--no-pdf-header-footer', '--print-to-pdf-no-header', '--virtual-time-budget=15000',
    "--print-to-pdf=`"$out`"", $url
  )
  Start-Process -FilePath $browser -ArgumentList $browserArgs -Wait -WindowStyle Hidden

  $deadline = (Get-Date).AddSeconds(30)
  while (-not (Test-Path $out) -and (Get-Date) -lt $deadline) { Start-Sleep -Milliseconds 300 }
  if (-not (Test-Path $out)) { throw 'PDF was not created.' }
  Start-Sleep -Seconds 1
  Write-Host "Wrote $out ($((Get-Item $out).Length) bytes)"
}
finally {
  Stop-Process -Id $server.Id -Force -ErrorAction SilentlyContinue
}
