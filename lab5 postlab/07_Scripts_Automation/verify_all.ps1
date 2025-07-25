# Verify all created DBs (runs the verify_*.sql files)
# Run with: powershell -ExecutionPolicy Bypass -File .\verify_all.ps1
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$sqlite = Join-Path $root "..\..\sqlite3.exe"   # adjust if needed

$checks = @(
    @{ db = "..\04_DB\sqlite\colonial.db"; script = "..\01_SQLite_Converted\colonial\verify_colonial.sql"; out = "..\06_Results\logs\verify_colonial.log" },
    @{ db = "..\04_DB\sqlite\solmaris.db"; script = "..\01_SQLite_Converted\solmaris\verify_solmaris.sql"; out = "..\06_Results\logs\verify_solmaris.log" },
    @{ db = "..\04_DB\sqlite\tal.db";       script = "..\01_SQLite_Converted\tal\verify_tal.sql";           out = "..\06_Results\logs\verify_tal.log" },
    @{ db = "..\04_DB\sqlite\postlab.db";   script = "..\01_SQLite_Converted\adventure_trip\verify_adventure_trip.sql"; out = "..\06_Results\logs\verify_adventure_trip.log" }
)

foreach ($c in $checks) {
    $dbPath = Resolve-Path (Join-Path $root $c.db)
    $scriptPath = Resolve-Path (Join-Path $root $c.script)
    $outPath = Resolve-Path (Join-Path $root $c.out)
    & $sqlite $dbPath ".read $scriptPath" *> $outPath
    Write-Host "Verified:" $dbPath "->" $outPath
}
