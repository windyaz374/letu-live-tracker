# Letu Live Tracker

A real-time livestream product data scraper that updates Google Sheets automatically.

## Features

- Scrape product data from Shopee livestream sessions
- Real-time updates to Google Sheets
- Simple UI for session management
- Cross-platform support (Linux development, Windows deployment)
- **🐳 Docker support for easy deployment**

## Architecture

- **Frontend**: React (Vite)
- **Backend**: Python Flask with Selenium
- **Data Export**: Google Sheets API
- **Deployment**: Docker (recommended) or traditional installation

## 🚀 Quick Start

### Option 1: Docker (Recommended - Easiest!)

**Prerequisites:** Just Docker Desktop!

```bash
# Windows: Double-click
docker-start.bat

# Linux/Mac: Run
./docker-start.sh
```

📖 See [DOCKER_GUIDE.md](doc/DOCKER_GUIDE.md) for complete Docker instructions.

### Option 2: Traditional Installation

**Prerequisites:**

#### For Windows Users

1. Python 3.8+ ([Download](https://www.python.org/downloads/))
2. Node.js 16+ ([Download](https://nodejs.org/))
3. Chrome browser installed

#### For Linux/Mac Users

1. Python 3.8+
2. Node.js 16+
3. Chrome/Chromium browser

## Installation

### 🐳 Docker Installation (Recommended)

1. Install Docker Desktop: https://www.docker.com/products/docker-desktop
2. Place `credentials.json` in `backend/` folder (see [GOOGLE_SHEETS_SETUP.md](doc/GOOGLE_SHEETS_SETUP.md))
3. Run `docker-start.bat` (Windows) or `./docker-start.sh` (Linux/Mac)

**That's it!** 🎉

### 🔧 Traditional Installation

#### Step 1: Clone the repository

```bash
git clone <repository-url>
cd letu-live-tracker
```

#### Step 2: Backend Setup

**Windows:**
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac:**
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Step 3: Frontend Setup

```bash
cd frontend
npm install
```

#### Step 4: Google Sheets API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Sheets API
4. Create credentials (OAuth 2.0 Client ID)
5. Download the credentials JSON file
6. Place it as `backend/credentials.json`

## Running the Application

### 🐳 With Docker (Recommended)

**Windows:**
```cmd
docker-start.bat
```

**Linux/Mac:**
```bash
./docker-start.sh
```

**Stop:**
```bash
docker-stop.bat  # Windows
./docker-stop.sh # Linux/Mac
```

### 🔧 Traditional Method

**Windows:**
```cmd
start.bat
```

Or manually:
```cmd
# Terminal 1 - Backend
cd backend
venv\Scripts\activate
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

**Linux/Mac:**
```bash
./start.sh
```

Or manually:
```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python app.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## Usage

1. Open the web interface (usually http://localhost:5173)
2. Enter the Shopee livestream Session ID
3. Enter your Google Sheet URL
4. Click "Start Tracking"
5. The tool will scrape data in real-time and update your Google Sheet

## Project Structure

```
letu-live-tracker/
├── backend/
│   ├── app.py              # Flask server
│   ├── scraper.py          # Web scraping logic
│   ├── sheets_handler.py   # Google Sheets integration
│   ├── requirements.txt    # Python dependencies
│   └── credentials.json    # Google API credentials (not in repo)
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── components/
│   │   └── ...
│   └── package.json
├── start.bat               # Windows startup script
├── start.sh               # Linux/Mac startup script
└── README.md
```

## Troubleshooting

### Chrome Driver Issues
- The application will automatically download the correct ChromeDriver
- Make sure Chrome browser is installed

### Google Sheets Permission Error
- Make sure your credentials.json is properly configured
- Grant necessary permissions when prompted

### Port Already in Use
- Backend runs on port 5000
- Frontend runs on port 5173
- Change ports in config if needed

## License

MIT
