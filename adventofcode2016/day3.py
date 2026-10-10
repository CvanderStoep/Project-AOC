import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return [list(map(int, re.findall(r'\d+', line))) for line in f]

    # triplets = []
    # for line in content:
    #     triplet = re.findall(f'\d+', line)
    #     triplet = list(map(int, triplet))
    #     triplets.append(triplet)
    #
    # return triplets


def check_valid_triangle(a, b, c) -> bool:
    if a + b <= c:
        return False
    if a + c <= b:
        return False
    if b + c <= a:
        return False
    return True

    # alternative
    # return a + b > c and a + c > b and b + c > a


def compute_part_one(file_name: str) -> str:
    triplets = read_input_file(file_name)
    print(triplets)
    valid_triplets = 0
    for triplet in triplets:
        a, b, c = triplet
        if check_valid_triangle(a, b, c):
            valid_triplets += 1

    return f'{valid_triplets= }'


def compute_part_two(file_name: str) -> str:
    triplets = read_input_file(file_name)
    valid_triplets = 0
    for i in range(0, len(triplets), 3):
        for j in range(3):
            a = triplets[i][j]
            b = triplets[i + 1][j]
            c = triplets[i + 2][j]
            if check_valid_triangle(a, b, c):
                valid_triplets += 1
    return f'{valid_triplets= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input3.txt')}")
    print(f"Part II: {compute_part_two('input/input3.txt')}")
