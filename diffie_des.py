
# DIFFIE-HELLMAN + DES ENCRYPTION

# Import DES cipher
from Crypto.Cipher import DES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Import hashlib
import hashlib

# Get prime number and primitive root
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Get private keys
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

# Calculate public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Calculate shared secret keys
alice_key = pow(B, a, p)
bob_key = pow(A, b, p)

# Display public keys
print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

# Display shared keys
print("Alice's Shared Key:", alice_key)
print("Bob's Shared Key:", bob_key)

# Check shared keys
if alice_key == bob_key:
    print("Key Exchange Successful")

    # Convert shared secret into 8-byte DES key
    key = hashlib.sha256(str(alice_key).encode()).digest()[:8]

    # Generate random IV
    iv = DES.new(key, DES.MODE_CBC).iv

    # Get plaintext
    message = input("Enter message: ").encode()

    # Encrypt using DES
    cipher = DES.new(key, DES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(message, 8))

    print("Encrypted Message:", encrypted.hex())

    # Generate DES key for Bob
    bob_des_key = hashlib.sha256(str(bob_key).encode()).digest()[:8]

    # Decrypt using DES
    cipher = DES.new(bob_des_key, DES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(encrypted), 8)

    print("Decrypted Message:", decrypted.decode())

    # Verify decryption
    if decrypted == message:
        print("Decryption Successful")
    else:
        print("Decryption Failed")

else:
    print("Key Exchange Failed")
