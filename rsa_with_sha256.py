
# RSA ENCRYPTION WITH SHA-256 HASH

# Import RSA algorithm
from Crypto.PublicKey import RSA

# Import RSA encryption method
from Crypto.Cipher import PKCS1_OAEP

# Import hashlib
import hashlib

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Get message
message = input("Enter message: ")

# Generate SHA-256 hash
h = hashlib.sha256(message.encode()).hexdigest()
print("Original Hash:", h)

# Encrypt message using public key
cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message.encode())

print("Encrypted Message:", encrypted.hex())

# Decrypt using private key
cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(encrypted).decode()

print("Decrypted Message:", decrypted)

# Verify hash
new_hash = hashlib.sha256(decrypted.encode()).hexdigest()

if new_hash == h:
    print("Hash Verified")
else:
    print("Hash Mismatch")
