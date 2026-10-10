def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_input(inputs: list) -> list:
    levels = []
    for line in inputs:
        line = list(map(int, line.split()))
        levels.append(line)

    return levels


def check_valid_list(level: list) -> bool:
    differences = [level[i] - level[i - 1] for i in range(1, len(level))]

    all_between_1_and_3 = all(1 <= x <= 3 for x in differences)
    all_between_minus1_and_minus3 = all(-3 <= x <= -1 for x in differences)

    return all_between_1_and_3 or all_between_minus1_and_minus3


def check_valid_list_extended(level: list) -> bool:
    for i in range(len(level)):
        level_subset = level[:]
        level_subset.pop(i)
        if check_valid_list(level_subset):
            return True

    return False


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    levels = process_input(inputs)

    amount_of_safe_reports = 0
    for level in levels:
        if check_valid_list(level):
            amount_of_safe_reports += 1
    return amount_of_safe_reports


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    levels = process_input(inputs)

    amount_of_safe_reports = 0
    for level in levels:
        if check_valid_list(level):
            amount_of_safe_reports += 1
        elif check_valid_list_extended(level):
            amount_of_safe_reports += 1
    return amount_of_safe_reports


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")
