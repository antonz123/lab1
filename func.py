CSI = '\x1B['
RESET = f'{CSI}0m'


def print_graph(width, num):
    print(
        f'{" " * (2 - len(str(num)))}{num} |{CSI}47m{" " * width}'
        f'{CSI}42m{" "}{CSI}47m{" " * (20 - width)}{RESET}'
    )


def paint(width, num):
    for i in range(1, 12):
        print_graph(width, num)
        width -= 1
        num -= 1
    print('    0 1 2 3 4 5')


if __name__ == '__main__':
    width = 10
    num = 10
    paint(width, num)
