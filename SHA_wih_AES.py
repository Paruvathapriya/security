#encrypt only hash
# AES ENCRYPTION WITH SHA-256 HASH

# Import AES cipher
from Crypto.Cipher import AES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib
import hashlib

# Get message
message = input("Enter message: ")

# Set 16-byte key and IV
key = b"1234567890123456"
iv = b"1234567890123456"

# Generate SHA-256 hash
h = hashlib.sha256(message.encode()).hexdigest()
print("Original Hash:", h)

# Encrypt only the hash
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted_hash = cipher.encrypt(pad(h.encode(), 16))
print("Encrypted Hash:", encrypted_hash.hex())

# Decrypt the hash
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_hash = unpad(cipher.decrypt(encrypted_hash), 16).decode()

print("Decrypted Hash:", decrypted_hash)

# Verify hash with original message
new_hash = hashlib.sha256(message.encode()).hexdigest()

if new_hash == decrypted_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
