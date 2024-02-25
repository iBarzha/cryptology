def caesar_cipher_encrypt(plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift = 1  # Caesar cipher with key 1
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += new_char
        else:
            ciphertext += char  # If not a letter, keep the character unchanged
    return ciphertext

def caesar_cipher_decrypt(ciphertext):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = 1  # Caesar cipher with key 1
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            plaintext += new_char
        else:
            plaintext += char
    return plaintext

# Surname for encryption
surname = "Bardzheiev"

# Encryption
encrypted_surname = caesar_cipher_encrypt(surname)
print("Зашифроване прізвище:", encrypted_surname)

# Deciphering
decrypted_surname = caesar_cipher_decrypt(encrypted_surname)
print("Дешифроване прізвище:", decrypted_surname)
