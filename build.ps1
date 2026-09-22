# =========================================================
# Zary Build Script
# =========================================================

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "========================================"
Write-Host "          Zary Build System"
Write-Host "========================================"
Write-Host ""

# Move to project directory
Set-Location $PSScriptRoot

Write-Host "[1/3] Cleaning previous build..."
Write-Host ""

if (Test-Path "build") {
    Remove-Item "build" -Recurse -Force
}

if (Test-Path "dist\zary.exe") {
    Remove-Item "dist\zary.exe" -Force
}

Write-Host "[2/3] Building Zary executable..."
Write-Host ""

python -m PyInstaller --onefile --name zary zary.py

if (-not (Test-Path "dist\zary.exe")) {
    Write-Host ""
    Write-Host "ERROR: Build failed."
    exit 1
}

Write-Host ""
Write-Host "[3/3] Build completed successfully."
Write-Host ""

Write-Host "Executable:"
Write-Host "  $PSScriptRoot\dist\zary.exe"

Write-Host ""
Write-Host "Testing version..."
Write-Host ""

& ".\dist\zary.exe" --version

Write-Host ""
Write-Host "========================================"
Write-Host "          Build Successful"
Write-Host "========================================"
Write-Host ""