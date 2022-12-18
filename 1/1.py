def encoder():
    with open('input.txt', "r", encoding="utf-8") as inp, open('output.txt', "w") as outp:
        while True:
            text = inp.readline()
            if len(text) == 0:
                break
            for simbol in text:
                outp.write(f'{ord(simbol)} ' if ord(simbol) != 10 else '')
            outp.write('\n')
    return 1


def decoder():
    with open('input.txt', "r") as inp, open('output.txt', "w", encoding="utf-8") as outp:
        while True:
            text = inp.readline().split()
            if len(text) == 0:
                break
            for num in text:
                try:
                    outp.write(f'{chr(int(num))}')
                except ValueError:
                    print('Невозможно декодировать!')
                    return 0
            outp.write('\n')
    return 1


try:
    choice = int(input('1 - Перевести текст из файла в список байт кодов\n2 - Перевести список байт кодов из файла в текст\n\nВаш выбор: '))
    if choice not in [1, 2]:
        print('Нет такого выбора!')
    else:
        if choice == 1:
            if encoder():
                print('Успешно!')
        elif choice == 2:
            if decoder():
                print('Успешно!')
except ValueError:
    print('Введите цифры!')
