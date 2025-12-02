# Development Guide

## Project Structure

```
letu-live-tracker/
├── backend/                    # Python Flask backend
│   ├── app.py                 # Main Flask application
│   ├── scraper.py             # Selenium-based web scraper
│   ├── sheets_handler.py      # Google Sheets API integration
│   ├── requirements.txt       # Python dependencies
│   ├── .env.template         # Environment variables template
│   ├── credentials.json      # Google API credentials (gitignored)
│   └── token.json            # OAuth token (gitignored)
│
├── frontend/                  # React frontend
│   ├── src/
│   │   ├── App.jsx           # Main React component
│   │   ├── App.css           # Styling
│   │   ├── main.jsx          # Entry point
│   │   └── index.css         # Global styles
│   ├── index.html            # HTML template
│   ├── package.json          # Node.js dependencies
│   └── vite.config.js        # Vite configuration
│
├── start.bat                  # Windows startup script
├── start.sh                   # Linux/Mac startup script
├── README.md                  # Main documentation
├── WINDOWS_INSTALLATION.md    # Windows user guide
├── GOOGLE_SHEETS_SETUP.md     # Google Sheets setup guide
└── .gitignore                # Git ignore rules
```

## Backend Architecture

### Flask API Endpoints

- `GET /api/health` - Health check
- `POST /api/start-tracking` - Start tracking a session
- `POST /api/stop-tracking` - Stop tracking a session
- `GET /api/status/<session_id>` - Get tracking status
- `GET /api/preview/<session_id>` - Preview data without tracking

### Scraping Strategy

The scraper uses two methods to extract data:

1. **Network Logs (Primary)**: Intercepts XHR requests to capture API responses
2. **DOM Parsing (Fallback)**: Parses HTML table elements if network method fails

### Data Flow

```
User Input → Flask API → Selenium Scraper → Network Intercept/DOM Parse
                                                    ↓
                                            Product Data
                                                    ↓
                                        Google Sheets API
                                                    ↓
                                        Update Spreadsheet
```

## Frontend Architecture

### Component Structure

- **App.jsx**: Main component with state management
  - Session ID input
  - Google Sheet URL input
  - Start/Stop tracking buttons
  - Preview functionality
  - Status display

### State Management

Uses React hooks for simple state management:
- `sessionId`: Current session being tracked
- `sheetUrl`: Target Google Sheet URL
- `isTracking`: Tracking status
- `previewData`: Preview results
- `error/success`: User feedback

## Key Technologies

### Backend
- **Flask**: Web framework
- **Selenium**: Browser automation for scraping
- **Google Sheets API**: Data export
- **Flask-CORS**: Cross-origin requests
- **webdriver-manager**: Automatic ChromeDriver management

### Frontend
- **React 18**: UI framework
- **Vite**: Build tool and dev server
- **Axios**: HTTP client
- **Modern CSS**: Gradient backgrounds, animations

## Development Setup

### Backend Development

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt
python app.py
```

### Frontend Development

```bash
cd frontend
npm install
npm run dev
```

### Hot Reload

- Backend: Flask debug mode enables auto-reload
- Frontend: Vite provides instant HMR (Hot Module Replacement)

## Adding Features

### Adding New Data Fields

1. **Update scraper.py**:
   ```python
   product = {
       'itemId': product.get('itemId'),
       'newField': product.get('newField'),  # Add here
       # ...
   }
   ```

2. **Update sheets_handler.py**:
   ```python
   headers = [
       'Item ID',
       'New Field',  # Add here
       # ...
   ]
   
   row = [
       str(product.get('itemId', '')),
       product.get('newField', ''),  # Add here
       # ...
   ]
   ```

3. **Update frontend** (if showing in UI):
   ```jsx
   <span>New Field: {product.newField || 0}</span>
   ```

### Changing Scrape Interval

In `app.py`, modify:
```python
time.sleep(30)  # Change this value (seconds)
```

### Adding New Endpoints

1. Add route in `app.py`:
   ```python
   @app.route('/api/my-endpoint', methods=['GET'])
   def my_endpoint():
       # Your logic here
       return jsonify({'data': 'value'})
   ```

2. Call from frontend:
   ```javascript
   const response = await axios.get(`${API_BASE_URL}/my-endpoint`);
   ```

## Testing

### Manual Testing

1. **Backend API**:
   ```bash
   curl http://localhost:5000/api/health
   ```

2. **Scraper**:
   ```python
   from scraper import ShopeeStreamScraper
   scraper = ShopeeStreamScraper('29060044')
   products = scraper.scrape_products()
   print(products)
   scraper.close()
   ```

3. **Google Sheets**:
   ```python
   from sheets_handler import GoogleSheetsHandler
   handler = GoogleSheetsHandler('your-sheet-url')
   handler.update_products([{'itemId': '123', 'title': 'Test'}])
   ```

### Debug Mode

Backend debugging:
```python
# app.py - already enabled
app.run(debug=True)
```

Frontend debugging:
- Use React DevTools browser extension
- Check browser console for errors
- Network tab for API calls

## Common Issues During Development

### CORS Errors
- Ensure Flask-CORS is configured
- Check `CORS(app)` in app.py
- Verify frontend proxy in vite.config.js

### Selenium Issues
- Install Chrome/Chromium browser
- Check ChromeDriver version compatibility
- Use headless mode for servers without display

### Google Sheets API
- Verify credentials.json is present
- Check OAuth scopes
- Delete token.json to re-authenticate

## Performance Optimization

### Backend
- Use connection pooling for database (if added)
- Cache frequently accessed data
- Implement rate limiting for API

### Frontend
- Use React.memo for expensive components
- Implement virtual scrolling for large lists
- Debounce user inputs

### Scraping
- Minimize page loads
- Reuse browser sessions
- Implement exponential backoff for retries

## Security Considerations

1. **API Security**:
   - Add authentication (JWT, API keys)
   - Implement rate limiting
   - Validate all inputs

2. **Credentials**:
   - Never commit credentials.json or token.json
   - Use environment variables for sensitive data
   - Implement proper access controls

3. **Scraping Ethics**:
   - Respect robots.txt
   - Implement reasonable delays
   - Don't overload target servers

## Deployment

### Docker (Recommended for Production)

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

# Install Chrome
RUN apt-get update && apt-get install -y chromium chromium-driver

# Copy backend
WORKDIR /app/backend
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .

# Copy frontend build
COPY frontend/dist /app/frontend/dist

EXPOSE 5000
CMD ["python", "app.py"]
```

### Cloud Platforms
- **Heroku**: Use Procfile and buildpacks
- **AWS**: EC2 or ECS with Docker
- **Google Cloud**: Cloud Run for containerized apps
- **DigitalOcean**: App Platform or Droplets

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Roadmap

Potential future features:
- [ ] Multiple session tracking
- [ ] Historical data visualization
- [ ] Email/Slack notifications
- [ ] Export to CSV/Excel
- [ ] Scheduled tracking (cron jobs)
- [ ] User authentication
- [ ] Dashboard with analytics
- [ ] Mobile responsive design
- [ ] Dark mode
- [ ] Multi-language support
