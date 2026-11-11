param([string]$Repo = 'C:\Users\jback\Downloads\a\AI-SI-TSI')
$ErrorActionPreference = 'Stop'
$Source = Split-Path -Parent $MyInvocation.MyCommand.Path
if (-not (Test-Path -LiteralPath $Repo -PathType Container)) {
  throw "Brak repozytorium lokalnego: $Repo"
}
$Target = Join-Path $Repo 'tools\tsi_wikimemory\stage044'
New-Item -ItemType Directory -Path $Target -Force | Out-Null
$Files = @('read_policy.py','audit_043.py','test_policy.py','README.md','wikimemory.py','search.py','result.json')
foreach ($File in $Files) {
  $S = Join-Path $Source $File
  if (-not (Test-Path -LiteralPath $S -PathType Leaf)) { throw "Brak pliku: $S" }
  $T = Join-Path $Target $File
  if (Test-Path -LiteralPath $T) {
    $Stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
    Copy-Item -LiteralPath $T -Destination "$T.backup-$Stamp" -ErrorAction Stop
  }
  Copy-Item -LiteralPath $S -Destination $T -Force
}
Write-Host "Zainstalowano etap 044 w $Target"
Write-Host 'Nie zmieniono checkpointow .pt ani panelu TSI.'
Write-Host "Test: cd '$Target'; python test_policy.py"
