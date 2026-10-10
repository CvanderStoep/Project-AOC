import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_input(inputs: list) -> list:
    pattern = r'mul\(\d+,\d+\)'
    instructions = [re.findall(pattern, line) for line in inputs]
    return instructions


def process_input_part2(inputs: list) -> list:
    # Use the join method to concatenate the strings
    inputs = " ".join(inputs)
    instructions = []

    pattern_do = r'do\(\).*mul\(\d+,\d+\)'  # greedy last one
    pattern_do_dont = r'do\(\).*?don\'t\(\)'  # non-greedy

    inputs = "do()" + inputs
    while inputs:
        match = re.search(pattern_do_dont, inputs)
        if match:  # find do()-dont() block
            inputs = inputs[match.end():]
            instructions.append(match.group())
        else:
            last_match = re.findall(pattern_do, inputs)[0]
            instructions.append(last_match)
            inputs = []

    return instructions


def process_instruction(instruction: str) -> int:
    numbers = re.findall(r'\d+', instruction)
    a, b = map(int, numbers)
    return a * b


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    all_instructions = process_input(inputs)
    total_instructions = 0
    for instructions in all_instructions:
        for instruction in instructions:
            outcome = process_instruction(instruction)
            total_instructions += outcome

    return total_instructions


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    inputs_enabled_instructions = process_input_part2(inputs)
    total_instructions = 0
    for line in inputs_enabled_instructions:
        # process_input expects a list as input and generates a list as output

        instructions = process_input([line])[0]
        for instruction in instructions:
            outcome = process_instruction(instruction)
            total_instructions += outcome

    return total_instructions


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input3.txt')}")
    print(f"Part II: {compute_part_two('input/input3.txt')}")
