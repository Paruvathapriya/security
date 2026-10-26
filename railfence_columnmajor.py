
# RAIL FENCE CIPHER - COLUMN MAJOR

# Function to encrypt plaintext
def encrypt(text, key):

    # Create empty rail fence matrix
    fence = [[' ' for i in range(len(text))] for j in range(key)]
    row, step = 0, 1

    # Arrange letters in zigzag pattern
    for col in range(len(text)):
        fence[row][col] = text[col]

        # Move downwards
        if row == 0:
            step = 1

        # Move upwards
        elif row == key - 1:
            step = -1
        row += step

    # Display rail fence matrix
    print("Rail Fence:")
    for r in fence:
        print(' '.join(r))

    # Read letters column by column
    cipher = ''.join(fence[i][j] for j in range(len(text))
                     for i in range(key) if fence[i][j] != ' ')
    return cipher


# Function to decrypt ciphertext
def decrypt(cipher, key):
    # Column-wise reading of a zigzag fence
    # recovers the original character sequence.
    return cipher


# Get plaintext and remove spaces
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


# COLUMN MAJOR RAIL FENCE CIPHER

# Function to encrypt
def encrypt(text, key):
    cols = (len(text) + key - 1) // key

    # Create empty fence
    fence = [[' ' for i in range(cols)] for j in range(key)]

    row, step = 0, 1
    index = 0

    # Fill letters column by column in zigzag order
    for col in range(cols):
        for i in range(key):
            if index < len(text):
                fence[row][col] = text[index]
                index += 1

                if row == 0:
                    step = 1
                elif row == key - 1:
                    step = -1
                row += step

    # Display fence
    print("Rail Fence:")
    for r in fence:
        print(' '.join(r))

    # Read row by row
    cipher = ''.join(ch for r in fence for ch in r if ch != ' ')
    return cipher


# Function to decrypt
def decrypt(cipher, key):
    cols = (len(cipher) + key - 1) // key
    fence = [[' ' for i in range(cols)] for j in range(key)]

    row, step = 0, 1
    count = 0

    # Mark zigzag positions
    for col in range(cols):
        for i in range(key):
            if count < len(cipher):
                fence[row][col] = '*'
                count += 1

                if row == 0:
                    step = 1
                elif row == key - 1:
                    step = -1
                row += step

    # Fill ciphertext row by row
    index = 0
    for r in range(key):
        for c in range(cols):
            if fence[r][c] == '*':
                fence[r][c] = cipher[index]
                index += 1

    # Read column by column in zigzag order
    result = ""
    row, step = 0, 1
    for i in range(len(cipher)):
        col = i // key
        result += fence[row][col]

        if row == 0:
            step = 1
        elif row == key - 1:
            step = -1
        row += step

    return result


# Get input
text = input("Enter plaintext: ").replace(" ", "").upper()
key = int(input("Enter key: "))

# Check key
if key < 2:
    print("Key must be at least 2")
else:
    cipher = encrypt(text, key)
    print("Ciphertext:", cipher)
    print("Decrypted:", decrypt(cipher, key))
