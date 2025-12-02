# Frontend - Letu Live Tracker

React-based frontend for the Letu Live Tracker application.

## 🎨 Features

- Modern, responsive UI with gradient design
- Real-time status updates
- Preview functionality
- Error handling and user feedback
- Beautiful animations and transitions

## 🛠️ Technology Stack

- **React 18** - UI framework
- **Vite 5** - Build tool and dev server
- **Axios** - HTTP client
- **Modern CSS** - Styling with flexbox and animations

## 📦 Installation

```bash
npm install
```

## 🚀 Development

```bash
# Start dev server (hot reload enabled)
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📂 Structure

```
frontend/
├── src/
│   ├── App.jsx         # Main component
│   ├── App.css         # Component styles
│   ├── main.jsx        # Entry point
│   └── index.css       # Global styles
├── index.html          # HTML template
├── package.json        # Dependencies
└── vite.config.js     # Vite configuration
```

## 🔧 Configuration

### API Base URL

The frontend connects to the backend API at `http://localhost:5000`. This is configured in:
- `App.jsx` - API_BASE_URL constant
- `vite.config.js` - Proxy configuration

### Port

The dev server runs on port **5173** by default. Change in `vite.config.js`:

```javascript
export default defineConfig({
  server: {
    port: 5173  // Change this
  }
})
```

## 🎨 Styling

The application uses custom CSS with:
- Gradient backgrounds
- Smooth transitions
- Responsive design
- Pulse animations
- Modern button styles

### Colors

Primary colors defined in CSS:
- Purple gradient: `#667eea` to `#764ba2`
- Success: `#22c55e`
- Error: `#f5576c`

## 📡 API Integration

The frontend communicates with the backend via REST API:

### Endpoints Used

```javascript
// Health check
GET /api/health

// Start tracking
POST /api/start-tracking
Body: { sessionId, sheetUrl }

// Stop tracking
POST /api/stop-tracking
Body: { sessionId }

// Get status
GET /api/status/:sessionId

// Preview data
GET /api/preview/:sessionId
```

## 🧩 Components

### App Component

Main component with state management:

```javascript
const [sessionId, setSessionId] = useState('')
const [sheetUrl, setSheetUrl] = useState('')
const [isTracking, setIsTracking] = useState(false)
const [error, setError] = useState('')
const [success, setSuccess] = useState('')
const [previewData, setPreviewData] = useState(null)
const [isLoading, setIsLoading] = useState(false)
```

### Key Functions

- `handleStartTracking()` - Start session tracking
- `handleStopTracking()` - Stop tracking
- `handlePreview()` - Preview session data

## 🎯 User Flow

1. User enters Session ID
2. User enters Google Sheet URL
3. (Optional) Click "Preview Data" to test
4. Click "Start Tracking"
5. Application shows tracking status
6. Data updates in Google Sheet every 30s
7. Click "Stop Tracking" when done

## 📱 Responsive Design

The UI is mobile-friendly with breakpoints:

```css
@media (max-width: 600px) {
  /* Mobile styles */
}
```

## 🐛 Error Handling

Errors are displayed with:
- Red alert boxes
- Clear error messages
- User-friendly language

Success messages use:
- Green alert boxes
- Confirmation text
- Status indicators

## 🔄 State Management

Simple React hooks-based state:
- No external state management library
- Local component state
- Prop drilling avoided (single component)

## 🚀 Building for Production

```bash
npm run build
```

Outputs to `dist/` folder:
- Minified JavaScript
- Optimized CSS
- Compressed assets

## 📝 Environment Variables

None required! API URL is hardcoded for local development.

For production, you might want to add `.env`:

```env
VITE_API_URL=https://your-api-url.com
```

Then use in code:
```javascript
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000';
```

## 🎨 Customization

### Change Colors

Edit `App.css`:
```css
.header {
  background: linear-gradient(135deg, #your-color 0%, #another-color 100%);
}
```

### Change Animations

Edit pulse animation in `App.css`:
```css
@keyframes pulse {
  /* Customize animation */
}
```

## 🧪 Testing

Manual testing recommended:
1. Test all input fields
2. Test error states
3. Test success states
4. Test loading states
5. Test responsive design

## 📊 Performance

- Initial load: ~100KB (gzipped)
- Hot reload: <1s
- Build time: ~5s

## 🔗 Related Documentation

- [Main README](../README.md)
- [Development Guide](../DEVELOPMENT.md)
- [Architecture](../ARCHITECTURE.md)

## 💡 Tips

- Use React DevTools for debugging
- Check browser console for errors
- Use Network tab to debug API calls
- Hot reload works automatically

---

**Built with React + Vite for optimal DX** ⚡
