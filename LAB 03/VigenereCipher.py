# Constants for the ASCII values of 'A' and 'Z', representing the upper case letters range.
A = 65
Z = 90
a = 97
z = 122


def custom_mod(x, n1, n2):
    return ((x - n1) % (n2 - n1 + 1)) + n1


def vigenere_cipher(text, key, mode='encrypt'):
    result = ""
    key_length = len(key)
    key_index = 0

    for char in text:
        # Get the next key index
        key_index = key_index % key_length
        # Get the letter at that index
        k = key[key_index]
        # compute the shift amount
        shift = ord(k.lower()) - ord('a')
        if mode == 'decrypt':
            shift = -shift

        enc_char = ord(char) + shift
        if char.isupper():
            result += chr(custom_mod(enc_char, A, Z))
            key_index += 1
        elif char.islower():
            result += chr(custom_mod(enc_char, a, z))
            key_index += 1
        else:
            result += char  # Non-alphabetic characters remain unchanged

    return result


plaintext = "I LOVE CRYPTO so much"
keyword = "BAD"
encrypted_text = vigenere_cipher(plaintext, keyword, mode='encrypt')
print(f"Encrypted: {encrypted_text}")

decrypted_text = vigenere_cipher(encrypted_text, keyword, mode='decrypt')
print(f"Decrypted: {decrypted_text}")
