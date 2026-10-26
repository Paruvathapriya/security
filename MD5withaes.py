
# AES ENCRYPTION WITH MD5 HASH VERIFICATION

# Import AES cipher
from Crypto.Cipher import AES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib for MD5
import hashlib

# Get message from user
message = input("Enter message: ")

# Set 16-byte secret key and initialization vector
key = b"1234567890123456"
iv = b"1234567890123456"

# Generate hash
h = hashlib.md5(message.encode()).hexdigest()
print("Original Hash:", h)

# Attach hash to message
data = message + "|" + h

# Encrypt message and hash using AES-CBC
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(data.encode(), 16))
print("Encrypted:", encrypted.hex())

# Decrypt encrypted data
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 16).decode()

# Separate message and received hash
msg, received_hash = decrypted.rsplit("|", 1)

# Display decrypted message and hash
print("Decrypted Message:", msg)
print("Received Hash:", received_hash)

# Verify
new_hash = hashlib.md5(msg.encode()).hexdigest()

# Compare original and received hashes
if new_hash == received_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
