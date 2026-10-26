
# MANUAL RSA ALGORITHM

# Import gcd to check coprime numbers
from math import gcd

# Get two prime numbers
p = int(input("Enter prime p: "))
q = int(input("Enter prime q: "))

# Get public exponent
e = int(input("Enter public exponent e: "))

# Get message as number
message = int(input("Enter message (number): "))

# Calculate n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Check valid RSA parameters
if p == q or gcd(e, phi) != 1 or not (1 < e < phi):
    print("Invalid RSA parameters")
    exit()

# Check message range
if not (0 <= message < n):
    print("Message must be between 0 and", n - 1)
    exit()

# Find private key
d = pow(e, -1, phi)

# Display public and private keys
print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Encryption
encrypted = pow(message, e, n)
print("Encrypted Message:", encrypted)

# Decryption
decrypted = pow(encrypted, d, n)
print("Decrypted Message:", decrypted)
