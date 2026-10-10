import math
import itertools


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def tuple_difference(tuple1, tuple2):
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]


def tuple_addition(tuple1, tuple2, step=1):
    return tuple1[0] + step * tuple2[0], tuple1[1] + step * tuple2[1]


def calculate_antinodes(antenna1, antenna2) -> list:
    difference = tuple_difference(antenna2, antenna1)
    antinodes = []
    antinode1 = tuple_addition(antenna2, difference)
    antinode2 = tuple_difference(antenna1, difference)

    antinodes.append(antinode1)
    antinodes.append(antinode2)
    return antinodes


def calculate_antinodes_part_two(antenna1, antenna2, grid) -> list:
    difference = tuple_difference(antenna2, antenna1)
    gcd_ = math.gcd(difference[0], difference[1])  # reduce for example vector (4,2) to (2,1)
    difference = (int(difference[0] / gcd_), int(difference[1] / gcd_))
    antinodes = [antenna1, antenna2]
    step = 1
    while True:
        antinode = tuple_addition(antenna1, difference, step)
        if within_bounds(antinode, grid):
            antinodes.append(antinode)
        else:
            break
        step += 1

    step = -1
    while True:
        antinode = tuple_addition(antenna1, difference, step)
        if within_bounds(antinode, grid):
            antinodes.append(antinode)
        else:
            break
        step -= 1

    return antinodes


def within_bounds(antinode, grid) -> bool:
    size = len(grid)
    if 0 <= antinode[0] < size and 0 <= antinode[1] < size:
        return True
    else:
        return False


def process_input(grid: list) -> dict:
    antennas = dict()
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element != '.':
                if element in antennas:
                    value = antennas[element]
                    value.append((i, j))
                    antennas[element] = value
                else:
                    antennas[element] = [(i, j)]
    return antennas


def generate_combinations(lst):
    return list(itertools.combinations(lst, 2))


def clean_antinodes(antinodes, grid) -> set:
    size = len(grid)
    clean_set = set()
    for antinode in antinodes:
        # if 0 <= antinode[0] < size and 0 <= antinode[1] < size:
        if within_bounds(antinode, grid):
            clean_set.add(antinode)

    return clean_set


def compute_part_one(file_name: str) -> int:
    grid = read_input_file(file_name)
    antennas = process_input(grid)
    antinodes = set()
    for antenna, locations in antennas.items():
        combinations = generate_combinations(locations)
        for antenna1, antenna2 in combinations:
            antinode1, antinode2 = calculate_antinodes(antenna1, antenna2)
            antinodes.add(antinode1)
            antinodes.add(antinode2)

    antinodes = clean_antinodes(antinodes, grid)
    return len(antinodes)


def compute_part_two(file_name: str) -> int:
    grid = read_input_file(file_name)
    antennas = process_input(grid)
    antinodes = set()
    for antenna, locations in antennas.items():
        combinations = generate_combinations(locations)
        for antenna1, antenna2 in combinations:

            antinode_list = calculate_antinodes_part_two(antenna1, antenna2, grid)
            for antinode in antinode_list:
                antinodes.add(antinode)

    antinodes = clean_antinodes(antinodes, grid)
    return len(antinodes)


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input8.txt')}")
    print(f"Part II: {compute_part_two('input/input8.txt')}")
