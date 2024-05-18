# Função para criptografar o texto
def encrypt(text, password):
    encrypted_text = ""
    for i in range(len(text)):
        char_code = chr(ord(text[i]) + ord(password[i % 6]) - 48)
        encrypted_text += char_code
    return encrypted_text

# Função para descriptografar o texto
def decrypt(text, password):
    decrypted_text = ""
    for i in range(len(text)):
        char_code = chr(ord(text[i]) - ord(password[i % 6]) + 48)
        decrypted_text += char_code
    return decrypted_text

def main():
    choice = int(input())

    text = input().strip()
    password = input().strip()

    if choice == 1:
        encrypted_text = encrypt(text, password)
        print(encrypted_text)
    elif choice == 2:
        decrypted_text = decrypt(text, password)
        print(decrypted_text)

if __name__ == "__main__":
    main()

