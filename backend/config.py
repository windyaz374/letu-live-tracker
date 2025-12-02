"""
Configuration file for the application
Modify these values to customize behavior
"""

# Scraping Configuration
SCRAPE_INTERVAL = 30  # seconds between each scrape
HEADLESS_MODE = True  # Run browser in headless mode (no visible window)
BROWSER_TIMEOUT = 30  # seconds to wait for page load

# Server Configuration
FLASK_HOST = '0.0.0.0'  # Listen on all interfaces
FLASK_PORT = 5000
FLASK_DEBUG = True  # Enable debug mode for development

# Frontend Configuration
FRONTEND_URL = 'http://localhost:5173'

# Google Sheets Configuration
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'
SHEETS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Shopee URLs
SHOPEE_DASHBOARD_URL = 'https://svcs-admin.shopee.vn/dashboard/stream'

# Logging Configuration
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Data Fields to Extract
# Add or remove fields based on what's available in the API
PRODUCT_FIELDS = [
    'itemId',
    'title',
    'coverImage',
    'minPrice',
    'maxPrice',
    'productClicks',
    'ctr',
    'ordersCreated',
    'itemsSold',
    'revenue'
]

# Rate Limiting (to avoid overwhelming the target server)
MAX_CONCURRENT_SESSIONS = 5  # Maximum number of sessions to track simultaneously
REQUEST_DELAY = 1  # seconds between requests (if making multiple)

# Retry Configuration
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds

# Chrome Options
CHROME_OPTIONS = [
    '--headless',
    '--no-sandbox',
    '--disable-dev-shm-usage',
    '--disable-gpu',
    '--window-size=1920,1080',
    '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
]
