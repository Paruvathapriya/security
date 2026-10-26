#only hash
# AES ENCRYPTION WITH MD5 HASH

# Import AES cipher
from Crypto.Cipher import AES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib for MD5
import hashlib

# Get message from user
message = input("Enter message: ")

# Set 16-byte key and IV
key = b"1234567890123456"
iv = b"1234567890123456"

# Generate MD5 hash
h = hashlib.md5(message.encode()).hexdigest()
print("Original Hash:", h)

# Encrypt only the hash
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted_hash = cipher.encrypt(pad(h.encode(), 16))
print("Encrypted Hash:", encrypted_hash.hex())

# Decrypt the hash
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_hash = unpad(cipher.decrypt(encrypted_hash), 16).decode()

print("Decrypted Hash:", decrypted_hash)

# Verify hash
new_hash = hashlib.md5(message.encode()).hexdigest()

if new_hash == decrypted_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
