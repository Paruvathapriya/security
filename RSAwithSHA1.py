
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

# Convert hash into integer and reduce modulo n
H = int(h, 16) % n

# Display message and hash values
print("Message:", message)
print("SHA-1 Hash:", h)
print("Hash Integer:", int(h, 16))
print("Reduced Hash:", H)

# Generate signature
# Sign the hash using private key
S = pow(H, d, n)
print("Digital Signature:", S)

# Verify signature
# Verify using public key
H_new = pow(S, e, n)
print("Verified Hash:", H_new)

# Compare original and verified hashes
if H == H_new:
    print("Signature Verified")
else:
    print("Signature Invalid")

# Tampering detection
# Modify the original message
modified = "PAY RAHUL RS 9000"

# Generate SHA-1 hash of modified message
h2 = hashlib.sha1(modified.encode()).hexdigest()
H2 = int(h2, 16) % n

# Display modified message and hash
print("Modified Message:", modified)
print("Modified Hash:", H2)

# Check whether modified message passes verification
if H2 == pow(S, e, n):
    print("Modified Message Accepted")
else:
    print("Tampering Detected")

# Explain private key and public key usage
print("Only the private key can be used")
print("to create the signature.")
print("Anyone can verify using the public key.")
