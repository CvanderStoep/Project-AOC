import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def yield_aba(part: str) -> str:
    for i in range(len(part) - 2):
        l1 = part[i]
        l2 = part[i + 1]
        l3 = part[i + 2]
        if l1 == l3 and l1 != l2:
            yield part[i:i + 3]


def has_corresponding_bab(aba: str, inside_parts: list) -> bool:
    bab = aba[1] + aba[0] + aba[1]
    return any(bab in part for part in inside_parts)


def is_abba(part: str) -> bool:
    for i in range(len(part) - 3):
        l1 = part[i]
        l2 = part[i + 1]
        l3 = part[i + 2]
        l4 = part[i + 3]
        if l1 == l4 and l2 == l3 and l1 != l2:
            return True

    return False


def split_and_label_string(s) -> list:
    # Use regular expression to find parts inside and outside square brackets
    parts = re.split(r'(\[[^\]]+\])', s)
    labeled_parts = []
    for part in parts:
        if part.startswith('[') and part.endswith(']'):
            labeled_parts.append(('inside_brackets', part[1:-1]))
        else:
            labeled_parts.append(('outside_brackets', part))
    return labeled_parts


def is_valid_tls_address(address: str) -> bool:
    parts = split_and_label_string(address)
    has_abba_outside = False

    for part_type, part_content in parts:
        if part_type == 'inside_brackets' and is_abba(part_content):
            return False  # Invalid address if ABBA pattern is found inside brackets
        if part_type == 'outside_brackets' and is_abba(part_content):
            has_abba_outside = True

    return has_abba_outside


def is_valid_ssl_address(address: str) -> bool:
    parts = split_and_label_string(address)
    outside_parts = [part_content for part_type, part_content in parts if part_type == 'outside_brackets']
    inside_parts = [part_content for part_type, part_content in parts if part_type == 'inside_brackets']

    for outside_part in outside_parts:
        for aba in yield_aba(outside_part):
            if has_corresponding_bab(aba, inside_parts):
                return True

    return False


def compute_part_one(file_name: str) -> str:
    addresses = read_input_file(file_name)
    number_valid_addresses = 0
    for address in addresses:
        if is_valid_tls_address(address):
            number_valid_addresses += 1

    return f'{number_valid_addresses= }'


def compute_part_two(file_name: str) -> str:
    addresses = read_input_file(file_name)
    number_valid_addresses = 0
    for address in addresses:
        if is_valid_ssl_address(address):
            number_valid_addresses += 1

    return f'{number_valid_addresses= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input7.txt')}")
    print(f"Part II: {compute_part_two('input/input7.txt')}")
