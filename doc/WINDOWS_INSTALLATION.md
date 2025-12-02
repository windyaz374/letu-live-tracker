# Windows Installation Guide

## Prerequisites

Before you begin, make sure you have:

1. **Python 3.8 or higher**
   - Download from: https://www.python.org/downloads/
   - ⚠️ **IMPORTANT**: During installation, check "Add Python to PATH"

2. **Node.js 16 or higher**
   - Download from: https://nodejs.org/
   - Choose the LTS (Long Term Support) version

3. **Google Chrome Browser**
   - Download from: https://www.google.com/chrome/
   - Required for web scraping

## Installation Steps

### Step 1: Download the Project

1. Download the project ZIP file or clone with Git:
   ```cmd
   git clone <repository-url>
   ```

2. Extract to a folder, for example:
   ```
   C:\Users\YourName\letu-live-tracker
   ```

### Step 2: Google Sheets Setup

Follow the instructions in `GOOGLE_SHEETS_SETUP.md` to:
1. Create a Google Cloud project
2. Enable Google Sheets API
3. Download `credentials.json`
4. Place `credentials.json` in the `backend\` folder

### Step 3: Run the Application

1. **Navigate to the project folder**
   - Open File Explorer
   - Go to your project folder
   - Double-click `start.bat`

2. **First-time setup** (automatic):
   - Python virtual environment will be created
   - Dependencies will be installed
   - This may take a few minutes

3. **Application starts**:
   - Two command windows will open (Backend & Frontend)
   - Your default browser will open automatically
   - Go to: http://localhost:5173

### Step 4: First Use

1. **Google Authentication** (first time only):
   - When you click "Start Tracking", a browser will open
   - Sign in to your Google account
   - Allow the requested permissions
   - Authentication token will be saved for future use

2. **Start Tracking**:
   - Enter the Session ID (from the livestream URL)
   - Enter your Google Sheet URL
   - Click "Start Tracking"

## Troubleshooting

### Python not found
**Error**: `'python' is not recognized as an internal or external command`

**Solution**:
1. Reinstall Python from https://www.python.org/downloads/
2. ✅ Check "Add Python to PATH" during installation
3. Restart your computer
4. Open Command Prompt and type: `python --version`

### Node.js not found
**Error**: `'node' is not recognized as an internal or external command`

**Solution**:
1. Install Node.js from https://nodejs.org/
2. Restart your computer
3. Open Command Prompt and type: `node --version`

### Port already in use
**Error**: `Address already in use` or `Port 5000 is already allocated`

**Solution**:
1. Close any applications using ports 5000 or 5173
2. Or kill the process:
   ```cmd
   netstat -ano | findstr :5000
   taskkill /PID <process_id> /F
   ```

### Chrome Driver issues
**Error**: Chrome driver errors

**Solution**:
- Make sure Google Chrome is installed
- The script will automatically download the correct driver
- If issues persist, try updating Chrome to the latest version

### Firewall blocking
**Error**: Windows Firewall blocks the application

**Solution**:
1. When prompted, click "Allow access"
2. Or manually allow Python and Node.js in Windows Firewall:
   - Control Panel → System and Security → Windows Defender Firewall
   - Allow an app through firewall
   - Add Python and Node.js

## Manual Setup (Advanced)

If the automatic `start.bat` doesn't work:

### Backend:
```cmd
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

### Frontend (in a new terminal):
```cmd
cd frontend
npm install
npm run dev
```

## Updating the Application

When a new version is released:

1. Download the latest version
2. Replace all files (keep your `credentials.json` and `token.json`)
3. Run `start.bat` again
4. Dependencies will update automatically if needed

## Stopping the Application

### Easy way:
- Close both command windows (Backend & Frontend)

### Proper way:
- In each command window, press `Ctrl+C`
- Type `Y` when prompted
- Close the windows

## Daily Use

After the first-time setup:

1. Double-click `start.bat`
2. Wait for browser to open
3. Enter Session ID and Google Sheet URL
4. Click "Start Tracking"
5. Your sheet will update every 30 seconds

That's it! 🎉

## Need Help?

If you encounter any issues:
1. Check the error messages in the command windows
2. Review this troubleshooting guide
3. Make sure all prerequisites are installed
4. Check that `credentials.json` is in the `backend\` folder

## Tips for Best Performance

- 💡 Keep the command windows open while tracking
- 💡 Don't close your browser tab while tracking is active
- 💡 Make sure your computer doesn't go to sleep during tracking
- 💡 Check your Google Sheet to verify data is updating
- 💡 Use a dedicated Google Sheet for each session
