def encrypt():
    with open('3/input.txt', 'r', encoding='utf-8') as inp:
        text = inp.read().split()
    msg = text[0]
    key = text[1]

    encrypt_text = ''
    i = 0
    for i in range(len(msg)):
        temp = ord(msg[i]) ^ ord(key[i])
        encrypt_text += f'{temp} '
        i += 1
        if i >= len(key):
            i = 0

    with open('3/output.txt', 'w', encoding='utf-8') as outp:
        outp.write(f'Зашифрованный текст: "{encrypt_text}"')


def decrypt():
    with open('3/input.txt', 'r', encoding='utf-8') as inp:
        text = inp.read().split('\n')
    msg = text[0].split()
    key = text[1]

    decrypt_text = ''
    i = 0
    for i in range(len(msg)):
        temp = int(msg[i]) ^ ord(key[i])
        decrypt_text += chr(temp)
        i += 1
        if i >= len(key):
            i = 0

    with open('3/output.txt', 'w', encoding='utf-8') as outp:
        outp.write(f'Расшифрованный текст: "{decrypt_text}"')

try:
    choice = int(input("1. Зашифровать\n2. Расшифровать\nВаш выбор: "))
    if choice == 1:
        encrypt()
    elif choice == 2:
        decrypt()
    else:
        print("Такого выбора нет!")
except ValueError:
    print('Введите число!')
