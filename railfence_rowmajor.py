
# RAIL FENCE CIPHER

# Function to encrypt plaintext
def encrypt(text, key):

    # Create empty rail fence matrix
    fence = [[' ' for i in range(len(text))] for j in range(key)]
    row, step = 0, 1

    # Arrange letters in zigzag pattern
    for col in range(len(text)):
        fence[row][col] = text[col]

        # Move downward
        if row == 0:
            step = 1

        # Move upward
        elif row == key - 1:
            step = -1

        row += step

    # Display rail fence pattern
    print("Rail Fence:")
    for r in fence:
        print(' '.join(r))

    # Read letters row by row
    cipher = ''.join(ch for r in fence for ch in r if ch != ' ')
    return cipher


# Function to decrypt ciphertext
def decrypt(cipher, key):

    # Create empty rail fence matrix
    fence = [[' ' for i in range(len(cipher))] for j in range(key)]
    row, step = 0, 1

    # Mark zigzag positions using *
    for col in range(len(cipher)):
        fence[row][col] = '*'

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1

        row += step

    # Fill ciphertext into marked positions
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if fence[i][j] == '*':
                fence[i][j] = cipher[index]
                index += 1

    # Read letters in zigzag order
    return ''.join(fence[i][j] for j in range(len(cipher))
                   for i in range(key) if fence[i][j] != ' ')


# Get plaintext from user
text = input("Enter plaintext: ").replace(" ", "").upper()

# Get number of rails
key = int(input("Enter key: "))

# Check valid key
if key < 2:
    print("Key must be at least 2")
else:
    # Encrypt plaintext
    cipher = encrypt(text, key)
    print("Ciphertext:", cipher)

    # Decrypt ciphertext
    print("Decrypted:", decrypt(cipher, key))
