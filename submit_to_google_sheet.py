import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Set up the Google Sheets API credentials
scope = ['https://www.googleapis.com/auth/spreadsheets']
creds_json = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
print(creds_json)
#creds_dict = eval(creds_json)  # Convert JSON string to dictionary
creds_dict = json.loads(creds_json)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

# Authenticate with the Google Sheets API
client = gspread.authorize(creds)

# Open the Google Sheet by its ID
sheet_id = '1s-GTbL1GmHqeLm5gnWKUJEz5wmNSLzELB0fcZAS3RZo'
sheet = client.open_by_key(sheet_id).sheet1

# Get the issue body from environment variable
issue_body = os.getenv('ISSUE_BODY')

# Append the issue body to the Google Sheet
sheet.append_row([issue_body])
