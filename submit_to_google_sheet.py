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

# Get the issue body from environment variable
issue_body = os.getenv('ISSUE_BODY')

# # Append the issue body to the Google Sheet
# sheet.append_row([issue_body])


# TODO: Parse values from ISSUE_BODY to use for column values
# Split the issue body by lines
lines = issue_body.split('\n')

# Initialize variables to store extracted values
term_to_obsolete = None
obsoleteion_reason = None

# Iterate over each line to find the relevant information
for line in lines:
    if line.startswith("### What term do you want to request obsoleting?"):
        term_to_obsolete = line.split("### What term do you want to request obsoleting?")[-1].strip()
    elif line.startswith("### Obsoleteion reason"):
        obsoleteion_reason = line.split("### Obsoleteion reason")[-1].strip()

# Output the extracted values
print("** Term to obsolete:", term_to_obsolete)
print("** Obsoleteion reason:", obsoleteion_reason)



# TODO: Validate values from ISSUE_BODY, e.g. Mondo ID, and fail Action if invalid



# Define row data for different columns
column1_data = term_to_obsolete
column2_data = 'Value2'
column3_data = obsoleteion_reason

# Append row data into different columns
row_data = [column1_data, column2_data, column3_data]

# Append the issue to the Google Sheet
sheet.append_row(row_data)
