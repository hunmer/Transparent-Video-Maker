@echo off
rem =============================================================
rem  Transparent Video Maker - Windows one-click launcher
rem  Double-click this file to start the app.
rem  "start-tvm.bat --console" runs it inside this window so
rem  Python errors / tracebacks stay visible.
rem =============================================================
setlocal EnableExtensions
cd /d "%~dp0"

set "APP=%~dp0TransparentVideoMaker.py"
if not exist "%APP%" (
    echo [x] TransparentVideoMaker.py was not found next to this script.
    pause
    exit /b 1
)

rem ---- locate a Python interpreter ----------------------------
set "PYW="
set "PYC="
for %%D in ("%ProgramFiles%\Python38" "%ProgramFiles%\Python311" "%ProgramFiles%\Python310") do (
    if not defined PYW if exist "%%~D\pythonw.exe" set "PYW=%%~D\pythonw.exe"
    if not defined PYC if exist "%%~D\python.exe"  set "PYC=%%~D\python.exe"
)
if not defined PYW for /f "delims=" %%I in ('where pythonw 2^>nul') do if not defined PYW set "PYW=%%I"
if not defined PYC for /f "delims=" %%I in ('where python 2^>nul') do if not defined PYC set "PYC=%%I"
if not defined PYW if defined PYC set "PYW=%PYC%"
if not defined PYW (
    echo [x] Python was not found. Install Python 3.10 / 3.11 or add it to PATH.
    pause
    exit /b 1
)

rem ---- "--console": stay in this window, errors visible -------
if /i "%~1"=="--console" (
    "%PYC%" "%APP%"
    echo.
    echo [app exited with code %errorlevel%]
    pause
    exit /b %errorlevel%
)

rem ---- already running? just focus that window ---------------
powershell -NoProfile -ExecutionPolicy Bypass -Command "$p = Get-Process pythonw -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -like 'Transparent Video*' } | Select-Object -First 1; if ($p) { Add-Type -AssemblyName Microsoft.VisualBasic; [Microsoft.VisualBasic.Interaction]::AppActivate($p.Id) | Out-Null; exit 3 } else { exit 0 }"
if "%errorlevel%"=="3" exit /b 0

rem ---- normal start: GUI only, no console window -------------
start "" "%PYW%" "%APP%"
exit /b 0
