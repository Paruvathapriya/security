#encrypt only the hash

# DES ENCRYPTION WITH MD5 HASH

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

# Generate MD5 hash
h = hashlib.md5(message.encode()).hexdigest()
print("Original Hash:", h)

# Encrypt only the hash
cipher = DES.new(key, DES.MODE_CBC, iv)
encrypted_hash = cipher.encrypt(pad(h.encode(), 8))
print("Encrypted Hash:", encrypted_hash.hex())

# Decrypt the hash
cipher = DES.new(key, DES.MODE_CBC, iv)
decrypted_hash = unpad(cipher.decrypt(encrypted_hash), 8).decode()

print("Decrypted Hash:", decrypted_hash)

# Verify hash with original message
new_hash = hashlib.md5(message.encode()).hexdigest()

if new_hash == decrypted_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
