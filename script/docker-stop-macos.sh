#!/bin/bash

echo "========================================"
echo "Letu Live Tracker - Docker Stop (macOS)"
echo "========================================"
echo ""

# Change to script directory's parent (project root)
cd "$(dirname "$0")"

echo "Stopping containers..."
docker-compose down

echo ""
echo "✓ Application stopped successfully"
echo ""
echo "To remove all data and start fresh:"
echo "  docker-compose down -v"
echo ""
echo "To view stopped containers:"
echo "  docker ps -a"
echo ""
