
# DES ALGORITHM

# Import DES cipher
from Crypto.Cipher import DES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Get 8-byte secret key
key = input("Enter 8-byte secret key: ").encode()

# Check key length
if len(key) != 8:
    print("Key must be exactly 8 bytes!")

else:
    # Get plaintext
    text = input("Enter plaintext: ").encode()

    # Create DES cipher in ECB mode
    cipher = DES.new(key, DES.MODE_ECB)

    # Pad plaintext and encrypt
    encrypted = cipher.encrypt(pad(text, DES.block_size))

    # Display plaintext
    print("Plaintext:", text.decode())

    # Display secret key
    print("Secret Key:", key.decode())

    # Display encrypted text in hexadecimal
    print("Ciphertext (Hex):", encrypted.hex())

    # Decrypt and remove padding
    decrypted = unpad(cipher.decrypt(encrypted), DES.block_size)

    # Display decrypted plaintext
    print("Decrypted Plaintext:", decrypted.decode())

    # Check if decrypted text matches original text
    print("Match:", decrypted == text)
