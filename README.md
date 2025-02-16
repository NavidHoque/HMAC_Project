# HMAC Secure Messaging Project

## Overview
This project demonstrates a simple **HMAC (Hash-based Message Authentication Code)** authentication system between two applications. One application (**Sender**) sends a JSON-formatted message along with an HMAC signature, while the other application (**Receiver**) verifies the integrity and authenticity of the message.

## How It Works
1. The Sender creates a JSON payload with a message.
2. The Sender computes an **HMAC signature** for the message using a secret key.
3. The message is **Base64-encoded** and stored in a file along with the HMAC signature.
4. The **Receiver** reads the encoded message and signature from the file.
5. The Receiver decodes the message, recalculates the HMAC, and verifies if it matches the received signature.
6. If the HMAC matches, the message is authenticated and displayed.

## Project Files
- `sender.py` – Sends a message with an HMAC signature.
- `receiver.py` – Receives and verifies the message.
- `message.txt` – Stores the encoded message and HMAC signature.
- `secret_key.txt` – Contains the secret key shared between both applications.

## Installation & Setup
1. Ensure you have **Python 3.x** installed.
2. Create a new directory and navigate to it.
3. Create the required files: `sender.py`, `receiver.py`, and `secret_key.txt`.
4. Add a **secret key** in `secret_key.txt`. The same key must be used by both applications.

## Usage Instructions
### **Run the sender application**
- This will generate a **Base64-encoded message** and its **HMAC signature**.
- The data will be saved in `message.txt`.

```sh
python sender.py

