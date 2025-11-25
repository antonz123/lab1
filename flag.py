CSI = '\x1B['
RESET = f'{CSI}0m'


def print_flag_stripe(color):
    print(f'{CSI}{color}m{" " * 50}{RESET}')
    print(f'{CSI}{color}m{" " * 50}{RESET}')


COLORS = [41, 47, 44]


def flag():
    for color in COLORS:
        print_flag_stripe(color)


if __name__ == '__main__':
    flag()
