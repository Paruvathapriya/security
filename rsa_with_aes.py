#This program uses RSA to encrypt the AES key and AES to encrypt the message. It also performs decryption and verifies that the original message is recovered.


# RSA + AES HYBRID ENCRYPTION

# Import RSA and AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

# Generate RSA keys
key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

# Get message
message = input("Enter message: ").encode()

# Set 16-byte AES key and IV
aes_key = b"1234567890123456"
iv = b"1234567890123456"

# Encrypt message using AES
cipher = AES.new(aes_key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(message, 16))
print("AES Encrypted Message:", encrypted.hex())

# Encrypt AES key using RSA public key
rsa_cipher = PKCS1_OAEP.new(public_key)
encrypted_key = rsa_cipher.encrypt(aes_key)
print("RSA Encrypted AES Key:", encrypted_key.hex())

# Decrypt AES key using RSA private key
rsa_cipher = PKCS1_OAEP.new(private_key)
decrypted_key = rsa_cipher.decrypt(encrypted_key)
print("Decrypted AES Key:", decrypted_key.decode())

# Decrypt message using AES
cipher = AES.new(decrypted_key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 16)

print("Decrypted Message:", decrypted.decode())

# Verify original and decrypted messages
if decrypted == message:
    print("Decryption Successful")
else:
    print("Decryption Failed")
