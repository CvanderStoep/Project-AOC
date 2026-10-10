def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return [(int(b), int(e)) for b, e in (line.split('-') for line in f)]


def find_lowest_ip(lines: list) -> int:
    begin_interval, end_interval = lines[0]
    for (b, e) in lines:
        if b - 1 <= end_interval:
            end_interval = max(end_interval, e)
        else:
            lowest_ip = end_interval + 1
            return lowest_ip


def find_allowed_ip(lines: list) -> int:
    begin_interval, end_interval = lines[0]
    total_allowed_ip = 0
    max_ip = 2**32 - 1
    for index, (b, e) in enumerate(lines):
        if b - 1 <= end_interval:
            end_interval = max(end_interval, e)
        else:
            lowest_ip = end_interval + 1
            valid_range = b - lowest_ip
            total_allowed_ip += valid_range
            end_interval = max(end_interval, e)

    return total_allowed_ip + max_ip - end_interval


def compute_part_one(file_name: str) -> str:
    lines = read_input_file(file_name)
    lines = sorted(lines)
    lowest_ip = find_lowest_ip(lines)

    return f'{lowest_ip= }'


def compute_part_two(file_name: str) -> str:
    lines = read_input_file(file_name)
    lines = sorted(lines)
    total_allowed_ip = find_allowed_ip(lines)

    return f'{total_allowed_ip= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input20.txt')}")
    print(f"Part II: {compute_part_two('input/input20.txt')}")
