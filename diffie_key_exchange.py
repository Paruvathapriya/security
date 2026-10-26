
# DIFFIE-HELLMAN KEY EXCHANGE

# Get prime number
p = int(input("Enter prime number (p): "))

# Get primitive root
g = int(input("Enter primitive root (g): "))

# Get Alice's private key
a = int(input("Enter Alice's private key: "))

# Get Bob's private key
b = int(input("Enter Bob's private key: "))

# Calculate Alice's public key
A = pow(g, a, p)

# Calculate Bob's public key
B = pow(g, b, p)

# Calculate shared secret key for Alice
alice_key = pow(B, a, p)

# Calculate shared secret key for Bob
bob_key = pow(A, b, p)

# Display input values
print("Prime Number:", p)
print("Primitive Root:", g)
print("Alice's Private Key:", a)
print("Bob's Private Key:", b)

# Display public keys
print("Alice's Public Key:", A)
print("Bob's Public Key:", B)

# Display shared secret keys
print("Shared Secret Key computed by Alice:", alice_key)
print("Shared Secret Key computed by Bob:", bob_key)

# Check whether both shared keys are equal
if alice_key == bob_key:
    print("Key Exchange Successful: Both keys are identical")
else:
    print("Key Exchange Failed")
