def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary


def xor_with_key(text_binary, key_binary):
    result = ''
    for i in range(len(text_binary)):
        result += str(int(text_binary[i]) ^ int(key_binary[i % len(key_binary)]))
    return result


def main():
    plaintext = "JOB"
    key = "000000100111111000010110"

    plaintext_binary = text_to_binary(plaintext)
    key_binary = key

    ciphertext_binary = xor_with_key(plaintext_binary, key_binary)

    print("Відкритий текст у двійковому вигляді:", plaintext_binary)
    print("Ключова гама у двійковому вигляді:", key_binary)
    print("Зашифрований текст у двійковому вигляді:", ciphertext_binary)


if __name__ == "__main__":
    main()
