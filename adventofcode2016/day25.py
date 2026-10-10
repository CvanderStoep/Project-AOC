from typing import List, Dict, Tuple, Any


def read_input_file(file_name: str) -> List[str]:
    """Reads input file and returns content as a list of strings."""
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(position: int, instructions: List[str], registers: Dict[str, int]) -> tuple[int, Any]:
    """Processes a single instruction and updates the registers."""
    instruction = instructions[position].split(' ')
    cmd = instruction[0]
    args = instruction[1:]
    sequence = None

    if cmd == 'inc':
        registers[args[0]] += 1
        position += 1

    elif cmd == 'dec':
        registers[args[0]] -= 1
        position += 1

    elif cmd == 'cpy':
        # src, dest = instruction[1], instruction[2]
        src, dest = args
        registers[dest] = registers[src] if src in 'abcd' else int(src)
        position += 1

    elif cmd == 'jnz':
        src, dest = args
        x = int(src) if src.isdigit() else registers[src]
        offset = registers[dest] if dest in 'abcd' else int(dest)
        position += offset if x != 0 else 1

    elif cmd == 'tgl':  # toggle instruction
        x = instruction[1]
        tgl_position = position + registers[x]
        if tgl_position >= len(instructions):
            pass
        else:
            tgl_instruction = instructions[tgl_position].split(' ')
            cmd = tgl_instruction[0]
            args = tgl_instruction[1:]

            if cmd == 'inc':
                instructions[tgl_position] = 'dec ' + args[0]
            if cmd == 'dec':
                instructions[tgl_position] = 'inc ' + args[0]
            if cmd == 'tgl':
                instructions[tgl_position] = 'inc ' + args[0]
            if cmd == 'jnz':
                instructions[tgl_position] = 'cpy ' + args[0] + ' ' + args[1]
            if cmd == 'cpy':
                instructions[tgl_position] = 'jnz ' + args[0] + ' ' + args[1]

        position += 1

    elif cmd == 'mul':
        registers[instruction[3]] = registers[instruction[2]] * registers[instruction[1]]
        position += 1

    elif cmd == 'out':
        src = args[0]
        sequence = int(src) if src.isdigit() else registers[src]
        position += 1

    else:
        print('Invalid instruction:', ' '.join(instruction))
        position += 1

    return position, sequence


def compute(file_name: str, initial_a: int) -> str:
    """Computes the value of register 'a' after processing all instructions."""
    instructions = read_input_file(file_name)
    while True:
        registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
        position = 0
        previous_integer = 1
        print()
        print(initial_a, ': ', previous_integer, end='')
        sequence_count = 0
        while position < len(instructions):
            position, transmitted_integer = process_instruction(position, instructions, registers)
            if transmitted_integer is not None:
                print(transmitted_integer, end='')
                if transmitted_integer == previous_integer:
                    initial_a += 1
                    break
                else:
                    previous_integer = transmitted_integer
                    sequence_count += 1
            if sequence_count > 50:
                print()
                return f'{initial_a= }'


if __name__ == '__main__':
    print(f"Part I: {compute('input/input25.txt', initial_a=0)}")
