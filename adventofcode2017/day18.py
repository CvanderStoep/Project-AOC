from collections import defaultdict, deque

import re

def is_number(string):
    pattern = r'^-?\d+(\.\d+)?$'  # Matches integers and decimals
    return bool(re.match(pattern, string))

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def process_instruction(registers: dict, position: int, instructions: list) -> int:

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
    elif operator == 'mul':
        registers[operands[0]] *= get_value(operands[1])
    elif operator == 'mod':
        registers[operands[0]] %= get_value(operands[1])
    elif operator == 'rcv' and registers.get('sound', 0) != 0:
        registers['recover'] = registers['sound']
    elif operator == 'jgz':
        if get_value(operands[0]) > 0:
            position += get_value(operands[1])
            return position

    # Default increment for non-jump instructions
    position += 1
    return position

def process_instruction_queue(registers: dict, position: int, instructions: list, snd_count: int, input_queue=None, output_queue=None) -> \
tuple[int, str, int]:

    program_status = 'ok'

    # Parse the current instruction
    if position >= len(instructions) or position < 0:
        program_status = 'terminated'
        return position, program_status, snd_count

    instruction = instructions[position]
    operator, *operands = instruction.split()

    def get_value(operand):
        return int(operand) if is_number(operand) else registers.get(operand, 0)

    # Execute the instruction
    if operator == 'snd':
        output_queue.append(get_value(operands[0]))
        snd_count += 1
    elif operator == 'set':
        registers[operands[0]] = get_value(operands[1])
    elif operator == 'add':
        registers[operands[0]] += get_value(operands[1])
    elif operator == 'mul':
        registers[operands[0]] *= get_value(operands[1])
    elif operator == 'mod':
        registers[operands[0]] %= get_value(operands[1])
    elif operator == 'rcv' and input_queue:
        registers[operands[0]] = input_queue.popleft()
    elif operator == 'rcv' and not input_queue:
        program_status = 'waiting'
        return position, program_status, snd_count

    elif operator == 'jgz':
        if get_value(operands[0]) > 0:
            position += get_value(operands[1])
            return position, program_status, snd_count

    # Default increment for non-jump instructions
    position += 1
    return position, program_status, snd_count


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    registers = defaultdict(int)
    position = 0
    while True:
        position = process_instruction(registers, position, instructions)
        if registers['recover'] != 0:
            return f'{registers['recover']= }'

def compute_part_two(file_name: str) -> str:
    instructions = read_input_file(file_name)
    registers_0, registers_1 = defaultdict(int), defaultdict(int)
    registers_0['p'], registers_1['p'] = 0, 1
    position_0, position_1 = 0, 0
    queue_0, queue_1 = deque(), deque()
    snd0_count, snd1_count = 0, 0
    p0_status, p1_status = 'ok', 'ok'  # can be: ok, waiting or terminated

    while p0_status == 'ok' or p1_status == 'ok':
        if p0_status != 'terminated':
            position_0, p0_status, snd0_count = process_instruction_queue(registers_0, position_0, instructions, snd0_count, input_queue=queue_0, output_queue=queue_1)
        if p1_status != 'terminated':
            position_1, p1_status, snd1_count = process_instruction_queue(registers_1, position_1, instructions, snd1_count, input_queue=queue_1, output_queue=queue_0)

    return f'{snd1_count= }'




if __name__ == '__main__':
    file_path = 'input/input18.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")