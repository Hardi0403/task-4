import random
import string
import hashlib

def generate_otp():
    """Generates a 6-digit OTP with 2 uppercase letters and 2 special characters."""
    characters = string.ascii_uppercase + string.digits + '!@#$%^&*()'
    otp = ''.join(random.choice(characters) for _ in range(6))
    return otp

def hash_otp(otp):
    """Hashes the OTP using SHA-256."""
    hash_object = hashlib.sha256(otp.encode('utf-8'))
    hashed_otp = hash_object.hexdigest()
    return hashed_otp

# Example usage:
otp = generate_otp()
hashed_otp = hash_otp(otp)

print("Generated OTP:", otp)
print("Hashed OTP:", hashed_otp)