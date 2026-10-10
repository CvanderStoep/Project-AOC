# https://github.com/godarderik/adventofcode/blob/master/2015/problem2.py
import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    pattern = r'\d+'
    row, column = re.findall(pattern, content[0])

    # content = list(map(int, content))

    return int(row), int(column)


def find_number(r, c):
    return (r + c - 2) * (r + c - 1) // 2 + c


def generate_next_code(code: int) -> int:
    code = (code * 252533) % 33554393
    return code


def compute_part_one(file_name: str) -> int:
    row, column = read_input_file(file_name)
    print(row, column)
    code = 20151125
    number = find_number(row, column)
    print(f"The number at row {row} and column {column} is {number}")
    for i in range(2, number + 1):
        code = generate_next_code(code)
    print(f'{i= } {code= }')

    return code


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return "part 2 not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input25.txt')}")
    # print(f"Part II: {compute_part_two('input/input25.txt')}")
