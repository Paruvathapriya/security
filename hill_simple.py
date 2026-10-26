import numpy as np

key = np.array([[3, 3], [2, 5]])

text = input("Enter plaintext: ").upper().replace(" ", "")

if len(text) % 2 != 0:
    text += 'X'

# Encryption
encrypted = ""

for i in range(0, len(text), 2):
    pair = np.array([ord(text[i]) - 65, ord(text[i+1]) - 65])
    result = np.dot(key, pair) % 26
    encrypted += ''.join(chr(x + 65) for x in result)

print("Encrypted:", encrypted)

# Finding inverse key
det = round(np.linalg.det(key))
det_inv = pow(det % 26, -1, 26)

adj = np.array([[key[1][1], -key[0][1]],
                [-key[1][0], key[0][0]]])

inverse = (det_inv * adj) % 26

# Decryption
decrypted = ""

for i in range(0, len(encrypted), 2):
    pair = np.array([ord(encrypted[i]) - 65, ord(encrypted[i+1]) - 65])
    result = np.dot(inverse, pair) % 26
    decrypted += ''.join(chr(x + 65) for x in result)

print("Decrypted:", decrypted)