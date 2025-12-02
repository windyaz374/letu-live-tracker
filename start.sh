#!/bin/bash

echo "========================================"
echo "Letu Live Tracker - Starting Application"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed"
    echo "Please install Python3 first"
    exit 1
fi

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "[ERROR] Node.js is not installed"
    echo "Please install Node.js first"
    exit 1
fi

echo "[1/4] Checking backend dependencies..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

if [ ! -d "venv/lib/python*/site-packages/flask" ]; then
    echo "Installing Python dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "[2/4] Checking frontend dependencies..."
cd ../frontend

if [ ! -d "node_modules" ]; then
    echo "Installing Node.js dependencies..."
    npm install
fi

echo ""
echo "[3/4] Starting backend server..."
cd ../backend
gnome-terminal -- bash -c "source venv/bin/activate && python app.py; exec bash" 2>/dev/null || \
xterm -e "source venv/bin/activate && python app.py" 2>/dev/null || \
(source venv/bin/activate && python app.py &)

echo ""
echo "[4/4] Starting frontend server..."
cd ../frontend
sleep 3
gnome-terminal -- bash -c "npm run dev; exec bash" 2>/dev/null || \
xterm -e "npm run dev" 2>/dev/null || \
(npm run dev &)

echo ""
echo "========================================"
echo "Application started successfully!"
echo "========================================"
echo ""
echo "Backend:  http://localhost:5000"
echo "Frontend: http://localhost:5173"
echo ""
echo "Opening browser..."
sleep 2

# Try to open browser
xdg-open http://localhost:5173 2>/dev/null || \
open http://localhost:5173 2>/dev/null || \
echo "Please open http://localhost:5173 in your browser"

echo ""
echo "Press Ctrl+C to stop the application"
wait
