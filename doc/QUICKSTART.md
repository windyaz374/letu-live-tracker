# Quick Start Guide

Get up and running in 5 minutes!

## For Windows Users

### 1️⃣ Install Prerequisites (One-time setup)

Download and install:
- **Python**: https://www.python.org/downloads/ ✅ Check "Add to PATH"
- **Node.js**: https://nodejs.org/ (LTS version)
- **Chrome**: https://www.google.com/chrome/

### 2️⃣ Setup Google Sheets (One-time setup)

1. Go to https://console.cloud.google.com/
2. Create new project → Enable Google Sheets API
3. Create OAuth credentials (Desktop app)
4. Download as `credentials.json`
5. Place in `backend/` folder

📖 Detailed instructions: [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)

### 3️⃣ Run the Application

Double-click: `start.bat`

That's it! 🎉

---

## For Linux/Mac Users

### 1️⃣ Install Prerequisites

```bash
# Python 3.8+
python3 --version

# Node.js 16+
node --version

# Chrome/Chromium browser
google-chrome --version
```

### 2️⃣ Setup Google Sheets

Same as Windows (see step 2 above)

### 3️⃣ Run the Application

```bash
chmod +x start.sh
./start.sh
```

---

## First Use

1. **Browser opens** → http://localhost:5173

2. **Enter Session ID**:
   - Find in URL: `?sessionId=29060044`
   - Example: `29060044`

3. **Enter Google Sheet URL**:
   - Create new sheet at https://sheets.google.com
   - Copy the URL
   - Example: `https://docs.google.com/spreadsheets/d/abc123.../edit`

4. **Click "Preview Data"** (optional):
   - Test the connection
   - See what data will be scraped

5. **Click "Start Tracking"**:
   - First time: Browser opens for Google login
   - Allow permissions
   - Data updates every 30 seconds ✨

---

## Testing Before First Use

### Test the scraper:
```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
python test_scraper.py 29060044
```

### Test Google Sheets:
```bash
python test_sheets.py "YOUR_SHEET_URL"
```

---

## Common First-Time Issues

### ❌ "Python not found"
→ Reinstall Python, check "Add to PATH"

### ❌ "credentials.json not found"
→ Complete Google Sheets setup (step 2)

### ❌ Browser doesn't open
→ Manually visit http://localhost:5173

### ❌ "Permission denied" on Linux
→ Run: `chmod +x start.sh`

---

## What Happens When You Run start.bat/start.sh?

1. ✅ Checks Python & Node.js installed
2. 📦 Creates virtual environment (first time)
3. 📥 Installs dependencies (first time)
4. 🚀 Starts backend server (port 5000)
5. 🎨 Starts frontend server (port 5173)
6. 🌐 Opens browser automatically

---

## Daily Usage (After Setup)

1. Double-click `start.bat` (or run `./start.sh`)
2. Enter Session ID + Sheet URL
3. Click "Start Tracking"
4. ✅ Done! Check your Google Sheet

---

## Stopping the Application

**Windows**: Close the two command windows

**Linux/Mac**: Press `Ctrl+C` in both terminals

---

## File Checklist

Before running for the first time:

- [ ] `backend/credentials.json` exists
- [ ] Python installed (check with `python --version`)
- [ ] Node.js installed (check with `node --version`)
- [ ] Chrome browser installed

---

## Next Steps

- 📖 Read [README.md](README.md) for full documentation
- 🪟 Windows users: See [WINDOWS_INSTALLATION.md](WINDOWS_INSTALLATION.md)
- 🔧 Developers: See [DEVELOPMENT.md](DEVELOPMENT.md)
- 📊 Google Sheets: See [GOOGLE_SHEETS_SETUP.md](GOOGLE_SHEETS_SETUP.md)

---

## Support

Having issues? Check:
1. Error messages in the command windows
2. Browser console (F12)
3. Troubleshooting guides in the docs above

---

**🎉 Enjoy tracking your livestream data!**
