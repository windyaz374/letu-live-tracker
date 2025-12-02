"""
Quick test script to verify the scraper is working
Run this before deploying to production
"""

import sys
from scraper import ShopeeStreamScraper

def test_scraper(session_id):
    """Test the scraper with a given session ID"""
    print(f"\n{'='*60}")
    print(f"Testing Scraper with Session ID: {session_id}")
    print(f"{'='*60}\n")
    
    try:
        # Initialize scraper
        print("[1/3] Initializing scraper...")
        scraper = ShopeeStreamScraper(session_id)
        print("✓ Scraper initialized successfully")
        
        # Scrape products
        print("\n[2/3] Scraping products...")
        products = scraper.scrape_products()
        
        if products:
            print(f"✓ Found {len(products)} products\n")
            
            # Display first 3 products
            print("Sample Products:")
            print("-" * 60)
            for i, product in enumerate(products[:3], 1):
                print(f"\nProduct {i}:")
                print(f"  Title: {product.get('title', 'N/A')}")
                print(f"  Item ID: {product.get('itemId', 'N/A')}")
                print(f"  Clicks: {product.get('productClicks', 0)}")
                print(f"  CTR: {product.get('ctr', 0)}%")
                print(f"  Orders: {product.get('ordersCreated', 0)}")
                print(f"  Revenue: {product.get('revenue', 0)}")
                
            if len(products) > 3:
                print(f"\n... and {len(products) - 3} more products")
        else:
            print("⚠ No products found. Possible reasons:")
            print("  - Invalid session ID")
            print("  - Session has no products")
            print("  - Page structure changed")
            print("  - Network issues")
        
        # Cleanup
        print("\n[3/3] Cleaning up...")
        scraper.close()
        print("✓ Scraper closed successfully")
        
        print(f"\n{'='*60}")
        print("Test completed successfully!")
        print(f"{'='*60}\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\nPlease check:")
        print("  - Chrome browser is installed")
        print("  - Internet connection is working")
        print("  - Session ID is correct")
        return False

if __name__ == '__main__':
    # Default session ID from the image
    default_session_id = '29060044'
    
    if len(sys.argv) > 1:
        session_id = sys.argv[1]
    else:
        session_id = input(f"Enter Session ID (default: {default_session_id}): ").strip()
        if not session_id:
            session_id = default_session_id
    
    test_scraper(session_id)
