# Create all SQLite DBs from converted scripts (edit paths if needed)
# Run with: powershell -ExecutionPolicy Bypass -File .\create_all_dbs.ps1
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$sqlite = Join-Path $root "..\..\sqlite3.exe"   # adjust if needed

$targets = @(
    @{ db = "..\04_DB\sqlite\colonial.db"; script = "..\01_SQLite_Converted\colonial\colonial_sqlite.sql" },
    @{ db = "..\04_DB\sqlite\solmaris.db"; script = "..\01_SQLite_Converted\solmaris\solmaris_sqlite.sql" },
    @{ db = "..\04_DB\sqlite\tal.db";       script = "..\01_SQLite_Converted\tal\tal_sqlite.sql" },
    @{ db = "..\04_DB\sqlite\postlab.db";   script = "..\01_SQLite_Converted\adventure_trip\adventure_trip.sql" }
)

foreach ($t in $targets) {
    $dbPath = Resolve-Path (Join-Path $root $t.db)
    $scriptPath = Resolve-Path (Join-Path $root $t.script)
    & $sqlite $dbPath ".read $scriptPath"
    Write-Host "Built DB:" $dbPath
}
