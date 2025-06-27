from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


SCOPES = ['https://www.googleapis.com/auth/documents']
DOCUMENT_ID = '10uZW0QdZlqzhFXynH2bzFFEq48vF-YhDmRPGTfl6lP8'

def read_document(service):
    try:
        doc = service.documents().get(documentId=DOCUMENT_ID).execute()
        print(f"\nTitle: {doc.get('title')}\n")
        print("Content:\n")

        for element in doc.get('body').get('content', []):
            if 'paragraph' in element:
                for item in element['paragraph']['elements']:
                    text = item.get('textRun')
                    if text:
                        print(text.get('content'), end='')
        print()

    except HttpError as err:
        print(f"Error: {err}")

def write_to_document(service, text):
    try:
        requests = [
            {
                'insertText': {
                    'endOfSegmentLocation': {},
                    'text': text + '\n'
                }
            }
        ]
        service.documents().batchUpdate(documentId=DOCUMENT_ID, body={'requests': requests}).execute()
        print("Text added to the document.")

    except HttpError as err:
        print(f"Error writing to document: {err}")


def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('docs', 'v1', credentials=creds)

    while True:
        choice = input("\nType 1 to read, 2 to write, 0 to exit: ").strip()

        if choice == '1':
            read_document(service)
        elif choice == '2':
            user_text = input("What do you want to write into the document? ")
            write_to_document(service, user_text)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid input. Please type 1, 2, or 0.")

if __name__ == '__main__':
    main()
