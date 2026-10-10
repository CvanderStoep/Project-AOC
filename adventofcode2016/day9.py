import re


def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content[0]


def decompress_string(content: str) -> str:
    if '(' not in content:
        return content

    components = re.split(r'(\(.*?\))', content, maxsplit=1)
    part1 = components[0]
    a, b = re.findall(r'(\d+)', components[1])
    a, b = int(a), int(b)
    part2 = components[2]
    repeat = part2[:a]
    remainder = part2[a:]
    content = part1 + repeat * b + decompress_string(remainder)

    return content


# decompression version2, 2b and 2c all work, but only 2b & 2c in decent amount of time for long input

def decompress_string_version2(content: str) -> str:
    if '(' not in content:
        return content

    components = re.split(r'(\(.*?\))', content, maxsplit=1)
    part1 = components[0]
    a, b = re.findall(r'(\d+)', components[1])
    a, b = int(a), int(b)
    part2 = components[2]
    repeat = part2[:a]
    remainder = part2[a:]
    content = decompress_string_version2(part1 + repeat * b + decompress_string_version2(remainder))

    return content


def decompress_string_version2b(content: str) -> int | str:
    if '(' not in content:
        return len(content)

    components = re.split(r'(\(.*?\))', content, maxsplit=1)
    part1 = components[0]
    a, b = re.findall(r'(\d+)', components[1])
    a, b = int(a), int(b)
    part2 = components[2]
    repeat = part2[:a]
    remainder = part2[a:]
    len_content = decompress_string_version2b(part1) + b * decompress_string_version2b(repeat) + decompress_string_version2b(remainder)

    return len_content


def decompress_string_version2c(content: str) -> int:
    if '(' not in content:
        return len(content)

    def decompress(content):
        total_length = 0
        i = 0

        while i < len(content):
            if content[i] == '(':
                end_marker = content.find(')', i)
                marker = content[i + 1:end_marker]
                a, b = map(int, marker.split('x'))
                i = end_marker + 1
                repeat_segment = content[i:i + a]
                total_length += b * decompress_string_version2c(repeat_segment)
                i += a
            else:
                total_length += 1
                i += 1

        return total_length

    return decompress(content)


def compute_part_one(file_name: str) -> str:
    content = read_input_file(file_name)
    print(content)

    decompressed = decompress_string(content)
    print(f'{decompressed= }')

    return f'{len(decompressed)= }'


def compute_part_two(file_name: str) -> str:
    content = read_input_file(file_name)
    print(content)

    decompressed_length = decompress_string_version2b(content)
    print(f'{decompressed_length= }')

    return f'{decompressed_length= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input9.txt')}")
    print(f"Part II: {compute_part_two('input/input9.txt')}")
