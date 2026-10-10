def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def is_safe(row: str, position: int) -> bool:
    if position < 0 or position >= len(row):
        return True
    if row[position] == '.':
        return True
    return False


def process_rules(row: str, position: int) -> str:
    left = is_safe(row, position - 1)
    center = is_safe(row, position)
    right = is_safe(row, position + 1)

    if not left and not center and right:
        return '^'
    if not center and not right and left:
        return '^'
    if not left and right and center:
        return '^'
    if not right and left and center:
        return '^'
    return '.'


def compute_part(file_name: str, rows: int) -> str:
    content = read_input_file(file_name)
    print(content)
    total_count = content.count('.')
    for i in range(rows-1):
        next_line = ''
        for pos, _ in enumerate(content):
            next_line += process_rules(content, pos)
        content = next_line
        total_count += content.count('.')

    return f'{total_count= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input18.txt', rows=40)}")
    print(f"Part I: {compute_part('input/input18.txt', rows=400000)}")
