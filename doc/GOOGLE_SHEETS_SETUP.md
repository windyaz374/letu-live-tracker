# Letu Live Tracker - Google Sheets Setup Guide

## Step-by-Step Instructions

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Click "Select a project" → "New Project"
3. Enter project name: "Letu Live Tracker"
4. Click "Create"

### 2. Enable Google Sheets API

1. In the Google Cloud Console, go to "APIs & Services" → "Library"
2. Search for "Google Sheets API"
3. Click on it and press "Enable"

### 3. Create Credentials

1. Go to "APIs & Services" → "Credentials"
2. Click "+ CREATE CREDENTIALS" → "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - User Type: External
   - App name: Letu Live Tracker
   - User support email: (your email)
   - Developer contact: (your email)
   - Click "Save and Continue"
   - Scopes: Skip this step
   - Test users: Add your email
   - Click "Save and Continue"

4. Create OAuth Client ID:
   - Application type: "Desktop app"
   - Name: "Letu Live Tracker Desktop"
   - Click "Create"

5. Download the credentials:
   - Click the download button (⬇️) next to your newly created OAuth client
   - Save the file as `credentials.json`
   - Move it to the `backend/` folder

### 4. First-Time Authentication

The first time you run the application and try to update Google Sheets:

1. A browser window will open automatically
2. Sign in with your Google account
3. Click "Advanced" → "Go to Letu Live Tracker (unsafe)"
4. Click "Allow" to grant permissions
5. The authentication token will be saved as `token.json`

### 5. Create Your Google Sheet

1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new blank spreadsheet
3. Give it a name (e.g., "Livestream Data - Session 29060044")
4. Copy the URL from the browser
5. Use this URL in the application

### 6. Share Permissions (Optional)

If you want others to view the data:
1. Click "Share" in the top-right corner
2. Add email addresses or get a shareable link
3. Set permissions (Viewer/Editor)

## Troubleshooting

### "credentials.json not found"
- Make sure you downloaded the credentials file from Google Cloud Console
- Place it in the `backend/` folder
- File name must be exactly `credentials.json`

### "Permission denied" error
- Delete `backend/token.json`
- Restart the application
- Re-authenticate when prompted

### "Insufficient permissions"
- Go to Google Cloud Console
- Check that Google Sheets API is enabled
- Verify OAuth consent screen is properly configured

### "Invalid grant" error
- Your refresh token may have expired
- Delete `backend/token.json`
- Restart and re-authenticate

## Security Notes

⚠️ **Important:**
- Never commit `credentials.json` or `token.json` to Git
- These files are in `.gitignore` by default
- Keep these files secure and private
- If compromised, delete and regenerate credentials in Google Cloud Console

## Additional Resources

- [Google Sheets API Documentation](https://developers.google.com/sheets/api)
- [OAuth 2.0 for Desktop Apps](https://developers.google.com/identity/protocols/oauth2/native-app)
