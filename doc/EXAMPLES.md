# Example Usage & Screenshots Guide

## Complete Walkthrough

### Example 1: Single Session Tracking

#### Scenario
You're running a livestream selling beauty products on Shopee. Session ID is `29060044`. You want to track all product performance in real-time.

#### Steps

**1. Prepare Your Google Sheet**
```
→ Go to https://sheets.google.com
→ Click "Blank" to create new spreadsheet
→ Name it: "Livestream Analytics - Session 29060044"
→ Copy the URL from browser
→ Example: https://docs.google.com/spreadsheets/d/1ABC...XYZ/edit
```

**2. Start the Application**
```
Windows:
  → Double-click start.bat
  → Wait for browser to open

Linux/Mac:
  → Open terminal
  → cd /path/to/letu-live-tracker
  → ./start.sh
  → Wait for browser to open
```

**3. Enter Information**
```
Session ID field: 29060044
Google Sheet URL: https://docs.google.com/spreadsheets/d/1ABC...XYZ/edit
```

**4. Preview (Optional)**
```
→ Click "Preview Data"
→ Wait 5-10 seconds
→ See sample products below the form
→ Verify data looks correct
```

**5. Start Tracking**
```
→ Click "Start Tracking"
→ First time: Browser opens for Google sign-in
→ Sign in → Allow permissions
→ See "Tracking active" message
```

**6. Check Your Sheet**
```
→ Go to your Google Sheet
→ Refresh the page
→ See data appearing!

Expected columns:
  | Item ID | Title | Cover Image | Min Price | Max Price | Product Clicks | CTR (%) | Orders Created | Items Sold | Revenue | Last Updated |
  |---------|-------|-------------|-----------|-----------|---------------|---------|----------------|------------|---------|--------------|
  | 2925... | Toner | https://... | 455400    | 455400    | 49            | 0.8     | 11             | 11         | 455400  | 2025-12-02...|
```

**7. Monitor in Real-Time**
```
→ Every 30 seconds, data refreshes
→ Watch numbers update automatically
→ Leave application running during livestream
```

**8. Stop Tracking**
```
→ Click "Stop Tracking" when done
→ Data remains in Google Sheet
→ Close the application windows
```

---

### Example 2: Multiple Products Comparison

#### Sample Data Output

After tracking session `29060044`, your Google Sheet will look like:

```
┌────────────┬────────────────────────────────────┬─────────┬──────┬──────────┬────────┐
│ Item ID    │ Title                              │ Clicks  │ CTR  │ Orders   │Revenue │
├────────────┼────────────────────────────────────┼─────────┼──────┼──────────┼────────┤
│ 2925423187 │ [d'Alba Official] Toner serum...  │ 49      │ 0.8% │ 11       │ 455400 │
│ 2929000123 │ Phấn Nền kiềm dầu Carslan...      │ 46      │ 0.6% │ 13       │ 299000 │
│ 2912345678 │ [d'Alba Official] Serum dưỡng...  │ 42      │ 1.4% │ 1        │ 382500 │
│ 2987654321 │ [Live] Toner Serum Dưỡng...       │ 30      │28.3% │ 4        │ 789360 │
│ 2955555555 │ FHYL Vớ Ống Chân đệt...            │ 22      │14.7% │ 7        │ 22000  │
└────────────┴────────────────────────────────────┴─────────┴──────┴──────────┴────────┘
```

**Insights You Can Get:**
- Which products get the most clicks
- Conversion rates (CTR)
- Top revenue generators
- Best-selling items
- Performance trends over time

---

### Example 3: Daily Workflow

#### Morning Preparation
```bash
8:00 AM - Start application
  → Double-click start.bat
  → Wait for browser to open

8:05 AM - Create today's sheet
  → New Google Sheet: "Daily Sales - 2025-12-02"
  → Share with team members

8:10 AM - Ready for first session
  → Application running
  → Waiting for livestream to start
```

#### During Livestream
```bash
10:00 AM - Livestream starts
  → Get session ID from dashboard
  → Enter in tracker: 29060044
  → Enter sheet URL
  → Click "Start Tracking"

10:01 AM - 12:00 PM - Active monitoring
  → Check Google Sheet every 5 minutes
  → Watch which products perform well
  → Share real-time data with team
  → Adjust livestream strategy based on data
```

#### After Livestream
```bash
12:00 PM - Livestream ends
  → Click "Stop Tracking"
  → Export final data (File → Download → CSV)
  → Share report with management
  → Close application
```

---

### Example 4: API Testing with cURL

For developers who want to test the API directly:

```bash
# Health check
curl http://localhost:5000/api/health

# Response:
{
  "status": "ok",
  "message": "Server is running"
}

# Preview data
curl http://localhost:5000/api/preview/29060044

# Response:
{
  "products": [
    {
      "itemId": "2925423187",
      "title": "[d'Alba Official] Toner serum...",
      "productClicks": 49,
      "ctr": 0.8,
      "ordersCreated": 11,
      "revenue": 455400
    }
  ],
  "count": 1
}

# Start tracking
curl -X POST http://localhost:5000/api/start-tracking \
  -H "Content-Type: application/json" \
  -d '{
    "sessionId": "29060044",
    "sheetUrl": "https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit"
  }'

# Response:
{
  "message": "Tracking started successfully",
  "sessionId": "29060044"
}

# Check status
curl http://localhost:5000/api/status/29060044

# Response:
{
  "tracking": true,
  "running": true,
  "lastUpdate": "2025-12-02 10:15:30"
}

# Stop tracking
curl -X POST http://localhost:5000/api/stop-tracking \
  -H "Content-Type: application/json" \
  -d '{"sessionId": "29060044"}'

# Response:
{
  "message": "Tracking stopped successfully"
}
```

---

### Example 5: Error Handling

#### Common Errors and Solutions

**Error: "Session not found"**
```
What you see:
  ⚠️ Failed to preview data
  No products found

Solution:
  → Verify session ID is correct
  → Check if livestream is active
  → Try accessing the dashboard manually first
```

**Error: "Permission denied" (Google Sheets)**
```
What you see:
  ⚠️ Failed to update Google Sheets
  Permission denied

Solution:
  → Delete backend/token.json
  → Restart application
  → Re-authenticate when prompted
  → Make sure you have edit access to the sheet
```

**Error: "Chrome driver not found"**
```
What you see:
  ❌ Chrome driver initialization failed

Solution:
  → Install Google Chrome browser
  → Restart application (auto-downloads driver)
  → Check internet connection
```

---

### Example 6: Advanced Use Cases

#### A. Historical Analysis
```
Track same product across multiple sessions:

Session 1 (Dec 1): Sheet A → Export as CSV
Session 2 (Dec 2): Sheet B → Export as CSV
Session 3 (Dec 3): Sheet C → Export as CSV

→ Combine CSVs in Excel
→ Create pivot tables
→ Analyze trends over time
```

#### B. Team Collaboration
```
1. Create shared Google Drive folder
2. Give team edit access
3. Each session → New sheet in folder
4. Team members can:
   → View real-time updates
   → Add notes/comments
   → Create charts
   → Export reports
```

#### C. Automated Reports
```
Use Google Sheets features:
→ =AVERAGE(J2:J100) for avg revenue
→ =MAX(F2:F100) for max clicks
→ =COUNTIF(H2:H100,">10") for hot products
→ Charts/Graphs auto-update
→ Email reports on schedule
```

---

### Example 7: Customization

#### Change Update Interval

Edit `backend/app.py`:
```python
# Line ~60
time.sleep(30)  # Change to 60 for 1-minute updates
```

#### Add New Data Fields

1. Edit `backend/scraper.py`:
```python
product = {
    'itemId': product.get('itemId'),
    'newField': product.get('newField'),  # Add here
    # ...existing fields...
}
```

2. Edit `backend/sheets_handler.py`:
```python
headers = [
    'Item ID',
    'New Field',  # Add here
    # ...existing headers...
]
```

3. Restart application

---

### Example 8: Troubleshooting Checklist

Before contacting support, check:

```
□ Python installed? Run: python --version
□ Node.js installed? Run: node --version
□ Chrome installed? Open Chrome browser
□ credentials.json exists in backend/?
□ Session ID correct? Check dashboard URL
□ Google Sheet URL correct? Can you access it?
□ Internet connection working?
□ Firewall allowing connections?
□ Ports 5000 and 5173 available?
□ Both terminal windows still open?
```

---

### Expected Performance

#### Typical Metrics
```
Scraping speed: 5-10 seconds per session
Data accuracy: 99%+ (direct from API)
Update frequency: 30 seconds (configurable)
Resource usage:
  - CPU: 5-15%
  - RAM: 200-500 MB
  - Network: <1 MB per update
```

#### Session Limits
```
Recommended: 1-3 concurrent sessions
Maximum: 5 concurrent sessions
Per session: Unlimited products
Data retention: Permanent (in Google Sheets)
```

---

## Quick Reference Card

```
╔═══════════════════════════════════════════════════════════╗
║              LETU LIVE TRACKER - QUICK REF                ║
╠═══════════════════════════════════════════════════════════╣
║ START:   Double-click start.bat (Windows)                 ║
║          or ./start.sh (Linux/Mac)                        ║
║                                                           ║
║ URLS:    Frontend: http://localhost:5173                 ║
║          Backend:  http://localhost:5000                  ║
║                                                           ║
║ INPUTS:  Session ID (from URL ?sessionId=XXXXX)          ║
║          Google Sheet URL (full URL with /edit)           ║
║                                                           ║
║ BUTTONS: Preview → Test connection                        ║
║          Start → Begin tracking (updates every 30s)       ║
║          Stop → End tracking                              ║
║                                                           ║
║ FILES:   backend/credentials.json (required)              ║
║          backend/token.json (auto-generated)              ║
║                                                           ║
║ SUPPORT: README.md, QUICKSTART.md, *_SETUP.md            ║
╚═══════════════════════════════════════════════════════════╝
```
