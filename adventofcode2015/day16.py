from dataclasses import dataclass
import re


@dataclass
class Aunt:
    number: int = 0
    children: int = None
    cats: int = None
    samoyeds: int = None
    pomeranians: int = None
    akitas: int = None
    vizslas: int = None
    goldfish: int = None
    trees: int = None
    cars: int = None
    perfumes: int = None


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    aunts = []
    for line in content:
        parts = line.split()
        number = int(parts[1][:-1])
        compound1 = parts[2][:-1]
        compound1_amount = int(parts[3][:-1])
        compound2 = parts[4][:-1]
        compound2_amount = int(parts[5][:-1])
        compound3 = parts[6][:-1]
        compound3_amount = int(parts[7])

        aunt = Aunt(number)
        setattr(aunt, compound1, compound1_amount)
        setattr(aunt, compound2, compound2_amount)
        setattr(aunt, compound3, compound3_amount)
        aunts.append(aunt)

    return aunts


# for aunt in aunts:
#     properties = [
#         (aunt.children, 3),
#         (aunt.cats, 7),
#         (aunt.samoyeds, 2),
#         (aunt.pomeranians, 3),
#         (aunt.akitas, 0),
#         (aunt.vizslas, 0),
#         (aunt.goldfish, 5),
#         (aunt.trees, 3),
#         (aunt.cars, 2),
#         (aunt.perfumes, 1)
#     ]
#
#     if all(prop is None or prop == value for prop, value in properties):
#         print(aunt.number)


def compute_part_one(file_name: str) -> int:
    aunts = read_input_file(file_name)
    print(aunts)
    for aunt in aunts:
        if (aunt.children == 3 or aunt.children is None) and \
                (aunt.cats == 7 or aunt.cats is None) and \
                (aunt.samoyeds == 2 or aunt.samoyeds is None) and \
                (aunt.pomeranians == 3 or aunt.pomeranians is None) and \
                (aunt.akitas == 0 or aunt.akitas is None) and \
                (aunt.vizslas == 0 or aunt.vizslas is None) and \
                (aunt.goldfish == 5 or aunt.goldfish is None) and \
                (aunt.trees == 3 or aunt.trees is None) and \
                (aunt.cars == 2 or aunt.cars is None) and \
                (aunt.perfumes == 1 or aunt.perfumes is None):
            return aunt.number

    return "no solution found"


def compute_part_two(file_name: str) -> int:
    aunts = read_input_file(file_name)
    print(aunts)
    for aunt in aunts:
        if (aunt.children == 3 or aunt.children is None) and \
                (aunt.cats is None or aunt.cats > 7) and \
                (aunt.samoyeds == 2 or aunt.samoyeds is None) and \
                (aunt.pomeranians is None or aunt.pomeranians < 3) and \
                (aunt.akitas == 0 or aunt.akitas is None) and \
                (aunt.vizslas == 0 or aunt.vizslas is None) and \
                (aunt.goldfish is None or aunt.goldfish < 5) and \
                (aunt.trees is None or aunt.trees > 3) and \
                (aunt.cars == 2 or aunt.cars is None) and \
                (aunt.perfumes == 1 or aunt.perfumes is None):
            return aunt.number

    return "no solution found"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input16.txt')}")
    print(f"Part II: {compute_part_two('input/input16.txt')}")
