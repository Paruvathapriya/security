
# RSA ENCRYPTION

# Import RSA algorithm
from Crypto.PublicKey import RSA

# Import RSA encryption method
from Crypto.Cipher import PKCS1_OAEP

# Generate 2048-bit RSA key
key = RSA.generate(2048)

# Generate public key
public_key = key.publickey()

# Assign private key
private_key = key

# Get plaintext
text = input("Enter plaintext: ").encode()

# Display public key
print("Public Key:")
print(public_key.export_key().decode())

# Display private key
print("Private Key:")
print(private_key.export_key().decode())

# Create cipher using public key
cipher = PKCS1_OAEP.new(public_key)

# Encrypt plaintext
encrypted = cipher.encrypt(text)

# Display ciphertext in hexadecimal
print("Ciphertext (Hex):", encrypted.hex())

# Create cipher using private key
cipher = PKCS1_OAEP.new(private_key)

# Decrypt ciphertext
decrypted = cipher.decrypt(encrypted)

# Display decrypted plaintext
print("Decrypted Plaintext:", decrypted.decode())

# Check whether plaintext matches decrypted text
print("Match:", decrypted == text)
