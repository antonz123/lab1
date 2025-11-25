CSI = '\x1B['
RESET = f'{CSI}0m'


def draw_row(offset, gap, paint_width, offset2):
    line = f'{CSI}47m{" " * offset}'
    for i in range(5):
        line += (
            f'{CSI}40m{" " * paint_width}'
            f'{CSI}47m{" " * gap}'
            f'{CSI}40m{" " * paint_width}'
            f'{CSI}47m{" " * offset2}'
        )
    line += (
        f'{CSI}40m{" " * paint_width}'
        f'{CSI}47m{" " * gap}'
        f'{CSI}40m{" " * paint_width}'
        f'{CSI}47m{" " * offset}{RESET}'
    )
    print(line)


def paint_pattern():
    offset = 16
    gap = 12
    paint_width = 4
    offset2 = 0
    shrinking = True

    for i in range(7):
        if gap <= 0:
            shrinking = False

        draw_row(offset, gap, paint_width, offset2)
        draw_row(offset, gap, paint_width, offset2)

        if not shrinking:
            offset -= 2
            gap += 4
            offset2 -= 4
        else:
            offset += 2
            gap -= 4
            offset2 += 4


if __name__ == '__main__':
    paint_pattern()
