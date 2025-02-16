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

# Read message and HMAC from file
with open("message.txt", "r") as file:
    lines = file.readlines()
    encoded_message = lines[0].strip()
    received_hmac = lines[1].strip()

# Print received encoded message, HMAC signature, and secret key
print("Received Encoded Message (Base64):", encoded_message)
print("Received HMAC Signature:", received_hmac)
print("Secret Key Used for Verification:", secret_key)

# Decode the Base64-encoded message
decoded_message = base64.b64decode(encoded_message).decode()

# Compute expected HMAC
expected_hmac = compute_hmac(decoded_message, secret_key)

# Verify HMAC
if hmac.compare_digest(received_hmac, expected_hmac):
    print("HMAC verified! Message is authentic.")
    print("Decoded Message:", json.loads(decoded_message)["message"])
else:
    print("HMAC verification failed! Message may be tampered with.")
