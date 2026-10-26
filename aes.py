
# AES ALGORITHM

# Import AES cipher
from Crypto.Cipher import AES

# Import padding functions
from Crypto.Util.Padding import pad, unpad

# Get 16-byte secret key
key = input("Enter 16-byte secret key: ").encode()

# Check key length
if len(key) != 16:
    print("Key must be exactly 16 bytes!")

else:
    # Get plaintext
    text = input("Enter plaintext: ").encode()

    # Create AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad plaintext and encrypt
    encrypted = cipher.encrypt(pad(text, AES.block_size))

    # Display plaintext
    print("Plaintext:", text.decode())

    # Display secret key
    print("Secret Key:", key.decode())

    # Display ciphertext in hexadecimal
    print("Ciphertext (Hex):", encrypted.hex())

    # Decrypt and remove padding
    decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

    # Display decrypted plaintext
    print("Decrypted Plaintext:", decrypted.decode())

    # Check whether original and decrypted text match
    print("Match:", decrypted == text)
