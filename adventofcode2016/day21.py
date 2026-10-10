import itertools
import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
        # return f.read().strip()
    # content = list(map(int, content))

    return content


def swap_chars(string, x, y):
    string_list = list(string)
    string_list[x], string_list[y] = string_list[y], string_list[x]
    return ''.join(string_list)


def swap_letters(string, letter1, letter2):
    if letter1 in string and letter2 in string:
        string = string.replace(letter1, '#').replace(letter2, letter1).replace('#', letter2)
    return string


def rotate_left(string, steps):
    # Ensure the steps value is within the range of the string length
    steps = steps % len(string)
    # Rotate the string to the left
    return string[steps:] + string[:steps]


def rotate_right(string, steps):
    # Ensure the steps value is within the range of the string length
    steps = steps % len(string)
    # Rotate the string to the right
    return string[-steps:] + string[:-steps]


def reverse_substring(string, i, j):
    # Ensure the indices are within the valid range
    if 0 <= i <= j < len(string):
        # Reverse the substring from index i to j
        return string[:i] + string[i:j + 1][::-1] + string[j + 1:]
    else:
        return "Invalid indices"


def move_char(string, i, j):
    string_list = list(string)
    char = string_list.pop(i)
    string_list.insert(j, char)
    return ''.join(string_list)


def process_operation(operation: str, start: str) -> str:
    digits = f'(\d+)'
    if operation.startswith('swap'):
        if 'position' in operation:
            p1, p2 = map(int, re.findall(digits, operation))
            start = swap_chars(start, p1, p2)
        if 'letter' in operation:
            _, _, p1, _, _, p2 = operation.split()
            start = swap_letters(start, p1, p2)
    elif operation.startswith('rotate'):
        if 'left' in operation:
            p1 = int(re.findall(digits, operation)[0])
            start = rotate_left(start, p1)
        if 'right' in operation:
            p1 = int(re.findall(digits, operation)[0])
            start = rotate_right(start, p1)
        if 'based' in operation:
            p1 = operation.split()[-1]
            i1 = start.find(p1)
            p1 = 1 + i1 if i1 < 4 else 2 + i1
            start = rotate_right(start, p1)
    elif operation.startswith('reverse'):
        p1, p2 = map(int, re.findall(digits, operation))
        start = reverse_substring(start, p1, p2)
    elif operation.startswith('move'):
        p1, p2 = map(int, re.findall(digits, operation))
        start = move_char(start, p1, p2)
    else:
        print('invalid operation')

    return start


def compute_part_one(file_name: str) -> str:
    operations = read_input_file(file_name)
    print(operations)
    start = 'abcdefgh'
    for operation in operations:
        start = process_operation(operation, start)

    return f'{start= }'


def compute_part_two(file_name: str) -> str:
    operations = read_input_file(file_name)
    start = 'abcdefgh'
    password = 'fbgdceah'
    permutations = itertools.permutations(start)

    for perm in permutations:
        start = ''.join(perm)
        for operation in operations:
            start = process_operation(operation, start)
        if start == password:
            perm = ''.join(perm)
            return f'{perm= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input21.txt')}")
    print(f"Part II: {compute_part_two('input/input21.txt')}")
