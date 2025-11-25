import math


with open('sequence.txt', 'r', encoding='utf-8') as f:
    numbers = [float(line) for line in f]

CSI = '\x1B['
RESET = f'{CSI}0m'


def print_column(num, gr2):
    print(f'{" " * (3 - len(str(num)))}{num}|    {CSI}47m  {RESET}    '
          f'{CSI}47m{"  " * gr2}{RESET}')


even_sum = sum(abs(numbers[i]) for i in range(0, len(numbers), 2))
odd_sum = sum(abs(numbers[i]) for i in range(1, len(numbers), 2))
gr2_num = odd_sum * 100 // even_sum


def paint():
    num = 100
    gr2 = 0
    for i in range(21):
        if num <= gr2_num:
            gr2 = 1
        print_column(num, gr2)
        num -= 5
    print('         Чёт  Нечёт')


if __name__ == '__main__':
    paint()
