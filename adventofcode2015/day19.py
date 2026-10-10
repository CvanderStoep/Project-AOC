import re
from collections import deque


def find_all_occurrences(s, sub):
    # Use the finditer method from the re module
    return [match.start() for match in re.finditer(re.escape(sub), s)]


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    replacements = content[0].splitlines()
    replacement_list = []
    for replacement in replacements:
        r1, r2 = replacement.split(' => ')
        replacement_list.append((r1, r2))

    replacements = replacement_list

    starting = content[1]

    return replacements, starting


def compute_part_one(file_name: str) -> int:
    replacements, starting_string = read_input_file(file_name)
    print(replacements, starting_string)

    new_molecules = set()
    for replacement in replacements:
        r1, r2 = replacement
        indices = find_all_occurrences(starting_string, r1)
        for i in indices:
            new_string = starting_string[:i] + r2 + starting_string[i + len(r1):]
            new_molecules.add(new_string)
    number_of_new_molecules = len(new_molecules)
    print(f'{number_of_new_molecules= }')

    return number_of_new_molecules


def compute_part_two(file_name: str) -> int:
    # this brute force solution is way too slow...
    replacements, starting_string = read_input_file(file_name)
    queue = deque()
    queue.append((0, 'e'))
    all_strings = set()
    while queue:
        n, s = queue.popleft()
        if s == starting_string:
            print(f'found it in {n} steps')
            return n

        for replacement in replacements:
            r1, r2 = replacement
            indices = find_all_occurrences(s, r1)
            for i in indices:
                new_string = s[:i] + r2 + s[i + len(r1):]
                if new_string not in all_strings:
                    all_strings.add(new_string)
                    queue.append((n + 1, new_string))

    return 42


def count_uppercase(s):
    count = 0
    for char in s:
        if char.isupper():
            count += 1
    return count


def compute_part_two_alter(file_name: str) -> int:
    replacements, starting_string = read_input_file(file_name)
    count_Y = starting_string.count("Y")
    count_Rn = starting_string.count("Rn")
    count_Ar = starting_string.count("Ar")
    count_symbols = count_uppercase(starting_string)

    # NumSymbols - #Rn - #Ar - 2 * #Y - 1
    # See the reddit suggestions
    solution = count_symbols - count_Rn - count_Ar - 2 * count_Y - 1

    print(f'{count_Y= }')
    print(f'{count_Ar= }')
    print(f'{count_Rn= }')
    print(f'{count_symbols= }')

    return solution


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input19.txt')}")
    # print(f"Part II: {compute_part_two('input/input19.txt')}")
    print(f"Part II: {compute_part_two_alter('input/input19.txt')}")
