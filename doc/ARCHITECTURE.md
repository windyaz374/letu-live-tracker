# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         End User (Windows)                       │
│                                                                  │
│  1. Opens browser → http://localhost:5173                       │
│  2. Enters Session ID + Google Sheet URL                        │
│  3. Clicks "Start Tracking"                                     │
└──────────────────────────┬───────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                    Frontend (React + Vite)                       │
│                      Port: 5173                                  │
│                                                                  │
│  • Beautiful UI with forms and status display                   │
│  • Real-time updates                                            │
│  • Preview functionality                                        │
│  • Error handling & user feedback                               │
└──────────────────────────┬───────────────────────────────────────┘
                          │ HTTP/REST API
                          ▼
┌─────────────────────────────────────────────────────────────────┐
│                     Backend (Python Flask)                       │
│                        Port: 5000                                │
│                                                                  │
│  API Endpoints:                                                 │
│  • POST /api/start-tracking                                     │
│  • POST /api/stop-tracking                                      │
│  • GET  /api/status/<sessionId>                                 │
│  • GET  /api/preview/<sessionId>                                │
│                                                                  │
│  Background Tasks:                                              │
│  • Threading for concurrent scraping                            │
│  • 30-second intervals                                          │
└──────┬──────────────────────────────────────┬───────────────────┘
       │                                      │
       ▼                                      ▼
┌──────────────────────┐          ┌──────────────────────────────┐
│  Selenium WebDriver  │          │  Google Sheets API Handler    │
│                      │          │                              │
│  • ChromeDriver      │          │  • OAuth 2.0 Authentication  │
│  • Headless Chrome   │          │  • Spreadsheet Updates       │
│  • Network logging   │          │  • Formatted Headers         │
│  • DOM parsing       │          │  • Timestamp tracking        │
└──────┬───────────────┘          └──────────┬───────────────────┘
       │                                      │
       ▼                                      ▼
┌──────────────────────┐          ┌──────────────────────────────┐
│  Shopee Dashboard    │          │     Google Sheets            │
│                      │          │                              │
│  URL:                │          │  User's spreadsheet with:    │
│  svcs-admin.shopee   │          │  • Product data              │
│  .vn/dashboard/      │          │  • Real-time updates         │
│  stream?sessionId=X  │          │  • Formatted columns         │
│                      │          │  • Timestamps                │
│  Returns:            │          └──────────────────────────────┘
│  • Product List JSON │
│  • Via XHR/API       │
└──────────────────────┘
```

## Data Flow

```
1. USER INPUT
   ┌─────────────┐
   │ Session ID  │
   │ Sheet URL   │
   └──────┬──────┘
          │
          ▼
2. FRONTEND SENDS REQUEST
   POST /api/start-tracking
   {
     sessionId: "29060044",
     sheetUrl: "https://docs.google.com/..."
   }
          │
          ▼
3. BACKEND INITIALIZES
   ┌──────────────────┐
   │ • Creates scraper│
   │ • Creates sheets │
   │   handler        │
   │ • Starts thread  │
   └────────┬─────────┘
            │
            ▼
4. SCRAPING LOOP (Every 30s)
   ┌─────────────────────────────────┐
   │                                 │
   │  Selenium → Shopee Dashboard   │
   │           ↓                     │
   │  Intercept Network Logs        │
   │           ↓                     │
   │  Extract Product JSON          │
   │           ↓                     │
   │  Parse Product Data            │
   │                                 │
   └────────┬────────────────────────┘
            │
            ▼
5. DATA PROCESSING
   Product List:
   [
     {
       itemId: "2925423187",
       title: "[d'Alba Official] Toner serum...",
       productClicks: 49,
       ctr: 0.8,
       ordersCreated: 11,
       revenue: 455400,
       ...
     },
     ...
   ]
            │
            ▼
6. GOOGLE SHEETS UPDATE
   ┌────────────────────────────┐
   │ • Format headers (if new) │
   │ • Clear old data          │
   │ • Write new rows          │
   │ • Add timestamp           │
   └────────┬───────────────────┘
            │
            ▼
7. REPEAT
   Wait 30 seconds → Go to step 4
```

## Technology Stack

### Frontend
```
React 18
  ├── Vite (Build Tool)
  ├── Axios (HTTP Client)
  └── Modern CSS
      ├── Flexbox
      ├── CSS Animations
      └── Gradient Backgrounds
```

### Backend
```
Python 3.8+
  ├── Flask (Web Framework)
  │   └── Flask-CORS (Cross-Origin)
  ├── Selenium (Web Scraping)
  │   ├── ChromeDriver
  │   └── webdriver-manager
  ├── Google APIs
  │   ├── google-auth
  │   ├── google-auth-oauthlib
  │   └── google-api-python-client
  └── Threading (Background Tasks)
```

## Key Features

### 1. Intelligent Scraping
- **Primary Method**: Network log interception
  - Captures XHR/Fetch API responses
  - Gets raw JSON data directly
  - More reliable and faster

- **Fallback Method**: DOM parsing
  - Parses HTML table structure
  - Used if network method fails
  - Ensures data extraction

### 2. Real-Time Updates
- Background threading
- Non-blocking operations
- 30-second refresh interval
- Automatic retry on failure

### 3. Google Sheets Integration
- OAuth 2.0 authentication
- Automatic header formatting
- Cell formatting (colors, bold)
- Timestamp tracking
- Data validation

### 4. User-Friendly Interface
- Single-click startup
- Beautiful gradient UI
- Real-time status indicators
- Error handling with clear messages
- Preview before tracking

### 5. Cross-Platform Support
- Developed on Linux
- Runs on Windows (primary target)
- Also supports macOS
- Automatic ChromeDriver management

## Security & Privacy

```
┌─────────────────────────────┐
│ credentials.json (Local)    │  ← Never committed to Git
│ • Contains OAuth secrets    │  ← In .gitignore
│ • Required for first auth   │  ← User downloads from GCP
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│ First-time OAuth Flow       │
│ • User signs in via browser │
│ • Grants permissions        │
│ • Receives access token     │
└─────────────────────────────┘
              │
              ▼
┌─────────────────────────────┐
│ token.json (Local)          │  ← Auto-generated
│ • Stores access/refresh     │  ← In .gitignore
│ • Auto-refreshes            │  ← No re-auth needed
│ • Expires periodically      │  ← Delete to re-auth
└─────────────────────────────┘
```

## Scaling Considerations

### Current Design
- Single instance
- In-memory session storage
- Suitable for personal use
- 5-10 concurrent sessions max

### Future Scalability
```
Could be enhanced with:
  ├── Database (PostgreSQL/MongoDB)
  │   └── Persistent session storage
  ├── Redis
  │   └── Caching & session management
  ├── Message Queue (Celery)
  │   └── Distributed scraping tasks
  ├── Load Balancer
  │   └── Multiple backend instances
  └── Docker + Kubernetes
      └── Container orchestration
```

## Error Handling

```
┌─────────────────┐
│   API Request   │
└────────┬────────┘
         │
         ▼
    ┌────────┐
    │ Valid? │──No──→ 400 Bad Request
    └───┬────┘
        │ Yes
        ▼
┌──────────────────┐
│  Try Scraping    │
└────────┬─────────┘
         │
         ├──Success──→ Return Data
         │
         └──Fail──→ Retry 3x
                      │
                      ├──Success──→ Return Data
                      │
                      └──Fail──→ 500 Server Error
                                  └─→ Log Error
                                      └─→ Notify User
```

## Deployment Options

### Option 1: Local (Current)
```
User's Computer
  ├── start.bat (Windows)
  └── start.sh (Linux/Mac)
```

### Option 2: Docker
```
Docker Container
  ├── Backend (Port 5000)
  └── Frontend (Port 5173)
```

### Option 3: Cloud
```
Cloud Platform
  ├── Backend API (Cloud Run/Heroku)
  ├── Frontend (Vercel/Netlify)
  └── Scheduled Jobs (Cloud Scheduler)
```

## Monitoring & Logging

### Current
- Console logs
- Flask debug output
- Browser console (frontend)

### Recommended for Production
- Structured logging (JSON)
- Error tracking (Sentry)
- Performance monitoring
- Analytics dashboard
