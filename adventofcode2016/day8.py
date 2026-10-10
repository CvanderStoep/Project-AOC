import re
import numpy as np


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_operation(screen, operation):
    a, b = re.findall(r'\d+', operation)
    a = int(a)
    b = int(b)
    if 'rect' in operation:
        for r in range(b):
            for c in range(a):
                screen[r, c] = 1
    if 'column' in operation:
        shift = b
        screen[:, a] = np.roll(screen[:, a], shift)
    if 'row' in operation:
        shift = b
        screen[a, :] = np.roll(screen[a, :], shift)

    return screen


def display_screen(screen) -> None:
    rows, cols = screen.shape
    for i in range(rows):
        for j in range(cols):
            if screen[i, j] == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()


def compute_part_one(file_name: str) -> str:
    screen = np.zeros((6, 50), dtype=int)

    operations = read_input_file(file_name)
    print(operations)
    for operation in operations:
        screen = process_operation(screen, operation)

    total_sum = int(np.sum(screen))
    print('Part II:')
    display_screen(screen)

    return f'{total_sum= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input8.txt')}")
