
# DIGITAL SIGNATURE SYSTEM

# Import RSA algorithm
from Crypto.PublicKey import RSA

# Import digital signature method
from Crypto.Signature import pkcs1_15

# Import SHA-256 hashing
from Crypto.Hash import SHA256

# Function to generate RSA keys
def generate_keys():

    # Generate 2048-bit RSA key
    key = RSA.generate(2048)

    # Save private key to file
    with open("private.pem", "wb") as f:
        f.write(key.export_key())

    # Save public key to file
    with open("public.pem", "wb") as f:
        f.write(key.publickey().export_key())

    # Display generated keys
    print("RSA Keys Generated and Saved")
    print("Public Key:\n", key.publickey().export_key().decode())
    print("Private Key:\n", key.export_key().decode())


# Function to digitally sign a message
def sign_message():
    try:
        # Read private key
        key = RSA.import_key(open("private.pem", "rb").read())

        # Get message
        text = input("Enter message: ")

        # Generate SHA-256 hash
        h = SHA256.new(text.encode())

        # Sign hash using private key
        signature = pkcs1_15.new(key).sign(h)

        # Display message, hash and signature
        print("Original Message:", text)
        print("SHA-256 Digest:", h.hexdigest())
        print("Digital Signature:", signature.hex())

    # Handle missing key file
    except FileNotFoundError:
        print("Generate keys first!")


# Function to verify digital signature
def verify_signature():
    try:
        # Read public key
        key = RSA.import_key(open("public.pem", "rb").read())

        # Get original message
        text = input("Enter original message: ")

        # Get signature in hexadecimal
        signature = bytes.fromhex(input("Enter signature in hex: "))

        # Generate SHA-256 hash
        h = SHA256.new(text.encode())

        # Verify signature using public key
        pkcs1_15.new(key).verify(h, signature)
        print("Signature is Valid")

    # Handle invalid signature
    except (ValueError, TypeError):
        print("Signature is Invalid")

    # Handle missing key file
    except FileNotFoundError:
        print("Generate keys first!")


# Function to demonstrate message tampering
def tampering():
    try:
        # Read private and public keys
        key = RSA.import_key(open("private.pem", "rb").read())
        public = RSA.import_key(open("public.pem", "rb").read())

        # Get original message
        text = input("Enter message: ")

        # Sign original message using private key
        signature = pkcs1_15.new(key).sign(SHA256.new(text.encode()))

        # Modify the message
        modified = text + "X"

        # Display original and modified messages
        print("Original Message:", text)
        print("Modified Message:", modified)

        try:
            # Verify modified message using original signature
            pkcs1_15.new(public).verify(SHA256.new(modified.encode()), signature)
            print("Signature is Valid")

        # Detect message modification
        except (ValueError, TypeError):
            print("Verification Failed: Message was altered")

    # Handle missing key files
    except FileNotFoundError:
        print("Generate keys first!")


# Function to demonstrate secure email communication
def email_demo():
    try:
        # Read private and public keys
        key = RSA.import_key(open("private.pem", "rb").read())
        public = RSA.import_key(open("public.pem", "rb").read())

        # Get Alice's message
        text = input("Alice's message to Bob: ")

        # Alice signs message using private key
        signature = pkcs1_15.new(key).sign(SHA256.new(text.encode()))

        # Display message and signature
        print("Alice signs and sends the message to Bob.")
        print("Message:", text)
        print("Signature:", signature.hex())

        try:
            # Bob verifies signature using public key
            pkcs1_15.new(public).verify(SHA256.new(text.encode()), signature)
            print("Bob: Signature Valid")

        except (ValueError, TypeError):
            print("Bob: Signature Invalid")

        # Modify the message
        modified = text + "X"
        print("Modified message received:", modified)

        try:
            # Verify modified message
            pkcs1_15.new(public).verify(SHA256.new(modified.encode()), signature)
            print("Bob: Signature Valid")

        # Detect tampering
        except (ValueError, TypeError):
            print("Bob: Verification Failed - Message Tampered")

    # Handle missing key files
    except FileNotFoundError:
        print("Generate keys first!")


# Menu-driven program
while True:
    print("\n========== DIGITAL SIGNATURE SYSTEM ==========")
    print("1. Generate RSA Public and Private Keys")
    print("2. Digitally Sign a Message")
    print("3. Verify a Digital Signature")
    print("4. Demonstrate Message Tampering")
    print("5. Secure Email Communication (Alice and Bob)")
    print("6. Exit")

    # Get user choice
    choice = input("Enter choice: ")

    if choice == '1':
        # Generate RSA keys
        generate_keys()

    elif choice == '2':
        # Sign a message
        sign_message()

    elif choice == '3':
        # Verify digital signature
        verify_signature()

    elif choice == '4':
        # Demonstrate tampering detection
        tampering()

    elif choice == '5':
        # Demonstrate Alice and Bob communication
        email_demo()

    elif choice == '6':
        # Exit program
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
