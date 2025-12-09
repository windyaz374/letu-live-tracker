from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import threading
import time
import os

from scraper import ShopeeStreamScraper
from sheets_handler import GoogleSheetsHandler

# Configure Flask to serve frontend
app = Flask(__name__, 
            static_folder='../frontend/dist',
            static_url_path='')
CORS(app)

# Store active scrapers
active_scrapers = {}

# ============================================
# FRONTEND ROUTES
# ============================================

@app.route('/')
def serve_frontend():
    """Serve React frontend"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files (JS, CSS, images)"""
    if os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        # For React Router - serve index.html
        return send_from_directory(app.static_folder, 'index.html')

# ============================================
# API ROUTES
# ============================================
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'message': 'Server is running'})

@app.route('/api/start-tracking', methods=['POST'])
def start_tracking():
    """Start tracking a livestream session"""
    try:
        data = request.json
        session_id = data.get('sessionId')
        sheet_url = data.get('sheetUrl')
        
        if not session_id or not sheet_url:
            return jsonify({'error': 'Missing sessionId or sheetUrl'}), 400
        
        # Check if already tracking this session
        if session_id in active_scrapers:
            return jsonify({'error': 'Already tracking this session'}), 400
        
        # Initialize scraper and sheets handler
        scraper = ShopeeStreamScraper(session_id)
        sheets_handler = GoogleSheetsHandler(sheet_url)
        
        # Store the scraper
        active_scrapers[session_id] = {
            'scraper': scraper,
            'sheets_handler': sheets_handler,
            'running': True
        }
        
        # Start scraping in background thread
        def scrape_loop():
            while active_scrapers.get(session_id, {}).get('running', False):
                try:
                    # Scrape products
                    products = scraper.scrape_products()
                    
                    # Update Google Sheets
                    if products:
                        sheets_handler.update_products(products)
                    
                    # Wait before next scrape (30 seconds)
                    time.sleep(30)
                except Exception as e:
                    print(f"Error in scrape loop: {str(e)}")
                    time.sleep(10)
        
        thread = threading.Thread(target=scrape_loop, daemon=True)
        thread.start()
        
        return jsonify({
            'message': 'Tracking started successfully',
            'sessionId': session_id
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/stop-tracking', methods=['POST'])
def stop_tracking():
    """Stop tracking a livestream session"""
    try:
        data = request.json
        session_id = data.get('sessionId')
        
        if not session_id:
            return jsonify({'error': 'Missing sessionId'}), 400
        
        if session_id not in active_scrapers:
            return jsonify({'error': 'Session not being tracked'}), 404
        
        # Stop the scraper
        active_scrapers[session_id]['running'] = False
        active_scrapers[session_id]['scraper'].close()
        del active_scrapers[session_id]
        
        return jsonify({'message': 'Tracking stopped successfully'})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/status/<session_id>', methods=['GET'])
def get_status(session_id):
    """Get tracking status for a session"""
    try:
        if session_id not in active_scrapers:
            return jsonify({'tracking': False})
        
        scraper_data = active_scrapers[session_id]
        
        return jsonify({
            'tracking': True,
            'running': scraper_data['running'],
            'lastUpdate': scraper_data.get('lastUpdate', None)
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/preview/<session_id>', methods=['GET'])
def preview_data(session_id):
    """Preview data for a session without starting tracking"""
    try:
        scraper = ShopeeStreamScraper(session_id)
        products = scraper.scrape_products()
        scraper.close()
        
        return jsonify({
            'products': products,
            'count': len(products) if products else 0
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("=" * 50)
    print("Letu Live Tracker Backend Starting...")
    print("=" * 50)
    print(f"Server running at: http://localhost:5000")
    print(f"API Endpoints:")
    print(f"  - GET  /api/health")
    print(f"  - POST /api/start-tracking")
    print(f"  - POST /api/stop-tracking")
    print(f"  - GET  /api/status/<session_id>")
    print(f"  - GET  /api/preview/<session_id>")
    print("=" * 50)
    app.run(debug=True, host='0.0.0.0', port=5000)
