from typing import Any


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def process_stream(stream: str) -> tuple[int | Any, int | Any]:
    total_score = 0
    open_brackets = 0
    garbage = False
    garbage_count = 0
    position = 0

    while position < len(stream):
        char = stream[position]
        if char == "!":
            position += 2
            continue
        if char == "<" and not garbage:
            garbage = True
        elif char == ">" and garbage:
            garbage = False
        elif char == '{' and not garbage:
            open_brackets += 1
        elif char == '}' and not garbage:
            total_score += open_brackets
            open_brackets -= 1
        elif garbage:
                garbage_count += 1

        position += 1
    return total_score, garbage_count

def compute_part_one(file_name: str) -> str:
    stream = read_input_file(file_name)[0]
    score, garbage_count = process_stream(stream)

    return f'{score= }, {garbage_count= }'



if __name__ == '__main__':
    file_path = 'input/input9.txt'
    print(f"Part I & II: {compute_part_one(file_path)}")
