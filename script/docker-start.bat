@echo off
echo ========================================
echo Letu Live Tracker - Docker Startup
echo ========================================
echo.

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

echo [1/5] Checking Docker...
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running
    echo Please start Docker Desktop and try again
    pause
    exit /b 1
)
echo √ Docker is running

echo.
echo [2/5] Checking credentials...
if not exist "backend\credentials.json" (
    echo [WARNING] credentials.json not found
    echo.
    echo Please follow these steps:
    echo 1. Complete Google Sheets setup (see GOOGLE_SHEETS_SETUP.md)
    echo 2. Place credentials.json in backend\ folder
    echo 3. Run this script again
    echo.
    pause
    exit /b 1
)
echo √ credentials.json found

echo.
echo [3/5] Creating data directory...
if not exist "data" mkdir data
echo √ Data directory ready

echo.
echo [4/5] Building Docker image...
echo This may take 5-10 minutes on first run...
docker-compose build
if errorlevel 1 (
    echo [ERROR] Failed to build Docker image
    pause
    exit /b 1
)
echo √ Docker image built successfully

echo.
echo [5/5] Starting application...
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
echo Backend API:  http://localhost:5000
echo Frontend:     http://localhost:5173
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul

start http://localhost:5173

echo.
echo To view logs:    docker-compose logs -f
echo To stop:         docker-compose down
echo To restart:      docker-compose restart
echo.
echo Press any key to exit...
pause >nul
