from collections import Counter


def most_frequent_letter(s: str) -> str:
    letter_counts = Counter(s)
    most_frequent = max(letter_counts, key=letter_counts.get)
    return most_frequent


def least_frequent_letter(s: str) -> str:
    letter_counts = Counter(s)
    least_frequent = min(letter_counts, key=letter_counts.get)
    return least_frequent


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def compute_part_one(file_name: str) -> str:
    messages = read_input_file(file_name)
    print(messages)
    result = ''
    for pos in range(len(messages[0])):
        vertical = ''
        for message in messages:
            vertical = vertical + message[pos]
        result = result + most_frequent_letter(vertical)

    return f'{result= }'


def compute_part_two(file_name: str) -> str:
    messages = read_input_file(file_name)
    result = ''
    for pos in range(len(messages[0])):
        vertical = ''
        for message in messages:
            vertical = vertical + message[pos]
        result = result + least_frequent_letter(vertical)

    return f'{result= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input6.txt')}")
    print(f"Part II: {compute_part_two('input/input6.txt')}")
