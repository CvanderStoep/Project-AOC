import re

import numpy as np


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    prizes = []
    for line in content:
        prize = line.splitlines()
        prizes.append(prize)

    return prizes


def process_input(prize):
    # ButtonA: X + 94, Y + 34   -> (a1 = 94, a2 = 34)
    # ButtonB: X + 22, Y + 67   -> (b1 = 22, b2 = 67)
    # Prize: X = 8400, Y = 5400 -> (c1 = 8400, c2 = 5400)

    pattern = r'\d+'
    button_a, button_b, value = prize[0], prize[1], prize[2]
    a1, a2 = map(int, re.findall(pattern, button_a))
    b1, b2 = map(int, re.findall(pattern, button_b))
    c1, c2 = map(int, re.findall(pattern, value))

    return a1, a2, b1, b2, c1, c2


def solve_equation(a1, a2, b1, b2, c1, c2) -> (int, int):
    # (a1 b1)  (A)  (c1)
    # (a2 b2)  (B)  (c2)

    A = np.array([[a1, b1], [a2, b2]])
    C = np.array([c1, c2])
    solution = np.linalg.solve(A, C)
    return solution


def compute_part_one(file_name: str) -> int:
    prizes = read_input_file(file_name)
    total_tokens = 0
    for prize in prizes:
        a1, a2, b1, b2, c1, c2 = process_input(prize)
        solution = solve_equation(a1, a2, b1, b2, c1, c2)
        A, B = solution
        eps = 0.0001
        # check for integer solutions
        if (abs(A - round(A)) < eps) and (abs(B - round(B)) < eps):
            A = round(A)
            B = round(B)
            if A > 100 or B > 100:
                print('too much pushes')
            total_tokens = total_tokens + 3 * A + B
    print(f'{total_tokens= }')

    return 1


def compute_part_two(file_name: str) -> int:
    prizes = read_input_file(file_name)
    total_tokens = 0
    for prize in prizes:
        a1, a2, b1, b2, c1, c2 = process_input(prize)
        c1 += 10000000000000
        c2 += 10000000000000
        solution = solve_equation(a1, a2, b1, b2, c1, c2)
        A, B = solution
        eps = 0.0001
        # check for integer solutions
        if (abs(A - round(A)) < eps) and (abs(B - round(B)) < eps):
            A = round(A)
            B = round(B)
            total_tokens = total_tokens + 3 * A + B
    print(f'{total_tokens= }')

    return 1


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input13.txt')}")
    print(f"Part II: {compute_part_two('input/input13.txt')}")
