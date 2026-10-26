#encrypt msg and hash
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import hashlib

message = input("Enter message: ")

key = b"12345678"
iv = b"12345678"

# Generate SHA-256 hash
h = hashlib.sha256(message.encode()).hexdigest()
print("Original Hash:", h)

# Encrypt only the hash
cipher = DES.new(key, DES.MODE_CBC, iv)
encrypted_hash = cipher.encrypt(pad(h.encode(), 8))
print("Encrypted Hash:", encrypted_hash.hex())

# Decrypt the hash
cipher = DES.new(key, DES.MODE_CBC, iv)
decrypted_hash = unpad(
    cipher.decrypt(encrypted_hash), 8
).decode()

print("Decrypted Hash:", decrypted_hash)

# Verify with message
new_hash = hashlib.sha256(message.encode()).hexdigest()

if new_hash == decrypted_hash:
    print("Hash Verified")
else:
    print("Hash Mismatch")
