
# PLAYFAIR CIPHER

# Generate 5x5 key matrix
def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    chars = ""

    # Remove repeated letters
    for ch in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if ch.isalpha() and ch not in chars:
            chars += ch

    # Convert into 5x5 matrix
    return [list(chars[i:i+5]) for i in range(0, 25, 5)]

# Prepare plaintext for encryption
def preprocess(text):
    # Convert to uppercase and replace J with I
    text = ''.join(ch for ch in text.upper().replace('J', 'I') if ch.isalpha())
    result = ""
    i = 0

    while i < len(text):
        result += text[i]

        # Add X between repeated letters
        if i + 1 < len(text) and text[i] == text[i+1]:
            result += 'X'
            i += 1

        # Add next letter
        elif i + 1 < len(text):
            result += text[i+1]
            i += 2
        else:
            i += 1

    # Add X if length is odd
    if len(result) % 2 != 0:
        result += 'X'

    return result

# Encrypt or decrypt using Playfair rules
def playfair(text, matrix, mode):
    result = ""

    # Process two letters at a time
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        # Find positions of both letters
        r1, c1 = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == a)
        r2, c2 = next((r, c) for r in range(5) for c in range(5) if matrix[r][c] == b)

        # +1 for encryption, -1 for decryption
        shift = 1 if mode == 'E' else -1

        # Rule 1: Same row
        if r1 == r2:
            result += matrix[r1][(c1+shift) % 5] + matrix[r2][(c2+shift) % 5]

        # Rule 2: Same column
        elif c1 == c2:
            result += matrix[(r1+shift) % 5][c1] + matrix[(r2+shift) % 5][c2]

        # Rule 3: Rectangle rule
        else:
            result += matrix[r1][c2] + matrix[r2][c1]

    return result

# Get keyword from user
key = input("Enter keyword: ")

# Generate key matrix
matrix = generate_matrix(key)

# Display matrix
print("Key Matrix:")
for row in matrix:
    print(row)

# Get plaintext
text = input("Enter plaintext: ")

# Prepare text
plain = preprocess(text)

# Encrypt plaintext
cipher = playfair(plain, matrix, 'E')
print("Encrypted text:", cipher)

# Decrypt ciphertext
print("Decrypted text:", playfair(cipher, matrix, 'D'))
