import { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:5000/api';

function App() {
  const [sessionId, setSessionId] = useState('');
  const [sheetUrl, setSheetUrl] = useState('');
  const [isTracking, setIsTracking] = useState(false);
  const [error, setError] = useState('');
  const [success, setSuccess] = useState('');
  const [previewData, setPreviewData] = useState(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleStartTracking = async () => {
    setError('');
    setSuccess('');
    
    if (!sessionId || !sheetUrl) {
      setError('Please fill in all fields');
      return;
    }

    setIsLoading(true);
    try {
      const response = await axios.post(`${API_BASE_URL}/start-tracking`, {
        sessionId,
        sheetUrl
      });
      
      setSuccess('Tracking started! Data will be updated every 30 seconds.');
      setIsTracking(true);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to start tracking');
    } finally {
      setIsLoading(false);
    }
  };

  const handleStopTracking = async () => {
    setIsLoading(true);
    try {
      await axios.post(`${API_BASE_URL}/stop-tracking`, { sessionId });
      setSuccess('Tracking stopped');
      setIsTracking(false);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to stop tracking');
    } finally {
      setIsLoading(false);
    }
  };

  const handlePreview = async () => {
    setError('');
    setPreviewData(null);
    
    if (!sessionId) {
      setError('Please enter a session ID');
      return;
    }

    setIsLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/preview/${sessionId}`);
      setPreviewData(response.data);
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to preview data');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="container">
        <div className="header">
          <h1>📊 Letu Live Tracker</h1>
          <p className="subtitle">Real-time Shopee Livestream Product Data Tracker</p>
        </div>

        <div className="card">
          <div className="form-group">
            <label htmlFor="sessionId">Session ID</label>
            <input
              id="sessionId"
              type="text"
              value={sessionId}
              onChange={(e) => setSessionId(e.target.value)}
              placeholder="e.g., 29060044"
              disabled={isTracking}
              className="input"
            />
            <p className="hint">Find this in the URL: ?sessionId=XXXXX</p>
          </div>

          <div className="form-group">
            <label htmlFor="sheetUrl">Google Sheet URL</label>
            <input
              id="sheetUrl"
              type="text"
              value={sheetUrl}
              onChange={(e) => setSheetUrl(e.target.value)}
              placeholder="https://docs.google.com/spreadsheets/d/..."
              disabled={isTracking}
              className="input"
            />
            <p className="hint">Make sure you have edit access to this sheet</p>
          </div>

          {error && (
            <div className="alert alert-error">
              ⚠️ {error}
            </div>
          )}

          {success && (
            <div className="alert alert-success">
              ✅ {success}
            </div>
          )}

          <div className="button-group">
            {!isTracking ? (
              <>
                <button
                  onClick={handleStartTracking}
                  disabled={isLoading}
                  className="btn btn-primary"
                >
                  {isLoading ? '⏳ Starting...' : '▶️ Start Tracking'}
                </button>
                <button
                  onClick={handlePreview}
                  disabled={isLoading}
                  className="btn btn-secondary"
                >
                  {isLoading ? '⏳ Loading...' : '👁️ Preview Data'}
                </button>
              </>
            ) : (
              <button
                onClick={handleStopTracking}
                disabled={isLoading}
                className="btn btn-danger"
              >
                {isLoading ? '⏳ Stopping...' : '⏹️ Stop Tracking'}
              </button>
            )}
          </div>

          {isTracking && (
            <div className="tracking-status">
              <div className="pulse"></div>
              <span>Tracking active - Updating every 30 seconds</span>
            </div>
          )}
        </div>

        {previewData && (
          <div className="card preview-card">
            <h2>Preview Data ({previewData.count} products found)</h2>
            <div className="preview-list">
              {previewData.products.slice(0, 5).map((product, index) => (
                <div key={index} className="preview-item">
                  <div className="preview-title">{product.title || 'N/A'}</div>
                  <div className="preview-stats">
                    <span>Clicks: {product.productClicks || 0}</span>
                    <span>Orders: {product.ordersCreated || 0}</span>
                    <span>Revenue: {product.revenue || 0}</span>
                  </div>
                </div>
              ))}
            </div>
            {previewData.count > 5 && (
              <p className="preview-more">...and {previewData.count - 5} more products</p>
            )}
          </div>
        )}

        <div className="info-card">
          <h3>ℹ️ How to use:</h3>
          <ol>
            <li>Get the Session ID from the livestream URL</li>
            <li>Create a Google Sheet and paste its URL</li>
            <li>Click "Preview Data" to test the connection</li>
            <li>Click "Start Tracking" to begin real-time updates</li>
            <li>Your Google Sheet will update automatically every 30 seconds</li>
          </ol>
        </div>

        <footer className="footer">
          <p>Made with ❤️ for livestream tracking</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
