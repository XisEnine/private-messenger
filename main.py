from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import warnings

# Suppress LibreSSL warning
warnings.filterwarnings("ignore", category=DeprecationWarning)

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
DOCUMENT_ID = '10uZW0QdZlqzhFXynH2bzFFEq48vF-YhDmRPGTfl6lP8'  # Replace with your doc ID

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token_file:
            token_file.write(creds.to_json())
    try:
        service = build('docs', 'v1', credentials=creds)
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        print(f"Title: {document.get('title')}")
        print("\nContent:\n")

        for element in document.get('body').get('content', []):
            if 'paragraph' in element:
                for elem in element['paragraph']['elements']:
                    text_run = elem.get('textRun')
                    if text_run:
                        print(text_run.get('content'), end='')
    except HttpError as error:
        print(f"An error occurred: {error}")
        print("\nMake sure you've:")
        print("1. Enabled Google Docs API at https://console.developers.google.com/apis/api/docs.googleapis.com")
        print("2. Waited a few minutes after enabling")
        print("3. Used the correct document ID")

if __name__ == '__main__':
    main()