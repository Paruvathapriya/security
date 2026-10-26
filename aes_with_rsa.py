
# AES + RSA DIGITAL SIGNATURE

# Import AES and RSA
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import digital signature and SHA-256
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Set AES key and IV
aes_key = b"1234567890123456"
iv = b"1234567890123456"

# Get message
message = input("Enter message: ").encode()

# Encrypt message using AES
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(message, 16))

print("Encrypted Message:", encrypted.hex())

# Generate SHA-256 hash of encrypted message
h = SHA256.new(encrypted)
print("SHA-256 Hash:", h.hexdigest())

# Sign the hash using RSA private key
signature = pkcs1_15.new(private_key).sign(h)
print("Digital Signature:", signature.hex())

# Verify signature using RSA public key
try:
    pkcs1_15.new(public_key).verify(SHA256.new(encrypted), signature)
    print("Signature Verified")
except (ValueError, TypeError):
    print("Signature Invalid")

# Decrypt message using AES
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Decrypted Message:", decrypted.decode())

# Check original and decrypted message
if decrypted == message:
    print("Decryption Successful")
else:
    print("Decryption Failed")

# Demonstrate tampering
modified = encrypted[:-1] + bytes([encrypted[-1] ^ 1])

# Verify modified ciphertext
try:
    pkcs1_15.new(public_key).verify(SHA256.new(modified), signature)
    print("Modified Message Accepted")
except (ValueError, TypeError):
    print("Tampering Detected")
