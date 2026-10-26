#encrpyt msg and hash

# DES ENCRYPTION WITH SHA-1 HASH VERIFICATION

# Import DES cipher
from Crypto.Cipher import DES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib
import hashlib

# Get message
message = input("Enter message: ")

# Set 8-byte key and IV
key = b"12345678"
iv = b"12345678"

# Generate SHA-1 hash
h = hashlib.sha1(message.encode()).hexdigest()
print("Original Hash:", h)

# Attach hash to message
data = message + "|" + h

# Encrypt message and hash together
cipher = DES.new(key, DES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(data.encode(), 8))
print("Encrypted:", encrypted.hex())

# Decrypt
cipher = DES.new(key, DES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 8).decode()

# Separate message and hash
msg, received_hash = decrypted.rsplit("|", 1)

print("Decrypted Message:", msg)
print("Received Hash:", received_hash)

# Verify hash
new_hash = hashlib.sha1(msg.encode()).hexdigest()

if new_hash == received_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
