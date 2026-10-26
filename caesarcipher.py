
# CAESAR CIPHER PROGRAM

# Function to encrypt the text
def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            # Check uppercase or lowercase
            base = ord('A') if ch.isupper() else ord('a')
            # Shift the character using the key
            result += chr((ord(ch) - base + key) % 26 + base)
        else:
            # Keep spaces, numbers and symbols unchanged
            result += ch
    return result

# Function to decrypt the text
def decrypt(text, key):
    return encrypt(text, -key)

# Try all possible keys
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
        # Encrypt plaintext
        text = input("Enter plaintext: ")
        key = int(input("Enter key (1-25): "))
        print("Encrypted text:", encrypt(text, key))

    elif choice == '2':
        # Decrypt ciphertext
        text = input("Enter ciphertext: ")
        key = int(input("Enter key (1-25): "))
        print("Decrypted text:", decrypt(text, key))

    elif choice == '3':
        # Display all possible decrypted texts
        text = input("Enter ciphertext: ")
        brute_force(text)

    elif choice == '4':
        # Exit the program
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
