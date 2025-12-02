@echo off
echo ========================================
echo Letu Live Tracker - Starting Application
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js is not installed or not in PATH
    echo Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo [1/4] Checking backend dependencies...
cd backend
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

if not exist venv\Lib\site-packages\flask (
    echo Installing Python dependencies...
    pip install -r requirements.txt
)

echo.
echo [2/4] Checking frontend dependencies...
cd ..\frontend
if not exist node_modules (
    echo Installing Node.js dependencies...
    call npm install
)

echo.
echo [3/4] Starting backend server...
cd ..\backend
start "Letu Tracker - Backend" cmd /k "venv\Scripts\activate.bat && python app.py"

echo.
echo [4/4] Starting frontend server...
cd ..\frontend
timeout /t 3 /nobreak >nul
start "Letu Tracker - Frontend" cmd /k "npm run dev"

echo.
echo ========================================
echo Application started successfully!
echo ========================================
echo.
echo Backend:  http://localhost:5000
echo Frontend: http://localhost:5173
echo.
echo Press any key to open the application in your browser...
pause >nul

start http://localhost:5173

echo.
echo To stop the application, close the backend and frontend windows.
echo.
pause
