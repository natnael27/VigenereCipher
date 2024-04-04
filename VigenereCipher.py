def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                cipher_text += chr((ord(char) + shift - ord('A')) % 26 + ord('A'))
            else:
                cipher_text += chr((ord(char) + shift - ord('a')) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            cipher_text += char

    return cipher_text

def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    key = key.upper()
    key_index = 0

    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if char.isupper():
                plain_text += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            else:
                plain_text += chr((ord(char) - shift - ord('a')) % 26 + ord('a'))
            key_index = (key_index + 1) % len(key)
        else:
            plain_text += char

    return plain_text

# Example usage:
plaintext = "NATNAEL"
key = "SECRETKEY"

cipher_text = vigenere_encrypt(plaintext, key)
print("Original Text:", plaintext)
print("Encrypted Text:", cipher_text)

decrypted_text = vigenere_decrypt(cipher_text, key)
print("Decrypted Text:", decrypted_text)
