#hill
from math import gcd

key = [[5, 8], [17, 3]]
text = "MATH"

print("Key Matrix:")
for row in key:
    print(row)

# Step 1: Convert text to numbers
nums = [ord(c) - 65 for c in text]
print("Plaintext Numbers:", nums)

# Step 2: Find determinant
a, b = key[0]
c, d = key[1]

det = a * d - b * c
print("Determinant:", det)

# Step 3: Check invertibility
if gcd(det, 26) != 1:
    print("Key is not invertible")
    exit()

print("Key is invertible")

# Step 4: Find inverse matrix
det_inv = pow(det % 26, -1, 26)

inverse = [
    [(d * det_inv) % 26, (-b * det_inv) % 26],
    [(-c * det_inv) % 26, (a * det_inv) % 26]
]

print("Inverse Key Matrix:")
for row in inverse:
    print(row)

# Step 5: Matrix multiplication
def convert(text, matrix):
    result = ""

    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i + 1]) - 65

        p = (matrix[0][0]*x + matrix[0][1]*y) % 26
        q = (matrix[1][0]*x + matrix[1][1]*y) % 26

        result += chr(p + 65) + chr(q + 65)

    return result

# Step 6: Encrypt
cipher = convert(text, key)
print("Ciphertext:", cipher)

# Step 7: Decrypt
plain = convert(cipher, inverse)
print("Decrypted Text:", plain)

#rsa with md5
import hashlib
from math import gcd

# Given values
p = 37
q = 41
e = 23

message = "CONFIRM ORDER 10245"

# Step 1: Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

print("n:", n)
print("Phi:", phi)
print("GCD:", gcd(e, phi))

if gcd(e, phi) != 1:
    print("Invalid public exponent")
    exit()

# Step 2: Calculate private key
d = pow(e, -1, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Step 3: Generate MD5 hash
md5 = hashlib.md5(message.encode()).hexdigest()

hash_int = int(md5, 16)
H = hash_int % n

print("Message:", message)
print("MD5 Digest:", md5)
print("MD5 Integer:", hash_int)
print("Reduced Hash H:", H)

# Step 4: Sign using private key
S = pow(H, d, n)
print("Digital Signature:", S)

# Step 5: Verify using public key
H_new = pow(S, e, n)

print("Verified Hash:", H_new)

if H == H_new:
    print("Signature Verified Successfully")
else:
    print("Signature Verification Failed")

# Step 6: Attacker modifies message
modified = "CONFIRM ORDER 10246"

modified_md5 = hashlib.md5(modified.encode()).hexdigest()
modified_H = int(modified_md5, 16) % n

print("\nModified Message:", modified)
print("Modified Hash:", modified_H)

# Attacker tries to reuse original signature
attacker_check = pow(S, e, n)

if modified_H == attacker_check:
    print("Modified Message Accepted")
else:
    print("Modified Message Rejected")

print("Attacker cannot correctly sign a new")
print("message using only the public key.")
print("Private key d is required for signing.")

#caesar

# CAESAR CIPHER PROGRAM

# Function to encrypt plaintext
def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            # Check uppercase or lowercase
            base = ord('A') if ch.isupper() else ord('a')

            # Shift character using key
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            # Keep numbers, spaces and symbols unchanged
            result += ch

    return result

# Function to decrypt ciphertext
def decrypt(text, key):
    return encrypt(text, -key)

# Try all possible shifts
def brute_force(text):
    for key in range(1, 26):
        print("Key", key, ":", decrypt(text, key))

# Menu-driven program
while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Brute Force Attack")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        # Get plaintext and key
        text = input("Enter plaintext: ")
        key = int(input("Enter key: "))

        # Encrypt plaintext
        cipher = encrypt(text, key)
        print("Encrypted text:", cipher)

        # Count encrypted alphabetic characters
        print("Number of characters encrypted:", sum(ch.isalpha() for ch in text))

    elif choice == '2':
        # Decrypt ciphertext
        text = input("Enter ciphertext: ")
        key = int(input("Enter key: "))
        print("Decrypted text:", decrypt(text, key))

    elif choice == '3':
        # Perform brute-force attack
        text = input("Enter ciphertext: ")
        brute_force(text)

    elif choice == '4':
        # Exit program
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")


#rsa with sha1

# RSA DIGITAL SIGNATURE USING SHA-1

# Import hashlib for SHA-1 hashing
import hashlib

# Import gcd to check coprime numbers
from math import gcd

# Define original message
message = "PAY RAHUL RS 5000"

# Set two prime numbers
p = 47
q = 59

# Set public exponent
e = 17

# Calculate n and phi
n = p*q
phi = (p-1)*(q-1)

# Display n, phi and GCD
print("n:", n)
print("Phi:", phi)
print("GCD:", gcd(e, phi))

# Check whether public exponent is valid
if gcd(e, phi) != 1:
    print("Invalid public exponent")
    exit()

# Calculate private key
d = pow(e, -1, phi)

# Display public and private keys
print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Generate SHA-1 hash
h = hashlib.sha1(message.encode()).hexdigest()

# Convert hash to integer and reduce modulo n
H = int(h, 16) % n

# Display message and hash values
print("Message:", message)
print("SHA-1 Hash:", h)
print("Hash Integer:", int(h, 16))
print("Reduced Hash:", H)

# Generate digital signature using private key
S = pow(H, d, n)
print("Digital Signature:", S)

# Verify signature using public key
H_new = pow(S, e, n)
print("Verified Hash:", H_new)

# Compare original and verified hashes
if H == H_new:
    print("Signature Verified")
else:
    print("Signature Invalid")

# Tampering detection
modified = "PAY RAHUL RS 9000"

# Generate hash of modified message
h2 = hashlib.sha1(modified.encode()).hexdigest()
H2 = int(h2, 16) % n

# Display modified message and hash
print("Modified Message:", modified)
print("Modified Hash:", H2)

# Verify old signature against modified message
if H2 == pow(S, e, n):
    print("Modified Message Accepted")
else:
    print("Tampering Detected")

# Explain signature concept
print("Only the private key can be used")
print("to create the signature.")
print("Anyone can verify using the public key.")


#aes encrypt only plain text
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

text = input("Enter plaintext: ")

key = b"1234567890123456"
iv = b"1234567890123456"

# Generate MD5 hash
h1 = hashlib.md5(text.encode()).hexdigest()
print("Original MD5 Hash:", h1)

# AES Encryption
cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(text.encode(), 16))
print("Encrypted Text:", encrypted.hex())

# AES Decryption
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher.decrypt(encrypted), 16).decode()
print("Decrypted Text:", decrypted)

# Verify MD5 hash
h2 = hashlib.md5(decrypted.encode()).hexdigest()
print("Decrypted MD5 Hash:", h2)

print("Hash Match:", h1 == h2)