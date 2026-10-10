from collections import defaultdict

import sympy


def read_input_file(file_name: str) -> int:
    with open(file_name) as f:
        content = f.read().splitlines()

    return int(content[0])


def compute_part_one(file_name: str) -> int:
    required_presents = read_input_file(file_name)
    print(required_presents)

    house = 1
    while True:
        presents = sum(sympy.divisors(house)) * 10
        if house % 100000 == 0:
            print(house, presents)
        if presents >= required_presents:
            print(f'{house= }')
            break
        house += 1

    return house


def compute_part_two(file_name: str) -> int:
    required_presents = read_input_file(file_name)
    print(required_presents)
    elf_visits = defaultdict(int)

    house = 1
    while True:
        divisors = sympy.divisors(house)
        for elf in divisors:
            elf_visits[elf] += 1
        # elves with less than 50 houses
        valid_elves = [elf for elf in divisors if elf_visits[elf] <= 50]
        if house % 100000 == 0:
            print(house, valid_elves)
        presents = sum(valid_elves) * 11
        if presents >= required_presents:
            print(f'{house= }')
            break
        house += 1

    return house


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input20.txt')}")
    print(f"Part II: {compute_part_two('input/input20.txt')}")
