# Google Docs API Reader & Writer

## 📄 Project Overview

A Python script that connects to the **Google Docs API** to **read from and write to** a specified Google Document using OAuth 2.0 authentication.

## 🚀 Features

* ✅ Authenticates securely using OAuth 2.0
* 📖 Reads and displays document metadata (title) and content
* ✍️ Allows you to append custom text at the end of the document
* 🔄 Interactive CLI to choose between reading, writing, or exiting
* ⚠️ Handles and explains common authentication and API errors

## 🗂️ File Structure

```
.
├── main.py                 # Main script with read/write logic
├── credentials.json        # OAuth 2.0 client credentials
├── token.json              # Generated user access token
├── README.md               # Project documentation
├── pyproject.toml          # Python project config (optional)
└── uv.lock                 # Dependency lock file (optional)
```

## ⚙️ Setup Instructions

### 1. Prerequisites

* Python 3.7 or higher
* A Google Cloud project with the **Docs API enabled**
* OAuth 2.0 credentials (`credentials.json`)
* OAuth consent screen configured for your account

### 2. Install Required Libraries

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 3. Configuration

* Place your `credentials.json` file in the project folder
* Update the `DOCUMENT_ID` variable with your Google Doc ID

---

## 🧪 Usage

```bash
python main.py
```

* Type `1` to **read** the document
* Type `2` to **append text** to the end
* Type `0` to **exit**

---

## 🛠 Error Handling

Covers and explains:

* Token/authentication issues
* Invalid document IDs
* Missing or unenabled APIs
* Permission or sharing restrictions

---

## 🔐 Security Notes

* Keep `credentials.json` safe and **never commit it to version control**
* `token.json` contains user-specific tokens; treat it as sensitive data

