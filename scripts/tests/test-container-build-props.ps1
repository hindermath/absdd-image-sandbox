#Requires -Version 7
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$root = Join-Path ([IO.Path]::GetTempPath()) ('ade-props-' + [guid]::NewGuid().ToString('N'))
$props = (Resolve-Path (Join-Path $PSScriptRoot '../../dotnet/ContainerBuild.props')).Path
try {
    $paths = @('mount_a/project', 'mount/a_project')
    $outputs = @()
    foreach ($relative in $paths) {
        $directory = Join-Path $root $relative
        New-Item -ItemType Directory -Path $directory -Force | Out-Null
        $project = Join-Path $directory 'Probe.csproj'
        Set-Content -LiteralPath $project -Value '<Project Sdk="Microsoft.NET.Sdk" />' -Encoding utf8NoBOM
        Set-Content -LiteralPath (Join-Path $directory 'Directory.Build.props') -Value '<Project><PropertyGroup><RepoProbe>present</RepoProbe></PropertyGroup></Project>' -Encoding utf8NoBOM
        $result = @(& dotnet msbuild $project "-p:DirectoryBuildPropsPath=$props" '-getProperty:BaseIntermediateOutputPath,BaseOutputPath,RepoProbe' '-nologo')
        if ($LASTEXITCODE -ne 0) { throw "MSBuild evaluation failed for $relative" }
        $values = ($result -join "`n") | ConvertFrom-Json -AsHashtable
        if ($values.Properties.RepoProbe -ne 'present') { throw "Repository props import failed for $relative" }
        if (-not $values.Properties.BaseIntermediateOutputPath.StartsWith('/dotnet-build/obj/')) { throw "obj escaped the build volume for $relative" }
        if (-not $values.Properties.BaseOutputPath.StartsWith('/dotnet-build/bin/')) { throw "bin escaped the build volume for $relative" }
        $outputs += $values.Properties.BaseIntermediateOutputPath
    }
    if ($outputs[0] -eq $outputs[1]) { throw 'Different absolute project paths collapsed to one output path' }
    'ContainerBuild.props mount-independent paths: PASS'
} finally {
    if (Test-Path -LiteralPath $root) { Remove-Item -LiteralPath $root -Recurse -Force }
}
