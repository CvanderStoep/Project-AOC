import json
import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read()  # .splitlines()

    return content


def read_input_file_json(file_name: str) -> list:
    with open(file_name) as f:
        content = json.load(f)

    return content


def recursive_sum(data):
    total = 0
    if isinstance(data, dict):
        if "red" in data.values():
            pass
        else:
            for value in data.values():
                total += recursive_sum(value)
    elif isinstance(data, list):
        for item in data:
            total += recursive_sum(item)
    elif isinstance(data, (int, float)):  # Check for numeric values
        total += data
    return total


def compute_part_one(file_name: str) -> int:
    pattern = r'-?\d+'  # pattern for positive and negative integers
    content = read_input_file(file_name)
    numbers = list(map(int, re.findall(pattern, content)))
    print(f'{sum(numbers)= }')

    return sum(numbers)


def compute_part_two(file_name: str) -> int:
    content = read_input_file_json(file_name)
    # content = eval(read_input_file(file_name))  # alternative read without needing json module

    sum_of_numbers_without_red = recursive_sum(content)
    print(f'{sum_of_numbers_without_red= }')

    return sum_of_numbers_without_red


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input12.txt')}")
    print(f"Part II: {compute_part_two('input/input12.txt')}")
