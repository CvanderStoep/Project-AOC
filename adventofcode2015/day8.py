import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.readlines()

    return content


def count_characters(line):
    # Characters in code (length of the string including quotes and escape characters)
    code_characters = len(line)

    # Remove the surrounding double quotes
    in_memory_string = line[1:-1]

    # Replace escape sequences to count in-memory characters
    in_memory_string = in_memory_string.replace(r'\\', '\\')  # Replace double backslash with single backslash
    in_memory_string = in_memory_string.replace(r'\"', '"')  # Replace escaped quote with a double quote
    in_memory_string = re.sub(r'\\x[0-9a-fA-F]{2}', '#', in_memory_string)  # Replace \x?? with a single character

    in_memory_characters = len(in_memory_string)

    return code_characters, in_memory_characters


def encoded_length(line):
    encoded_string = '"'  # Start with an extra double quote
    for char in line:
        if char == '\\' or char == '"':
            encoded_string += '\\'  # Add an escape character for backslash or double quote
        encoded_string += char
    encoded_string += '"'  # End with an extra double quote
    return len(encoded_string)


def compute_part_one(file_name: str) -> int:
    lines = read_input_file(file_name)

    total_code_characters = 0
    total_in_memory_characters = 0

    # Iterate over each line and calculate the totals
    for line in lines:
        line = line.strip()
        code_characters, in_memory_characters = count_characters(line)
        total_code_characters += code_characters
        total_in_memory_characters += in_memory_characters

    # Calculate the difference
    difference = total_code_characters - total_in_memory_characters

    print(f'Total characters of code: {total_code_characters}')
    print(f'Total characters in memory: {total_in_memory_characters}')
    print(f'Difference: {difference}')

    return difference


def compute_part_two(file_name: str) -> int:
    lines = read_input_file(file_name)
    total_encoded_length = 0
    total_original_length = 0

    # Iterate over each line and calculate the totals
    for line in lines:
        line = line.strip()
        total_original_length += len(line)
        total_encoded_length += encoded_length(line)

    # Calculate the difference
    difference = total_encoded_length - total_original_length

    print(f'Total encoded length: {total_encoded_length}')
    print(f'Total original length: {total_original_length}')
    print(f'Difference: {difference}')
    return difference


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input8.txt')}")
    print(f"Part II: {compute_part_two('input/input8.txt')}")
