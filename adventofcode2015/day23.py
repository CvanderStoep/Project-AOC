import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(registers: dict, position: int, instruction: str) -> (int, int, int):
    pattern = r'-?\d+'
    if 'hlf' in instruction:
        register_name = instruction[-1]
        registers[register_name] = registers[register_name] // 2
        position += 1
    if 'tpl' in instruction:
        register_name = instruction[-1]
        registers[register_name] *= 3
        position += 1
    if 'inc' in instruction:
        register_name = instruction[-1]
        registers[register_name] += 1
        position += 1
    if 'jmp' in instruction:
        jump = int(re.findall(pattern, instruction)[0])
        position += jump
    if 'jie' in instruction:
        register_name = instruction[4]
        r = registers[register_name]
        if r % 2 == 0:
            jump = int(re.findall(pattern, instruction)[0])
            position += jump
        else:
            position += 1
    if 'jio' in instruction:
        register_name = instruction[4]
        r = registers[register_name]
        if r == 1:
            jump = int(re.findall(pattern, instruction)[0])
            position += jump
        else:
            position += 1

    return registers, position

# alternative
# def process_instruction(registers: dict, position: int, instruction: str) -> (dict, int):
#     pattern = r'-?\d+'
#     parts = instruction.replace(',', '').split()
#
#     match parts:
#         case ['hlf', reg]:
#             registers[reg] //= 2
#             position += 1
#         case ['tpl', reg]:
#             registers[reg] *= 3
#             position += 1
#         case ['inc', reg]:
#             registers[reg] += 1
#             position += 1
#         case ['jmp', offset]:
#             position += int(offset)
#         case ['jie', reg, offset]:
#             if registers[reg] % 2 == 0:
#                 position += int(offset)
#             else:
#                 position += 1
#         case ['jio', reg, offset]:
#             if registers[reg] == 1:
#                 position += int(offset)
#             else:
#                 position += 1
#
#     return registers, position


def compute_part_one(file_name: str) -> int:
    registers = {'a': 0, 'b': 0}
    instructions = read_input_file(file_name)
    print(instructions)
    position = 0

    while position < len(instructions):
        instruction = instructions[position]
        registers, position = process_instruction(registers, position, instruction)

    return registers['b']


def compute_part_two(file_name: str) -> int:
    registers = {'a': 1, 'b': 0}
    instructions = read_input_file(file_name)
    position = 0

    while position < len(instructions):
        instruction = instructions[position]
        registers, position = process_instruction(registers, position, instruction)

    return registers['b']


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input23.txt')}")
    print(f"Part II: {compute_part_two('input/input23.txt')}")
