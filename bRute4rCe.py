from itertools import product
from Crypto.Cipher import ARC4

# Provide the Ciphertext
ciphertext_hex = 'insert ciphertext here'
ciphertext = bytes.fromhex(ciphertext_hex)

# Function to attempt RC4 decryption with a given password
def rc4_decrypt(ciphertext, password):
    cipher = ARC4.new(password.encode())
    return cipher.decrypt(ciphertext)

# Generate all possible 4-character passwords (lowercase, uppercase, and digits)
possible_passwords = product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', repeat=4)

# Try each password
for password_tuple in possible_passwords:
    password = ''.join(password_tuple)
    decrypted_message = rc4_decrypt(ciphertext, password)
    try:
        decrypted_message_str = decrypted_message.decode('utf-8')
        if decrypted_message_str.isprintable():
            print(f"Password: {password}, Decrypted message: {decrypted_message_str}")
    except UnicodeDecodeError:
        continue
