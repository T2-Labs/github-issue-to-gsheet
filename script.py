import os
from github import Github
from gspread import service_account

def extract_id(body):
  # Update regular expression to match your ID format
  match = re.search(r"MONDO:(\d+)", body)
  return match.group(1) if match else None

def get_next_available_row(worksheet):
    col = worksheet.col_values(1)  # Assuming you want to find the next empty row in column 1
    return len(col) + 1

def main(username, organization, repo_name, issue_number):
  g = Github(os.environ["GH_TOKEN"])
  repo = g.get_repo(f"{organization}/{repo_name}")
  issue = repo.get_issue(issue_number)

  if issue.author.login != username or not issue.assignee or not issue.assignee.login == username:
    print("You don't have permission to update this issue.")
    return

  id_value = extract_id(issue.body)
  if not id_value:
    print("ID not found in issue body.")
    return

  # Configure Google Sheets API with service account credentials
  gc = service_account.from_json_keyfile_dict(json.loads(os.environ["GOOGLE_SHEETS_CREDENTIALS"]))
  sheet = gc.open("GitHub Action Demo").sheet1

  # Find next available row
  next_row = get_next_available_row(sheet)

  # Update cell value in the next available row
  sheet.update_cell(next_row, 1, id_value)
  print("Successfully added ID to Google Sheet.")

if __name__ == "__main__":
  username = os.environ["ACTOR"]
  organization = "T2-Labs"  # Replace with your organization name
  repo_name = "github-gsheets-demos"  # Replace with your repository name
  issue_number = int(os.environ["ISSUE_NUMBER"])
  main(username, organization, repo_name, issue_number)
