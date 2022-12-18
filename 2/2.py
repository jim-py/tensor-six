with open('input.txt', "r") as inp, open('output.txt', "w", encoding="utf-8") as outp:
    c, h, o = map(int, inp.readline().split())
    outp.write(f'Максимум {int(min(c / 2, h / 6, o))} молекул спирта.')
