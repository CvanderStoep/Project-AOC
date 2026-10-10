from collections import defaultdict, deque

import re

def is_number(string):
    pattern = r'^-?\d+(\.\d+)?$'  # Matches integers and decimals
    return bool(re.match(pattern, string))

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def process_instruction(registers: dict, position: int, instructions: list, mul_times: int) -> tuple[int, int]:

    # Parse the current instruction
    instruction = instructions[position]
    operator, *operands = instruction.split()

    def get_value(operand):
        return int(operand) if is_number(operand) else registers.get(operand, 0)

    # Execute the instruction
    if operator == 'snd':
        registers['sound'] = get_value(operands[0])
    elif operator == 'set':
        registers[operands[0]] = get_value(operands[1])
    elif operator == 'add':
        registers[operands[0]] += get_value(operands[1])
    elif operator == 'sub':
        registers[operands[0]] -= get_value(operands[1])
    elif operator == 'mul':
        registers[operands[0]] *= get_value(operands[1])
        mul_times += 1
    elif operator == 'mod':
        registers[operands[0]] %= get_value(operands[1])
    elif operator == 'rcv' and registers.get('sound', 0) != 0:
        registers['recover'] = registers['sound']
    elif operator == 'jgz':
        if get_value(operands[0]) > 0:
            position += get_value(operands[1])
            return position, mul_times
    elif operator == 'jnz':
        if get_value(operands[0]) != 0:
            position += get_value(operands[1])
            return position, mul_times
    # Default increment for non-jump instructions
    position += 1
    return position, mul_times


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    registers = defaultdict(int)
    position = 0
    mul_times = 0
    while 0<= position < len(instructions):
        position, mul_times = process_instruction(registers, position, instructions, mul_times)
    return f'{mul_times= }'

def compute_part_two(file_name: str) -> str:
    return f'run python code day23-part2'


if __name__ == '__main__':
    file_path = 'input/input23.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")