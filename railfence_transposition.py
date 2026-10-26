
# RAIL FENCE TRANSPOSITION TECHNIQUE

# Function for row-major encryption
def encrypt_row(text, cols):

    # Add X to make text length divisible by columns
    text += 'X' * ((-len(text)) % cols)

    # Calculate number of rows
    rows = len(text) // cols

    # Create empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0

    # Fill matrix column by column
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = text[k]
            k += 1

    # Display encryption matrix
    print("Encryption Matrix (Row Major):")
    for row in matrix:
        print(' '.join(row))

    # Read matrix row by row
    return ''.join(matrix[r][c] for r in range(rows) for c in range(cols))


# Function for row-major decryption
def decrypt_row(cipher, cols):

    # Calculate number of rows
    rows = len(cipher) // cols

    # Fill matrix row by row
    matrix = [list(cipher[r*cols:(r+1)*cols]) for r in range(rows)]

    # Read matrix column by column
    text = ''.join(matrix[r][c] for c in range(cols) for r in range(rows))

    # Remove extra X
    return text.rstrip('X')


# Function for column-major encryption
def encrypt_col(text, cols):

    # Add X for padding
    text += 'X' * ((-len(text)) % cols)

    # Calculate number of rows
    rows = len(text) // cols

    # Fill matrix row by row
    matrix = [list(text[r*cols:(r+1)*cols]) for r in range(rows)]

    # Display encryption matrix
    print("Encryption Matrix (Column Major):")
    for row in matrix:
        print(' '.join(row))

    # Read matrix column by column
    return ''.join(matrix[r][c] for c in range(cols) for r in range(rows))


# Function for column-major decryption
def decrypt_col(cipher, cols):

    # Calculate number of rows
    rows = len(cipher) // cols

    # Create empty matrix
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    k = 0

    # Fill matrix column by column
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = cipher[k]
            k += 1

    # Read row by row and remove extra X
    return ''.join(''.join(row) for row in matrix).rstrip('X')


# Get plaintext from user
text = input("Enter plaintext: ").replace(" ", "").upper()

# Get number of columns
cols = int(input("Enter number of columns: "))

# Check valid number of columns
if cols <= 0:
    print("Number of columns must be positive.")
else:
    # Row-major encryption
    cipher1 = encrypt_row(text, cols)
    print("Row Major Ciphertext:", cipher1)

    # Row-major decryption
    print("Decrypted Plaintext:", decrypt_row(cipher1, cols))
    print()

    # Column-major encryption
    cipher2 = encrypt_col(text, cols)
    print("Column Major Ciphertext:", cipher2)

    # Column-major decryption
    print("Decrypted Plaintext:", decrypt_col(cipher2, cols))
