#!/bin/bash

echo "========================================"
echo "Letu Live Tracker - Docker Startup (macOS)"
echo "========================================"
echo ""

# Change to script directory's parent (project root)
cd "$(dirname "$0")"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "[ERROR] Docker is not installed"
    echo ""
    echo "Please install Docker Desktop for Mac:"
    echo "https://docs.docker.com/desktop/install/mac-install/"
    echo ""
    exit 1
fi

echo "[1/6] Checking Docker..."
if ! docker info &> /dev/null; then
    echo "[ERROR] Docker is not running"
    echo ""
    echo "Please start Docker Desktop and try again"
    echo "You can find it in your Applications folder"
    exit 1
fi
echo "✓ Docker is running"

echo ""
echo "[2/6] Checking credentials..."
if [ ! -f "backend/credentials.json" ]; then
    echo "[WARNING] credentials.json not found"
    echo ""
    echo "Current directory: $(pwd)"
    echo "Looking for: $(pwd)/backend/credentials.json"
    echo ""
    echo "Please follow these steps:"
    echo "1. Complete Google Sheets setup (see doc/GOOGLE_SHEETS_SETUP.md)"
    echo "2. Place credentials.json in backend/ folder"
    echo "3. Run this script again"
    echo ""
    exit 1
fi
echo "✓ credentials.json found"

echo ""
echo "[3/6] Creating data directory..."
mkdir -p data
echo "✓ Data directory ready"

echo ""
echo "[4/6] Cleaning up old containers..."
docker-compose down -v 2>/dev/null || true
docker rm -f letu-live-tracker 2>/dev/null || true
echo "✓ Cleanup complete"

echo ""
echo "[5/6] Building Docker image..."
echo "This may take 5-10 minutes on first run..."
if ! docker-compose build --no-cache; then
    echo "[ERROR] Failed to build Docker image"
    exit 1
fi
echo "✓ Docker image built successfully"

echo ""
echo "[6/6] Starting application..."
if ! docker-compose up -d; then
    echo "[ERROR] Failed to start application"
    exit 1
fi

echo ""
echo "========================================"
echo "Application started successfully!"
echo "========================================"
echo ""
echo "Access the application at:"
echo "  http://localhost:5000"
echo ""
echo "Opening browser in 3 seconds..."
sleep 3

# Open browser (macOS)
open http://localhost:5000 2>/dev/null || echo "Please open http://localhost:5000 in your browser"

echo ""
echo "Useful commands:"
echo "  View logs:   docker-compose logs -f"
echo "  Stop:        docker-compose down"
echo "  Restart:     docker-compose restart"
echo ""
echo "Press any key to continue..."
read -n 1 -s
