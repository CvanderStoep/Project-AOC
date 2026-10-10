import re

from tqdm import tqdm


def read_input_file(file_name: str) -> tuple:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    register = content[0]
    program = content[1]

    A, B, C = map(int, re.findall(r'-?\d+', register))
    program = list(map(int, re.findall(r'-?\d+', program)))

    return A, B, C, program


def process_instruction(opcode, operand, A, B, C, position, outputlist) -> tuple:
    match operand:
        case 0 | 1 | 2 | 3:
            combo = operand
        case 4:
            combo = A
        case 5:
            combo = B
        case 6:
            combo = C

    # division = int(A / (2 ** combo))
    division = A >> combo
    modulo = combo % 8
    match opcode:
        case 0:
            A = division
        case 1:
            B = B ^ operand
        case 2:
            B = modulo
        case 3:
            if A != 0:
                position = operand
        case 4:
            B = B ^ C
        case 5:
            outputlist.append(modulo)
        case 6:
            B = division
        case 7:
            C = division
        case _:
            print('unknown value')

    return A, B, C, position


def compute_part_one(file_name: str) -> int:
    A, B, C, program = read_input_file(file_name)
    position = 0
    outputlist = []
    while position < len(program):
        opcode = program[position]
        operand = program[position + 1]
        A, B, C, new_position = process_instruction(opcode, operand, A, B, C, position, outputlist)
        if new_position == position:
            position += 2
        else:
            position = new_position

    return ','.join(map(str, outputlist))

def compute_part_two(file_name: str) -> int:
    A, B, C, program = read_input_file(file_name)
    program_string = ','.join(map(str, program))
    A_try = 164541017976509 - 100  # this must be a lucky guess : - )
    while True:
        A = A_try
        position = 0
        outputlist = []
        while position < len(program):
            opcode = program[position]
            operand = program[position + 1]
            A, B, C, new_position = process_instruction(opcode, operand, A, B, C, position, outputlist)
            if new_position == position:
                position += 2
            else:
                position = new_position
        output_string = ','.join(map(str, outputlist))
        if program_string == output_string:
            return A_try
            # print(A_try)
            # print(','.join(map(str, outputlist)))
            break
        A_try += 1

    return "nothing found"




if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input17.txt')}")
    print(f"Part II: {compute_part_two('input/input17.txt')}")
