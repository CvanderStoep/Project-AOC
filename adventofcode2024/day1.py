def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_input(inputs: list) -> (list, list):
    left, right = zip(*(map(int, line.split()) for line in inputs))
    return list(left), list(right)


# def process_input(inputs: list) -> (list, list):
#     left = []
#     right = []
#     for line in inputs:
#         left_number, right_number = map(int, line.split())
#         left.append(left_number)
#         right.append(right_number)
#
#     return left, right


def calc_distance(left: list, right: list) -> int:
    left.sort()
    right.sort()

    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)

    return distance


def calc_similarity(left: list, right: list) -> int:
    score = 0
    for l in left:
        score += l * right.count(l)

    return score


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    left_list, right_list = process_input(inputs)
    return calc_distance(left_list, right_list)


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    left_list, right_list = process_input(inputs)
    return calc_similarity(left_list, right_list)


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input1.txt')}")
    print(f"Part II: {compute_part_two('input/input1.txt')}")

