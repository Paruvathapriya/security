
# MD5 MESSAGE DIGEST

# Import hashlib library
import hashlib

# Function to generate MD5 hash
def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

# Menu-driven program
while True:
    print("\n--- MD5 MENU ---")
    print("1. Generate MD5 Message Digest")
    print("2. Verify Message Integrity")
    print("3. Demonstrate Avalanche Effect")
    print("4. Generate MD5 Checksum for a Text File")
    print("5. Compare MD5, SHA-1 and SHA-256")
    print("6. Exit")

    # Get user choice
    choice = input("Enter choice: ")

    if choice == '1':
        # Generate MD5 digest
        text = input("Enter message: ")
        print("MD5 Digest:", md5(text))

    elif choice == '2':
        # Get message and previous digest
        text = input("Enter message: ")
        digest = input("Enter previous digest: ").lower()

        # Compare digests to verify integrity
        if md5(text) == digest:
            print("Message Integrity: Matches")
        else:
            print("Message Integrity: Does Not Match")

    elif choice == '3':
        # Get original and modified messages
        text1 = input("Enter original message: ")
        text2 = input("Enter modified message: ")

        # Display both MD5 hashes
        print("Original MD5:", md5(text1))
        print("Modified MD5:", md5(text2))

    elif choice == '4':
        # Get text file path
        path = input("Enter file path: ")

        try:
            # Open file in binary mode
            with open(path, 'rb') as f:
                # Calculate MD5 checksum of file
                print("File MD5:", hashlib.md5(f.read()).hexdigest())

        # Handle missing file
        except FileNotFoundError:
            print("File not found!")

    elif choice == '5':
        # Get message and convert to bytes
        text = input("Enter message: ").encode()

        # Display MD5, SHA-1 and SHA-256 hashes
        print("MD5:", hashlib.md5(text).hexdigest())
        print("SHA-1:", hashlib.sha1(text).hexdigest())
        print("SHA-256:", hashlib.sha256(text).hexdigest())

    elif choice == '6':
        # Exit the program
        print("Exiting program...")
        break

    else:
        # Handle invalid choice
        print("Invalid choice!")
