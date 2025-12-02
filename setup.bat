@echo off
REM Setup script for Windows developers
REM Run this once after cloning the repository

echo ======================================
echo Letu Live Tracker - Development Setup
echo ======================================
echo.

REM Check prerequisites
echo [1/5] Checking prerequisites...

python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed
    echo Please install from https://www.python.org/downloads/
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('python --version') do echo √ Python: %%i

node --version >nul 2>&1
if errorlevel 1 (
    echo X Node.js is not installed
    echo Please install from https://nodejs.org/
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('node --version') do echo √ Node.js: %%i

npm --version >nul 2>&1
if errorlevel 1 (
    echo X npm is not installed
    pause
    exit /b 1
)
for /f "tokens=*" %%i in ('npm --version') do echo √ npm: %%i

REM Setup backend
echo.
echo [2/5] Setting up Python backend...
cd backend

if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install --upgrade pip >nul 2>&1
pip install -r requirements.txt

echo √ Backend dependencies installed

REM Check for credentials
if not exist credentials.json (
    echo.
    echo ⚠ Warning: credentials.json not found
    echo   Please follow GOOGLE_SHEETS_SETUP.md to create it
)

REM Setup frontend
echo.
echo [3/5] Setting up React frontend...
cd ..\frontend

echo Installing Node.js dependencies...
call npm install

echo √ Frontend dependencies installed

REM Create .env if needed
cd ..\backend
if not exist .env (
    echo.
    echo [4/5] Creating .env file...
    copy .env.template .env
    echo √ .env file created from template
) else (
    echo.
    echo [4/5] .env file already exists
)

echo.
echo [5/5] Setup verification...
cd ..

echo √ All setup steps completed

echo.
echo ======================================
echo Setup completed successfully!
echo ======================================
echo.
echo Next steps:
echo 1. Setup Google Sheets API (see GOOGLE_SHEETS_SETUP.md)
echo 2. Place credentials.json in backend\ folder
echo 3. Run: start.bat
echo.
echo For testing:
echo   Backend scraper: cd backend ^&^& venv\Scripts\activate ^&^& python test_scraper.py
echo   Google Sheets:   cd backend ^&^& venv\Scripts\activate ^&^& python test_sheets.py ^<sheet_url^>
echo.
pause
