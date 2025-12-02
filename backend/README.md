# Backend - Letu Live Tracker

Python Flask backend for scraping Shopee livestream data and updating Google Sheets.

## 🐍 Features

- RESTful API with Flask
- Selenium web scraping
- Google Sheets integration
- Background threading
- Automatic ChromeDriver management
- OAuth 2.0 authentication

## 🛠️ Technology Stack

- **Python 3.8+**
- **Flask 3.0** - Web framework
- **Selenium 4.15** - Web automation
- **Google APIs** - Sheets integration
- **ChromeDriver** - Browser automation

## 📦 Installation

```bash
# Create virtual environment
python3 -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Running

```bash
# Make sure venv is activated
python app.py
```

Server runs on `http://localhost:5000`

## 📂 Structure

```
backend/
├── app.py                    # Flask server
├── scraper.py               # Web scraping
├── sheets_handler.py        # Google Sheets
├── config.py                # Configuration
├── requirements.txt         # Dependencies
├── test_scraper.py         # Test scraper
├── test_sheets.py          # Test sheets
├── .env.template           # Environment template
└── credentials.json        # Google credentials (gitignored)
```

## 🔧 Configuration

### Environment Variables

Copy `.env.template` to `.env`:

```bash
cp .env.template .env
```

Edit as needed:
```env
FLASK_ENV=development
FLASK_DEBUG=True
PORT=5000
SCRAPE_INTERVAL=30
```

### config.py

Main configuration file:
- Scraping settings
- Chrome options
- API endpoints
- Timeouts

## 📡 API Endpoints

### Health Check
```
GET /api/health
Response: { "status": "ok", "message": "Server is running" }
```

### Start Tracking
```
POST /api/start-tracking
Body: { "sessionId": "29060044", "sheetUrl": "https://..." }
Response: { "message": "Tracking started successfully", "sessionId": "..." }
```

### Stop Tracking
```
POST /api/stop-tracking
Body: { "sessionId": "29060044" }
Response: { "message": "Tracking stopped successfully" }
```

### Get Status
```
GET /api/status/<sessionId>
Response: { "tracking": true, "running": true, "lastUpdate": "..." }
```

### Preview Data
```
GET /api/preview/<sessionId>
Response: { "products": [...], "count": 5 }
```

## 🕷️ Web Scraping

### scraper.py

Uses Selenium to:
1. Navigate to Shopee dashboard
2. Intercept network logs
3. Extract product JSON
4. Parse data

#### Methods

- `scrape_products()` - Main scraping function
- `_extract_from_network_logs()` - Primary method
- `_extract_from_dom()` - Fallback method

### Data Extracted

```python
{
    'itemId': '2925423187',
    'title': 'Product name',
    'coverImage': 'https://...',
    'minPrice': 455400,
    'maxPrice': 455400,
    'productClicks': 49,
    'ctr': 0.8,
    'ordersCreated': 11,
    'itemsSold': 11,
    'revenue': 455400
}
```

## 📊 Google Sheets

### sheets_handler.py

Manages Google Sheets:
1. OAuth authentication
2. Spreadsheet updates
3. Header formatting
4. Data validation

#### Methods

- `update_products()` - Update sheet with data
- `_write_headers()` - Create formatted headers
- `_authenticate()` - OAuth flow

### Setup

1. Create Google Cloud project
2. Enable Sheets API
3. Create OAuth credentials
4. Download as `credentials.json`
5. Place in `backend/` folder

See [GOOGLE_SHEETS_SETUP.md](../GOOGLE_SHEETS_SETUP.md)

## 🧪 Testing

### Test Scraper

```bash
python test_scraper.py 29060044
```

### Test Google Sheets

```bash
python test_sheets.py "https://docs.google.com/spreadsheets/d/.../edit"
```

## 🔄 Background Processing

Uses Python threading:
- Non-blocking scraping
- 30-second intervals
- Automatic error recovery
- Clean shutdown

## 🐛 Error Handling

All endpoints have try-catch blocks:
- Return appropriate HTTP codes
- Log errors to console
- Provide user-friendly messages

## 🔒 Security

- OAuth 2.0 for Google API
- Credentials stored locally
- Token auto-refresh
- CORS enabled for frontend
- No external data storage

## 📝 Dependencies

```txt
flask==3.0.0              # Web framework
flask-cors==4.0.0         # CORS support
selenium==4.15.2          # Web automation
webdriver-manager==4.0.1  # ChromeDriver
google-auth==2.25.2       # Google auth
google-api-python-client  # Sheets API
```

## 🚀 Production Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Using Docker

```dockerfile
FROM python:3.9-slim
# Install Chrome
RUN apt-get update && apt-get install -y chromium chromium-driver
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

## 🔧 Troubleshooting

### Chrome Driver Issues
- Install Chrome browser
- Delete cached driver
- Restart application

### Import Errors
```bash
pip install -r requirements.txt
```

### Google Sheets Permission
- Delete `token.json`
- Restart app
- Re-authenticate

## 📈 Performance

- Scraping: 5-10 seconds
- Updates: Every 30 seconds
- Memory: ~200-500 MB
- CPU: 5-15%

## 🔗 Related Documentation

- [Main README](../README.md)
- [Development Guide](../DEVELOPMENT.md)
- [Google Sheets Setup](../GOOGLE_SHEETS_SETUP.md)

---

**Built with Python + Flask for reliability** 🐍
