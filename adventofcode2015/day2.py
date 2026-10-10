import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    pattern = r'\d+'
    boxes = []
    for line in content:
        numbers = list(map(int, re.findall(pattern, line)))
        numbers.sort()
        boxes.append(numbers)

    return boxes


def calculate_paper_size(box: list) -> int:
    l, w, h = box  # box dimension is ordered, so l, w are the smallest

    area = 2 * l * w + 2 * l * h + 2 * h * w + l * w
    return area


def calculate_ribbon_size(box: list) -> int:
    l, w, h = box  # box dimension is ordered, so l, w are the smallest

    length = 2 * l + 2 * w + l * w * h
    return length


def compute_part_one(file_name: str) -> int:
    boxes = read_input_file(file_name)
    total_area = 0
    for box in boxes:
        area = calculate_paper_size(box)
        total_area += area

    return total_area


def compute_part_two(file_name: str) -> int:
    boxes = read_input_file(file_name)
    total_length = 0
    for box in boxes:
        length = calculate_ribbon_size(box)
        total_length += length

    return total_length




if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")
