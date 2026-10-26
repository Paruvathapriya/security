#encrypt both hash and msg
# DES ENCRYPTION WITH MD5 HASH VERIFICATION

# Import DES cipher
from Crypto.Cipher import DES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib for MD5
import hashlib

# Get message from user
message = input("Enter message: ")

# Set secret key and initialization vector
key = b"12345678"
iv = b"12345678"

# Generate hash
h = hashlib.md5(message.encode()).hexdigest()
print("MD5 Hash:", h)

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

# Display decrypted message and received hash
print("Decrypted Message:", msg)
print("Received Hash:", received_hash)

# Verify hash
new_hash = hashlib.md5(msg.encode()).hexdigest()

# Compare calculated hash with received hash
if new_hash == received_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
