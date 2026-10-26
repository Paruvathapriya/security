#encrypt both message and hash

# AES ENCRYPTION WITH SHA-256 HASH VERIFICATION

# Import AES cipher
from Crypto.Cipher import AES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib for SHA-256
import hashlib

# Get message from user
message = input("Enter message: ")

# Set 16-byte secret key and initialization vector
key = b"1234567890123456"
iv = b"1234567890123456"

# Generate SHA-256 hash
h = hashlib.sha256(message.encode()).hexdigest()

# Display original hash
print("Original Hash:", h)

# Attach hash to message
data = message + "|" + h

# Encrypt
# Create AES cipher in CBC mode
cipher = AES.new(key, AES.MODE_CBC, iv)

# Pad and encrypt message with hash
encrypted = cipher.encrypt(pad(data.encode(), 16))

# Display encrypted text
print("Encrypted:", encrypted.hex())

# Decrypt
# Create AES cipher for decryption
cipher = AES.new(key, AES.MODE_CBC, iv)

# Decrypt and remove padding
decrypted = unpad(cipher.decrypt(encrypted), 16).decode()

# Separate message and received hash
msg, received_hash = decrypted.rsplit("|", 1)

# Display decrypted message and hash
print("Decrypted Message:", msg)
print("Received Hash:", received_hash)

# Verify
# Generate SHA-256 hash of decrypted message
new_hash = hashlib.sha256(msg.encode()).hexdigest()

# Compare calculated hash with received hash
if new_hash == received_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
