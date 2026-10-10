from typing import List, Dict


def read_input_file(file_name: str) -> List[str]:
    """Reads input file and returns content as a list of strings."""
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(position: int, instructions: List[str], registers: Dict[str, int]) -> int:
    """Processes a single instruction and updates the registers."""
    instruction = instructions[position].split(' ')

    if instruction[0] == 'inc':
        registers[instruction[1]] += 1
        position += 1

    elif instruction[0] == 'dec':
        registers[instruction[1]] -= 1
        position += 1

    elif instruction[0] == 'cpy':
        src, dest = instruction[1], instruction[2]
        registers[dest] = int(src) if src.isdigit() else registers[src]
        position += 1

    elif instruction[0] == 'jnz':
        src, offset = instruction[1], int(instruction[2])
        x = int(src) if src.isdigit() else registers[src]
        position += offset if x != 0 else 1

    else:
        print('Invalid instruction:', ' '.join(instruction))
        position += 1

    return position


def compute(file_name: str, initial_c: int = 0) -> str:
    """Computes the value of register 'a' after processing all instructions."""
    instructions = read_input_file(file_name)
    registers = {'a': 0, 'b': 0, 'c': initial_c, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)

    return f'{registers["a"]= }'


if __name__ == '__main__':
    print(f"Part I: {compute('input/input12.txt')}")
    print(f"Part II: {compute('input/input12.txt', initial_c=1)}")
