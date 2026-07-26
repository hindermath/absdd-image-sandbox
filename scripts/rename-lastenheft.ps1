#Requires -Version 7

<#
.SYNOPSIS
Renames a completed Lastenheft with its feature identifier.

.DESCRIPTION
Validates the Markdown source and feature name, then uses git mv so the
repository records the completed Lastenheft under an archived filename.

.PARAMETER File
Repository-relative path of the Lastenheft Markdown file.

.PARAMETER BranchName
Stable feature or branch identifier appended to the filename.

.EXAMPLE
.\scripts\rename-lastenheft.ps1 -File Lastenheft_Example.md -BranchName 001-example -WhatIf
#>

[CmdletBinding(SupportsShouldProcess, ConfirmImpact = 'Medium')]
param(
  [Parameter(Mandatory)]
  [string]$File,

  [Parameter(Mandatory)]
  [ValidatePattern('^[A-Za-z0-9][A-Za-z0-9._-]*$')]
  [string]$BranchName
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if (-not (Test-Path -LiteralPath $File -PathType Leaf)) {
  throw "Fehler: Datei nicht gefunden: $File / Error: File not found: $File"
}
if ([IO.Path]::GetExtension($File) -ne '.md') {
  throw "Fehler: Lastenheft muss eine Markdown-Datei sein: $File / Error: Requirements file must be Markdown: $File"
}

$directory = Split-Path -Path $File -Parent
if ([string]::IsNullOrEmpty($directory)) {
  $directory = '.'
}
$stem = [IO.Path]::GetFileNameWithoutExtension($File)
$targetPath = Join-Path -Path $directory -ChildPath "$stem.$BranchName.md"

if ((Test-Path -LiteralPath $targetPath) -and
    ([IO.Path]::GetFullPath($targetPath) -ne [IO.Path]::GetFullPath($File))) {
  throw "Fehler: Zieldatei existiert bereits: $targetPath / Error: Target file already exists: $targetPath"
}

if ($PSCmdlet.ShouldProcess($File, "git mv nach / to $targetPath")) {
  & git mv -- $File $targetPath
  if ($LASTEXITCODE -ne 0) {
    throw 'Fehler: git mv fehlgeschlagen / Error: git mv failed'
  }
  Write-Output "Umbenannt / Renamed: $File -> $targetPath"
}
