import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ShopeeStreamScraper:
    """Scraper for Shopee livestream product data"""
    
    def __init__(self, session_id):
        self.session_id = session_id
        self.url = f"https://svcs-admin.shopee.vn/dashboard/stream?sessionId={session_id}"
        self.driver = None
        self._setup_driver()
    
    def _setup_driver(self):
        """Setup Chrome WebDriver with headless options"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
        
        # Install and setup ChromeDriver automatically
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
    
    def scrape_products(self):
        """
        Scrape product data from the livestream session
        Returns list of product dictionaries
        """
        try:
            # Navigate to the page
            self.driver.get(self.url)
            
            # Wait for the page to load
            time.sleep(3)
            
            # Method 1: Try to intercept network requests for productList API
            products = self._extract_from_network_logs()
            
            if not products:
                # Method 2: Fallback to DOM parsing
                products = self._extract_from_dom()
            
            return products
            
        except Exception as e:
            print(f"Error scraping products: {str(e)}")
            return []
    
    def _extract_from_network_logs(self):
        """Extract product data from network logs (XHR requests)"""
        try:
            # Enable Performance Logging
            self.driver.execute_cdp_cmd('Network.enable', {})
            
            # Get network logs
            logs = self.driver.get_log('performance')
            
            products = []
            for entry in logs:
                try:
                    log = json.loads(entry['message'])['message']
                    
                    # Look for productList API response
                    if 'Network.responseReceived' in log['method']:
                        response_url = log['params'].get('response', {}).get('url', '')
                        
                        if 'productList' in response_url and 'sessionId' in response_url:
                            # Get the response body
                            request_id = log['params']['requestId']
                            response = self.driver.execute_cdp_cmd(
                                'Network.getResponseBody', 
                                {'requestId': request_id}
                            )
                            
                            body = json.loads(response['body'])
                            
                            # Extract product list from response
                            if 'data' in body and 'list' in body['data']:
                                for product in body['data']['list']:
                                    products.append({
                                        'itemId': product.get('itemId'),
                                        'title': product.get('title'),
                                        'coverImage': product.get('coverImage'),
                                        'maxPrice': product.get('maxPrice', 0),
                                        'minPrice': product.get('minPrice', 0),
                                        'productClicks': product.get('productClicks', 0),
                                        'ctr': product.get('ctr', 0),
                                        'ordersCreated': product.get('ordersCreated', 0),
                                        'revenue': product.get('revenue', 0),
                                        'itemsSold': product.get('itemsSold', 0)
                                    })
                            break
                            
                except Exception as e:
                    continue
            
            return products
            
        except Exception as e:
            print(f"Error extracting from network logs: {str(e)}")
            return []
    
    def _extract_from_dom(self):
        """Fallback method: Extract product data from DOM elements"""
        try:
            products = []
            
            # Wait for product list to load
            wait = WebDriverWait(self.driver, 10)
            
            # This is a fallback - you'll need to adjust selectors based on actual DOM
            # Look for product rows in the table
            product_rows = self.driver.find_elements(By.CSS_SELECTOR, 'tr')
            
            for row in product_rows:
                try:
                    # Extract data from table cells
                    cells = row.find_elements(By.TAG_NAME, 'td')
                    
                    if len(cells) >= 6:
                        product = {
                            'title': cells[0].text,
                            'productClicks': self._parse_number(cells[1].text),
                            'ctr': self._parse_percentage(cells[2].text),
                            'ordersCreated': self._parse_number(cells[3].text),
                            'itemsSold': self._parse_number(cells[4].text),
                        }
                        products.append(product)
                        
                except Exception as e:
                    continue
            
            return products
            
        except Exception as e:
            print(f"Error extracting from DOM: {str(e)}")
            return []
    
    def _parse_number(self, text):
        """Parse number from text, removing commas and special characters"""
        try:
            return int(text.replace(',', '').replace('.', ''))
        except:
            return 0
    
    def _parse_percentage(self, text):
        """Parse percentage from text"""
        try:
            return float(text.replace('%', ''))
        except:
            return 0.0
    
    def close(self):
        """Close the WebDriver"""
        if self.driver:
            self.driver.quit()
    
    def __del__(self):
        """Cleanup on deletion"""
        self.close()
