import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

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

# # Get the issue body from environment variable
# issue_body = os.getenv('ISSUE_BODY')

# # Append the issue body to the Google Sheet
# sheet.append_row([issue_body])


# TODO: Parse values from ISSUE_BODY to use for column values 


# Define row data for different columns
column1_data = 'Value1'
column2_data = 'Value2'
column3_data = 'Value3'

# Append row data into different columns
row_data = [column1_data, column2_data, column3_data]

# Append the issue to the Google Sheet
sheet.append_row(row_data)
