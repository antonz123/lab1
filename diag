with open('sequence.txt', 'r', encoding='utf-8') as f:
    a = [float(i) for i in f]

CSI = '\x1B['
RESET = f'{CSI}0m'


def column(num, gr2):
    print(f'{' '*(3-len(str(num)))}{num}|    {CSI}47m  {RESET}    {CSI}47m{"  " * gr2}{RESET}')


chet = sum(abs(a[i]) for i in range(0, len(a), 2))
nechet = sum(abs(a[i]) for i in range(1, len(a), 2))
gr2_num = nechet * 100 // chet


def paint():
    num = 100
    gr2 = 0
    for i in range(21):
        if num <= gr2_num:
            gr2 = 1
        column(num, gr2)
        num -= 5
    print('         Чёт  Нечёт')


if __name__ == '__main__':
    paint()
