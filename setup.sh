#!/bin/bash

# Setup script for Linux/Mac developers
# Run this once after cloning the repository

echo "======================================"
echo "Letu Live Tracker - Development Setup"
echo "======================================"
echo ""

# Check prerequisites
echo "[1/5] Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed"
    exit 1
fi
echo "✓ Python3: $(python3 --version)"

if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed"
    exit 1
fi
echo "✓ Node.js: $(node --version)"

if ! command -v npm &> /dev/null; then
    echo "❌ npm is not installed"
    exit 1
fi
echo "✓ npm: $(npm --version)"

# Setup backend
echo ""
echo "[2/5] Setting up Python backend..."
cd backend

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt

echo "✓ Backend dependencies installed"

# Check for credentials
if [ ! -f "credentials.json" ]; then
    echo ""
    echo "⚠️  Warning: credentials.json not found"
    echo "   Please follow GOOGLE_SHEETS_SETUP.md to create it"
fi

# Setup frontend
echo ""
echo "[3/5] Setting up React frontend..."
cd ../frontend

echo "Installing Node.js dependencies..."
npm install

echo "✓ Frontend dependencies installed"

# Create .env if needed
cd ../backend
if [ ! -f ".env" ]; then
    echo ""
    echo "[4/5] Creating .env file..."
    cp .env.template .env
    echo "✓ .env file created from template"
else
    echo ""
    echo "[4/5] .env file already exists"
fi

# Make scripts executable
echo ""
echo "[5/5] Making scripts executable..."
cd ..
chmod +x start.sh
chmod +x backend/test_scraper.py
chmod +x backend/test_sheets.py

echo "✓ Scripts are now executable"

echo ""
echo "======================================"
echo "Setup completed successfully!"
echo "======================================"
echo ""
echo "Next steps:"
echo "1. Setup Google Sheets API (see GOOGLE_SHEETS_SETUP.md)"
echo "2. Place credentials.json in backend/ folder"
echo "3. Run: ./start.sh"
echo ""
echo "For testing:"
echo "  Backend scraper: cd backend && source venv/bin/activate && python test_scraper.py"
echo "  Google Sheets:   cd backend && source venv/bin/activate && python test_sheets.py <sheet_url>"
echo ""
