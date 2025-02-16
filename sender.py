import hmac
import hashlib
import base64
import json


def compute_hmac(message: str, secret_key: str) -> str:
    """Computes the HMAC for a given message.

    Uses SHA-256 and encodes the digest in Base64.

    Args:
        message (str): The message to compute the HMAC for.
        secret_key (str): The secret key used for HMAC computation.

    Returns:
        str: The computed HMAC encoded in Base64.
    """
    hmac_object = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256)
    return base64.b64encode(hmac_object.digest()).decode()


# Load secret key from file
with open("secret_key.txt", "r") as file:
    secret_key = file.read().strip()

# Simple JSON payload with just a message
payload = {
    "message": "Testing123"
}

# Convert payload to JSON format
message_json = json.dumps(payload, sort_keys=True)

# Encode the JSON message in Base64
encoded_message = base64.b64encode(message_json.encode()).decode()

# Compute HMAC for the original JSON message (not the Base64 version)
hmac_signature = compute_hmac(message_json, secret_key)

# Save message and HMAC to a file (simulating sending data)
with open("message.txt", "w") as file:
    file.write(encoded_message + "\n" + hmac_signature)

# Print the encoded message for debugging or transmission
print(payload)
print("Encoded Message (Base64):", encoded_message)
print("HMAC Signature:", hmac_signature)
print("Message and HMAC saved. Ready to be sent to receiver.")
