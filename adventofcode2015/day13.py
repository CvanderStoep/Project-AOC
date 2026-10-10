import itertools
from typing import Any


def read_input_file(file_name: str) -> tuple[dict[tuple[Any, Any], int], list[Any]]:
    happiness = dict()
    persons = set()

    with open(file_name) as f:
        for line in f:
            p1, _, effect, n, *_, p2 = line.split()
            persons.add(p1)
            n = int(n)
            if effect == 'lose':
                n = -n
            happiness[(p1, p2[:-1])] = n

    return happiness, list(persons)


def compute_part_one(file_name: str) -> int:
    happiness_table, persons_list = read_input_file(file_name)
    permutations = itertools.permutations(persons_list)
    number_of_persons = len(persons_list)
    maximum_happiness = 0
    for persons in permutations:
        happiness = 0
        for position in range(number_of_persons):
            person = persons[position]
            neighbour1 = persons[(position - 1) % number_of_persons]
            neighbour2 = persons[(position + 1) % number_of_persons]
            happiness += happiness_table[(person, neighbour1)]
            happiness += happiness_table[(person, neighbour2)]
        maximum_happiness = max(maximum_happiness, happiness)
    print(f'{maximum_happiness= }')

    return maximum_happiness


def compute_part_two(file_name: str) -> int:
    # same question as part I, but add myself to the list.
    happiness_table, persons_list = read_input_file(file_name)
    for person in persons_list:
        happiness_table[('Carlo', person)] = 0
        happiness_table[(person, 'Carlo')] = 0
    persons_list.append('Carlo')
    permutations = itertools.permutations(persons_list)
    number_of_persons = len(persons_list)
    maximum_happiness = 0
    for persons in permutations:
        happiness = 0
        for position in range(number_of_persons):
            person = persons[position]
            neighbour1 = persons[(position - 1) % number_of_persons]
            neighbour2 = persons[(position + 1) % number_of_persons]
            happiness += happiness_table[(person, neighbour1)]
            happiness += happiness_table[(person, neighbour2)]
        maximum_happiness = max(maximum_happiness, happiness)
    print(f'{maximum_happiness= }')

    return maximum_happiness


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input13.txt')}")
    print(f"Part II: {compute_part_two('input/input13.txt')}")
