
# RSA DIGITAL SIGNATURE USING MD5

# Import hashlib for MD5 hashing
import hashlib

# Import gcd to check coprime numbers
from math import gcd

# Define original message
message = "CONFIRM ORDER 10245"

# Set two prime numbers
p = 37
q = 41

# Set public exponent
e = 23

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

# Generate MD5 hash
h = hashlib.md5(message.encode()).hexdigest()

# Convert hash into integer and reduce modulo n
H = int(h, 16) % n

# Display message and hash values
print("Message:", message)
print("MD5 Hash:", h)
print("Hash Integer:", int(h, 16))
print("Reduced Hash:", H)

# Digital signature
# Sign the hash using private key
S = pow(H, d, n)
print("Signature:", S)

# Verification
# Verify signature using public key
H_new = pow(S, e, n)
print("Verified Hash:", H_new)

# Compare original and verified hashes
if H == H_new:
    print("Signature Verified")
else:
    print("Signature Invalid")

# Attacker modifies the message
modified = "CONFIRM ORDER 10246"

# Generate hash of modified message
h2 = hashlib.md5(modified.encode()).hexdigest()
H2 = int(h2, 16) % n

# Display modified message and hash
print("Modified Message:", modified)
print("Modified Hash:", H2)

# Check whether modified message passes verification
if H2 == pow(S, e, n):
    print("Modified Message Accepted")
else:
    print("Modified Message Rejected")

# Explain private key requirement
print("Attacker cannot sign a new message")
print("using only the public key.")
print("Private key is required for signing.")
