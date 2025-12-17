@echo off
chcp 65001 >nul
echo ========================================
echo   Rotate Images to Landscape Format
echo ========================================
echo.

REM Check if a directory or file has been dragged here
if "%~1"=="" (
    REM No parameter - use current directory
    set "TARGET_DIR=%~dp0"
    echo Processing images in current directory...
) else (
    REM Parameter exists - use it
    set "TARGET_DIR=%~1"
    echo Processing images in: %TARGET_DIR%
)

echo.
python "%~dp0rotate_images.py" "%TARGET_DIR%"

if errorlevel 1 (
    echo.
    echo ERROR: Something went wrong during execution.
    pause
    exit /b 1
)

echo.
pause

