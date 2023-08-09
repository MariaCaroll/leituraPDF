$exclude = @("venv", "leituraPDF.zip")
$files = Get-ChildItem -Path . -Exclude $exclude
Compress-Archive -Path $files -DestinationPath "leituraPDF.zip" -Force