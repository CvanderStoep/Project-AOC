import re
from collections import Counter


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def get_top_n_values(d: dict, n: int) -> list:
    # Sort the dictionary items first by value in descending order, then by key in ascending order
    sorted_items = sorted(d.items(), key=lambda item: (-item[1], item[0]))
    # Select the top n items
    return sorted_items[:n]


def caesar_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Non-letter characters are added as-is
    return ''.join(encrypted_text)


def count_letters(s: str) -> dict:
    # Use Counter to count occurrences of each letter
    letter_counts = Counter(s)
    # Filter out non-alphabetic characters
    letter_counts = {k: v for k, v in letter_counts.items() if k.isalpha()}
    return letter_counts

def parse_room(room):
    match = re.match(r'([a-z-]+)-(\d+)\[([a-z]+)\]', room)
    if match:
        encrypted_name, sector_id, checksum = match.groups()
        return encrypted_name.replace('-', ''), int(sector_id), checksum
    return None, None, None


def split_string(s):
    """
    input: aczupnetwp - mfyyj - opalcexpye - 977[peyac]
    output: aczupnetwp-mfyyj-opalcexpye-977, [peyac]
    """

    match = re.match(r'^(.*?)(\[\w+\])$', s)
    if match:
        part1 = match.group(1)
        part2 = match.group(2)
        return part1, part2
    else:
        return None, None


def is_real_room(room: str) -> tuple[int, bool]:
    """
    check if the room is valid, return both the ID and boolean value
    """
    encrypted_name, sector_id, checksum = parse_room(room)
    letter_count = count_letters(encrypted_name)
    top_n = get_top_n_values(letter_count, 5)
    for key, _ in top_n:
        if key not in checksum:
            return sector_id, False

    return sector_id, True


def compute_part_one(file_name: str) -> str:
    rooms = read_input_file(file_name)
    sum_id = 0
    for room in rooms:
        id, valid_room = is_real_room(room)
        if valid_room:
            sum_id += id

    return f'{sum_id= }'


def compute_part_two(file_name: str) -> str:
    rooms = read_input_file(file_name)
    for room in rooms:
        part1, _ = split_string(room)
        id = int(part1[-3:])
        encrypted = caesar_encrypt(part1, id)
        if 'pole' in encrypted:
            print(f'{encrypted= }')
            return f'{id= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input4.txt')}")
    print(f"Part II: {compute_part_two('input/input4.txt')}")
