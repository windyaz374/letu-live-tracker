# Letu Live Tracker

A real-time livestream product data scraper that updates Google Sheets automatically.

## Features

- Scrape product data from Shopee livestream sessions
- Real-time updates to Google Sheets
- Simple UI for session management
- Cross-platform support (Linux development, Windows deployment)

## Architecture

- **Frontend**: React (Vite)
- **Backend**: Python Flask with Selenium
- **Data Export**: Google Sheets API

## Prerequisites

### For Windows Users

1. Python 3.8+ ([Download](https://www.python.org/downloads/))
2. Node.js 16+ ([Download](https://nodejs.org/))
3. Chrome browser installed

### For Linux/Mac Users

1. Python 3.8+
2. Node.js 16+
3. Chrome/Chromium browser

## Installation

### Step 1: Clone the repository

```bash
git clone <repository-url>
cd letu-live-tracker
```

### Step 2: Backend Setup

#### Windows
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

#### Linux/Mac
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Frontend Setup

```bash
cd frontend
npm install
```

### Step 4: Google Sheets API Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable Google Sheets API
4. Create credentials (OAuth 2.0 Client ID)
5. Download the credentials JSON file
6. Place it as `backend/credentials.json`

## Running the Application

### Windows

Run the provided batch file:
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

### Linux/Mac

Run the provided shell script:
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
