import re
import os.path
from datetime import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class GoogleSheetsHandler:
    """Handler for Google Sheets API operations"""
    
    def __init__(self, sheet_url):
        self.sheet_url = sheet_url
        self.spreadsheet_id = self._extract_spreadsheet_id(sheet_url)
        self.service = None
        self._authenticate()
    
    def _extract_spreadsheet_id(self, url):
        """Extract spreadsheet ID from Google Sheets URL"""
        # Pattern: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit...
        match = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url)
        if match:
            return match.group(1)
        raise ValueError("Invalid Google Sheets URL")
    
    def _authenticate(self):
        """Authenticate with Google Sheets API"""
        creds = None
        
        # The file token.json stores the user's access and refresh tokens
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
        # If there are no (valid) credentials available, let the user log in
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists('credentials.json'):
                    raise FileNotFoundError(
                        "credentials.json not found. Please download it from Google Cloud Console."
                    )
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES
                )
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        
        self.service = build('sheets', 'v4', credentials=creds)
    
    def update_products(self, products):
        """
        Update product data in Google Sheets
        Creates headers if they don't exist
        """
        try:
            # Prepare headers
            headers = [
                'Item ID',
                'Title',
                'Cover Image',
                'Min Price',
                'Max Price',
                'Product Clicks',
                'CTR (%)',
                'Orders Created',
                'Items Sold',
                'Revenue',
                'Last Updated'
            ]
            
            # Check if sheet has headers
            result = self.service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range='A1:K1'
            ).execute()
            
            values = result.get('values', [])
            
            # If no headers, add them
            if not values:
                self._write_headers(headers)
            
            # Prepare product data rows
            rows = []
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            for product in products:
                row = [
                    str(product.get('itemId', '')),
                    product.get('title', ''),
                    product.get('coverImage', ''),
                    product.get('minPrice', 0),
                    product.get('maxPrice', 0),
                    product.get('productClicks', 0),
                    product.get('ctr', 0),
                    product.get('ordersCreated', 0),
                    product.get('itemsSold', 0),
                    product.get('revenue', 0),
                    timestamp
                ]
                rows.append(row)
            
            # Clear existing data (except headers)
            self.service.spreadsheets().values().clear(
                spreadsheetId=self.spreadsheet_id,
                range='A2:K'
            ).execute()
            
            # Write new data
            if rows:
                body = {'values': rows}
                self.service.spreadsheets().values().update(
                    spreadsheetId=self.spreadsheet_id,
                    range='A2',
                    valueInputOption='RAW',
                    body=body
                ).execute()
            
            print(f"Updated {len(rows)} products in Google Sheets")
            return True
            
        except HttpError as error:
            print(f"An error occurred: {error}")
            return False
    
    def _write_headers(self, headers):
        """Write headers to the first row"""
        body = {'values': [headers]}
        self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheet_id,
            range='A1',
            valueInputOption='RAW',
            body=body
        ).execute()
        
        # Format headers (bold, background color)
        requests = [{
            'repeatCell': {
                'range': {
                    'sheetId': 0,
                    'startRowIndex': 0,
                    'endRowIndex': 1
                },
                'cell': {
                    'userEnteredFormat': {
                        'backgroundColor': {
                            'red': 0.2,
                            'green': 0.6,
                            'blue': 0.9
                        },
                        'textFormat': {
                            'bold': True,
                            'foregroundColor': {
                                'red': 1.0,
                                'green': 1.0,
                                'blue': 1.0
                            }
                        }
                    }
                },
                'fields': 'userEnteredFormat(backgroundColor,textFormat)'
            }
        }]
        
        body = {'requests': requests}
        self.service.spreadsheets().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body=body
        ).execute()
