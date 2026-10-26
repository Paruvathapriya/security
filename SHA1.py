
# SHA-1 MESSAGE DIGEST

# Import hashlib library
import hashlib

# Function to generate SHA-1 hash
def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()

# Function to demonstrate avalanche effect
def avalanche():

    # Get original and modified messages
    text = input("Enter message: ")
    modified = input("Enter modified message: ")

    # Display both hash values
    print("Original Hash:", sha1(text))
    print("Modified Hash:", sha1(modified))

# Function to compare two messages
def compare():

    # Get two messages
    a = input("Enter first message: ")
    b = input("Enter second message: ")

    # Compare hash values
    if sha1(a) == sha1(b):
        print("Messages are identical")
    else:
        print("Messages are different")

# Function for SHA-1 preprocessing
def padding():

    # Get message
    text = input("Enter sentence: ")

    # Convert text to bytes
    data = text.encode()

    # Convert bytes to binary
    binary = ''.join(format(byte, '08b') for byte in data)

    # Find original message length
    length = len(binary)

    # Append 1 bit
    padded = binary + '1'

    # Add zero bits until length reaches 448 mod 512
    padded += '0' * ((448 - len(padded) % 512) % 512)

    # Append original length as 64 bits
    padded += format(length, '064b')

    # Display binary and padded message
    print("Original Binary:", binary)
    print("Padded Message:", padded)

    # Divide padded message into 512-bit blocks
    print("512-bit Blocks:")
    for i in range(0, len(padded), 512):
        print(padded[i:i+512])

    # Display SHA-1 digest
    print("SHA-1 Digest:", sha1(text))

# Menu-driven program
while True:
    print("\n--- SHA-1 MENU ---")
    print("1. Generate SHA-1 Digest")
    print("2. Avalanche Effect")
    print("3. Compare Two Messages")
    print("4. SHA-1 Preprocessing")
    print("5. Exit")

    # Get user choice
    choice = input("Enter choice: ")

    if choice == '1':
        # Generate SHA-1 digest
        text = input("Enter message: ")
        print("Message:", text)
        print("SHA-1 Digest:", sha1(text))

    elif choice == '2':
        # Demonstrate avalanche effect
        avalanche()

    elif choice == '3':
        # Compare two messages
        compare()

    elif choice == '4':
        # Display SHA-1 padding steps
        padding()

    elif choice == '5':
        # Exit program
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
