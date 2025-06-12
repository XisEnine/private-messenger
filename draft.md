
# Google Docs API Reader

## Project Overview
A Python script that connects to the Google Docs API to fetch and display the content of a specified Google Document.

## Features
- Authenticates with Google's OAuth 2.0
- Reads document metadata (title)
- Extracts and displays document content
- Handles authentication tokens securely
- Provides clear error messages for common issues

## File Structure
```
.
├── main.py                 # Main script
├── credentials.json        # Google API credentials
├── token.json              # Generated auth token
├── README.md               # Project documentation
├── pyproject.toml          # Python project config
└── uv.lock                 # Dependency lock file
```

## Code Implementation

```python
"""
Google Docs API Reader
Authenticates and retrieves content from a specified Google Doc.
"""

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import warnings

# Suppress LibreSSL warning
warnings.filterwarnings("ignore", category=DeprecationWarning)

# API Configuration
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
DOCUMENT_ID = '10uZW0QdZlqzhFXynH2bzFFEq48vF-YhDmRPGTfl6lP8'  # Replace with your doc ID

def authenticate_user():
    """Handles OAuth 2.0 authentication flow"""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    return creds

def fetch_document_content(service):
    """Retrieves and displays document content"""
    document = service.documents().get(documentId=DOCUMENT_ID).execute()
    
    print(f"Title: {document.get('title')}")
    print("\nContent:\n")
    
    for element in document.get('body').get('content', []):
        if 'paragraph' in element:
            for elem in element['paragraph']['elements']:
                text_run = elem.get('textRun')
                if text_run:
                    print(text_run.get('content'), end='')

def main():
    try:
        creds = authenticate_user()
        service = build('docs', 'v1', credentials=creds)
        fetch_document_content(service)
        
    except HttpError as error:
        print(f"An error occurred: {error}")
        print("\nTroubleshooting:")
        print("1. Enable Google Docs API at https://console.developers.google.com/apis/api/docs.googleapis.com")
        print("2. Wait a few minutes after enabling")
        print("3. Verify the document ID is correct")

if __name__ == '__main__':
    main()
```

## Setup Instructions

1. **Prerequisites**
   - Python 3.7+
   - Google Cloud Project with Docs API enabled
   - OAuth consent screen configured

2. **Installation**
   ```bash
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

3. **Configuration**
   - Place your `credentials.json` file in the project root
   - Update `DOCUMENT_ID` with your target document ID

## Usage
```bash
python main.py
```

## Error Handling
The script provides clear troubleshooting guidance for:
- API not enabled
- Invalid document ID
- Authentication failures
- Permission issues

## Security Notes
- `credentials.json` should be kept confidential
- `token.json` is automatically generated but contains sensitive data
