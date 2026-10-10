import itertools
import sys
from typing import Any


def read_input_file(file_name: str) -> tuple[dict[tuple[Any, Any], int], set[Any]]:
    with open(file_name) as f:
        content = f.read().splitlines()

    distances = dict()
    cities = set()

    for line in content:
        left, distance = line.split(' = ')
        city1, city2 = left.split(' to ')
        distances[(city1, city2)] = int(distance)
        distances[(city2, city1)] = int(distance)
        cities.add(city1)
        cities.add(city2)

    return distances, cities


def compute_part(file_name: str) -> tuple[int, int]:
    distances, cities = read_input_file(file_name)
    combinations = itertools.permutations(cities, len(cities))
    shortest_distance = sys.maxsize
    longest_distance = 0
    for combination in combinations:
        distance = 0
        for city1, city2 in zip(combination, combination[1:]):
            distance += distances[(city1, city2)]
        shortest_distance = min(distance, shortest_distance)
        longest_distance = max(distance, longest_distance)
    print(f'{shortest_distance= }')
    print(f'{longest_distance= }')

    return shortest_distance, longest_distance


if __name__ == '__main__':
    print(f"Part I & II: {compute_part('input/input9.txt')}")
