# github-issue-to-gsheet

## Project Set-up 
1. Create a requirements.txt file with:
```
PyGithub
gspread
```

Run `pip install -r requirements.txt`


2. Create a GitHub Action Workflow. See `issue_template_to_sheet.yml` file in this repo under `.github/workflows`.


3. Create a GitHub Personal Access Token to use with the Python script that will be used for the GitHub Action. Follow these steps:
- Go to your GitHub profile settings at https://github.com/settings/tokens.
- Click "Generate new token."
- Give the token a descriptive name and select the "repo" scope (or the minimum scope your workflow needs).
- This is accessed as `${{ secrets.GH_TOKEN }}` in the `issue_template_to_sheet.yml` file.
**Never commit this token to your repository or share it publicly.**

4. Create a Service Account Key file to use for credentials for Google Sheets. Follow these steps:
- Go to the Google Cloud Platform console (https://console.cloud.google.com/: https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the Google Sheets API for your project.
- Go to "IAM & Admin" -> "Service Accounts".
- Click "Create Service Account" and choose a relevant name.
- Grant the service account "Editor" or "Viewer" access to your desired Google Sheet (depending on your needs).
- For the Service Account, click on Keys and then Add Key to create a new key. The key will automatically be downloaded to your local computer.
- Download the JSON key file for the service account. Never share or commit this file publicly.

Store the base64-encoded JSON key file content as a secret named GOOGLE_SHEETS_CREDENTIALS in your GitHub repository's secret settings. This involves encoding the file's content before storing it.

- Use a base64 encoder online or with a command-line tool to encode the downloaded key file content.
	- For example, using `pybase64` run: `pybase64 encode your_credentials_file.json > base64-output.json`
- Go to your GitHub repository's "Settings" -> "Actions" -> "Secrets".
- Click "New repository secret."
- Add a secret name (e.g., GOOGLE_SHEETS_CREDENTIALS) and paste the encoded key file content into the value field.
- Access the secret in your workflow script (`issue_template_to_sheet.yml`) file using `${{secrets.GOOGLE_SHEETS_CREDENTIALS}}`.

5. Update other placeholders in `script.py`.
Replace placeholders like Your_Spreadsheet_Name, organization, and repository name with your actual values.
Securely store tokens and credentials as environment variables in your GitHub repository.
Adjust the regular expression in extract_id to match your specific ID format.
Adapt the column index (1) in sheet.update_cell based on your sheet structure.


## Resources
- GitHub Actions https://docs.github.com/en/actions/quickstart



