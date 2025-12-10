@echo off
echo ========================================
echo Letu Live Tracker - Docker Startup
echo ========================================
echo.

REM Save current directory and change to project root
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%\.."

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed or not running
    echo.
    echo Please install Docker Desktop:
    echo https://www.docker.com/products/docker-desktop
    echo.
    pause
    exit /b 1
)

echo [1/6] Checking Docker...
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)
echo √ Docker is running

echo.
echo [2/6] Checking credentials...
if not exist "backend\credentials.json" (
    echo [WARNING] credentials.json not found
    echo.
    echo Current directory: %CD%
    echo Looking for: %CD%\backend\credentials.json
    echo.
    echo Please follow these steps:
    echo 1. Complete Google Sheets setup (see doc\GOOGLE_SHEETS_SETUP.md)
    echo 2. Place credentials.json in backend\ folder
    echo 3. Run this script again
    echo.
    pause
    exit /b 1
)
echo √ credentials.json found

echo.
echo [3/6] Creating data directory...
if not exist "data" mkdir data
echo √ Data directory ready

echo.
echo [4/6] Cleaning up old containers...
docker-compose down -v >nul 2>&1
docker rm -f letu-live-tracker >nul 2>&1
echo √ Cleanup complete

echo.
echo [5/6] Building Docker image...
echo This may take 5-10 minutes on first run...
docker-compose build --no-cache
if errorlevel 1 (
    echo [ERROR] Failed to build Docker image
    pause
    exit /b 1
)
echo √ Docker image built successfully

echo.
echo [6/6] Starting application...
docker-compose up -d
if errorlevel 1 (
    echo [ERROR] Failed to start application
    pause
    exit /b 1
)

echo.
echo ========================================
echo Application started successfully!
echo ========================================
echo.
echo Access the application at:
echo   http://localhost:5000
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul

start http://localhost:5000

echo.
echo Useful commands:
echo   View logs:   docker-compose logs -f
echo   Stop:        docker-compose down
echo   Restart:     docker-compose restart
echo.
echo Press any key to exit...
pause >nul
