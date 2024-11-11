def caesar_cipher(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - 96) % 26 + 97)
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - 64) % 26 + 65)
        else:
            result += char
    return result

text = input("Skriv text att chiffrera: ")
print("Chiffrerad text:", caesar_cipher(text))

text = input("Skriv ett annat ord:")
print("Chiffrerad text:", caesar_cipher(text))