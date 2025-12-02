"""
Test Google Sheets integration
Run this to verify your credentials are working
"""

import sys
from sheets_handler import GoogleSheetsHandler

def test_sheets(sheet_url):
    """Test Google Sheets handler with a given sheet URL"""
    print(f"\n{'='*60}")
    print(f"Testing Google Sheets Integration")
    print(f"{'='*60}\n")
    
    try:
        # Initialize handler
        print("[1/3] Initializing Google Sheets handler...")
        handler = GoogleSheetsHandler(sheet_url)
        print("✓ Handler initialized successfully")
        print(f"✓ Spreadsheet ID: {handler.spreadsheet_id}")
        
        # Prepare test data
        print("\n[2/3] Preparing test data...")
        test_products = [
            {
                'itemId': '123456789',
                'title': 'Test Product 1',
                'coverImage': 'https://example.com/image1.jpg',
                'minPrice': 10000,
                'maxPrice': 15000,
                'productClicks': 100,
                'ctr': 5.5,
                'ordersCreated': 10,
                'itemsSold': 15,
                'revenue': 150000
            },
            {
                'itemId': '987654321',
                'title': 'Test Product 2',
                'coverImage': 'https://example.com/image2.jpg',
                'minPrice': 20000,
                'maxPrice': 25000,
                'productClicks': 200,
                'ctr': 8.2,
                'ordersCreated': 20,
                'itemsSold': 30,
                'revenue': 600000
            }
        ]
        print(f"✓ Prepared {len(test_products)} test products")
        
        # Update sheet
        print("\n[3/3] Writing to Google Sheet...")
        success = handler.update_products(test_products)
        
        if success:
            print("✓ Data written successfully!")
            print(f"\n{'='*60}")
            print("Test completed successfully!")
            print(f"{'='*60}\n")
            print("Please check your Google Sheet to verify the data.")
            print(f"Sheet URL: {sheet_url}\n")
            return True
        else:
            print("❌ Failed to write data")
            return False
            
    except FileNotFoundError as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease follow these steps:")
        print("  1. Complete the Google Sheets setup (see GOOGLE_SHEETS_SETUP.md)")
        print("  2. Download credentials.json from Google Cloud Console")
        print("  3. Place credentials.json in the backend/ folder")
        return False
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease check:")
        print("  - Your Google Sheet URL is correct")
        print("  - You have edit access to the sheet")
        print("  - credentials.json is properly configured")
        print("  - You've completed the OAuth authentication")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sheet_url = sys.argv[1]
    else:
        print("Please provide your Google Sheet URL")
        print("Example: https://docs.google.com/spreadsheets/d/YOUR_SHEET_ID/edit")
        sheet_url = input("\nEnter Google Sheet URL: ").strip()
    
    if not sheet_url:
        print("Error: Google Sheet URL is required")
        sys.exit(1)
    
    test_sheets(sheet_url)
