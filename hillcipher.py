
# HILL CIPHER

from math import gcd

# Calculate determinant
def determinant(key):
    return (key[0][0]*key[1][1] - key[0][1]*key[1][0]) % 26

# Find inverse key matrix
def inverse_key(key):
    det = determinant(key)

    # Check if determinant is coprime with 26
    if gcd(det, 26) != 1:
        raise ValueError("Key matrix is not invertible modulo 26")

    # Find modular inverse of determinant
    det_inv = next(i for i in range(26) if (det*i) % 26 == 1)

    # Calculate inverse matrix
    return [[key[1][1]*det_inv % 26, -key[0][1]*det_inv % 26],
            [-key[1][0]*det_inv % 26, key[0][0]*det_inv % 26]]

# Encrypt or decrypt text
def process(text, key):

    # Convert text to uppercase and remove spaces
    text = ''.join(ch for ch in text.upper() if ch.isalpha())

    # Add X if length is odd
    if len(text) % 2:
        text += 'X'

    result = ""

    # Process two letters at a time
    for i in range(0, len(text), 2):

        # Convert letters to numbers (A=0, B=1...)
        a, b = ord(text[i])-65, ord(text[i+1])-65

        # Matrix multiplication
        result += chr((key[0][0]*a + key[0][1]*b) % 26 + 65)
        result += chr((key[1][0]*a + key[1][1]*b) % 26 + 65)

    return result

try:
    # Get key matrix
    print("Enter 2x2 key matrix:")
    key = [[int(input("a: ")), int(input("b: "))],
           [int(input("c: ")), int(input("d: "))]]

    # Calculate determinant
    det = determinant(key)
    print("Determinant:", det)

    # Generate inverse key matrix
    inv = inverse_key(key)
    print("Inverse Key Matrix:", inv)

    # Get plaintext
    text = input("Enter plaintext: ")

    # Encryption
    cipher = process(text, key)
    print("Encrypted text:", cipher)

    # Decryption
    print("Decrypted text:", process(cipher, inv))

except ValueError as e:
    print(e)
