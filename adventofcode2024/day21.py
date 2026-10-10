import re
from typing import List

import numpy as np


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def move_sequence_numerical(first: str, second: str) -> list[str]:
    numerical_keypad = {'A': (2, 3), '0': (1, 3),
                        '1': (0, 2), '2': (1, 2), '3': (2, 2),
                        '4': (0, 1), '5': (1, 1), '6': (2, 1),
                        '7': (0, 0), '8': (1, 0), '9': (2, 0)}

    x_direction = {1: '>', -1: '<'}
    y_direction = {1: 'v', -1: '^'}
    sort_order = [">", "^", "<", "v"]

    x1, y1 = numerical_keypad[first]
    x2, y2 = numerical_keypad[second]
    difference = (x2 - x1, y2 - y1)
    x, y = difference[0], difference[1]
    robot_arm = []
    if x != 0:
        for _ in range(abs(x)):
            robot_arm.append(x_direction[np.sign(x)])
    if y != 0:
        for _ in range(abs(y)):
            robot_arm.append(y_direction[np.sign(y)])

    robot_arm.sort(key=lambda val: sort_order.index(val))
    robot_arm.append('A')

    return robot_arm


def move_sequence_directional(first: str, second: str) -> list[str]:
    directional_keypad = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}

    x_direction = {1: '>', -1: '<'}
    y_direction = {1: 'v', -1: '^'}
    sort_order = ["v", ">", "<", "^"]

    x1, y1 = directional_keypad[first]
    x2, y2 = directional_keypad[second]
    difference = (x2 - x1, y2 - y1)
    x, y = difference[0], difference[1]
    robot_arm = []
    if x != 0:
        for _ in range(abs(x)):
            robot_arm.append(x_direction[np.sign(x)])
    if y != 0:
        for _ in range(abs(y)):
            robot_arm.append(y_direction[np.sign(y)])

    robot_arm.sort(key=lambda val: sort_order.index(val))
    robot_arm.append('A')

    return robot_arm


def compute_part_one(file_name: str) -> int:
    codes = read_input_file(file_name)
    pattern = r'\d+'
    print(codes)
    code_complexity = 0
    for code in codes:
        code = 'A' + code
        code_number = int(re.findall(pattern, code)[0])
        print(f'{code= }, {code_number= }')
        first_sequence = []
        for pos in range(len(code) - 1):
            first = code[pos]
            second = code[pos + 1]
            first_sequence += move_sequence_numerical(first, second)
        first_sequence = ''.join(first_sequence)
        print(f'{first_sequence= }')
        first_sequence = 'A' + first_sequence
        second_sequence = []
        for pos in range(len(first_sequence) - 1):
            first = first_sequence[pos]
            second = first_sequence[pos + 1]
            second_sequence += move_sequence_directional(first, second)
        second_sequence = ''.join(second_sequence)
        print(f'{second_sequence= }')
        second_sequence = 'A' + second_sequence
        third_sequence = []
        for pos in range(len(second_sequence) - 1):
            first = second_sequence[pos]
            second = second_sequence[pos + 1]
            third_sequence += move_sequence_directional(first, second)
        third_sequence = ''.join(third_sequence)
        print(f'{third_sequence= }')
        print(f'{len(third_sequence)= }')
        code_complexity += len(third_sequence) * code_number
    print(f'{code_complexity= }')

    return 1


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return 2


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input21.txt')}")
    print(f"Part II: {compute_part_two('input/input21.txt')}")
