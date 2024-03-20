import numpy as np
def text_to_numbers(text):
    return [ord(char) - 65 for char in text]

def numbers_to_text(numbers):
    return ''.join([chr(num + 65) for num in numbers])

def hill_cipher_encrypt(plaintext, key_matrix):
    plaintext = plaintext.replace(" ", "").upper()
    plaintext_numbers = text_to_numbers(plaintext)

    n = len(key_matrix)
    if len(plaintext_numbers) % n != 0:
        plaintext_numbers += [0] * (n - len(plaintext_numbers) % n)

    blocks = [plaintext_numbers[i:i + n] for i in range(0, len(plaintext_numbers), n)]

    key_matrix = np.array(key_matrix)

    ciphertext = []
    for block in blocks:
        block = np.array(block)
        encrypted_block = np.dot(key_matrix, block) % 26
        ciphertext.extend(encrypted_block)

    return numbers_to_text(ciphertext)

key_matrix = [
    [11, 2, 19],
    [5, 23, 25],
    [20, 7, 1]
]

plaintext = "LOT TRY CAT"

ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Зашифрований текст:", ciphertext)
