[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Add-Type -AssemblyName System.Windows.Forms

$folderDialog = New-Object System.Windows.Forms.FolderBrowserDialog
$folderDialog.Description = "Select the folder containing the files to rename."
if ($folderDialog.ShowDialog() -ne "OK") { exit }

$target_folder = $folderDialog.SelectedPath

$old_text = Read-Host "Enter the text to replace"
$new_text = Read-Host "Enter the new text"

Get-ChildItem -Path $target_folder -File | ForEach-Object {
    $newName = $_.Name -replace [regex]::Escape($old_text), $new_text
    if ($_.Name -ne $newName) {
        Rename-Item -Path $_.FullName -NewName $newName
    }
}

Write-Host "Renaming completed successfully!" -ForegroundColor Green
Pause
