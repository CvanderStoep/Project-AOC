from typing import List, Dict


def read_input_file(file_name: str) -> List[str]:
    """Reads input file and returns content as a list of strings."""
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def process_instruction(position: int, instructions: List[str], registers: Dict[str, int]) -> int:
    """Processes a single instruction and updates the registers."""
    instruction = instructions[position].split(' ')
    cmd = instruction[0]
    args = instruction[1:]

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
        # www.reddit.com/r/adventofcode/comments/5jvbzt/2016_day_23_solutions/
        # replace below loop that increments a with d*b:
        # cpy b c
        # inc a
        # dec c
        # jnz c -2
        # dec d
        # jnz d -5

        # with:
        # mul b d a
        # cpy 0 c
        # cpy 0 c
        # cpy 0 c
        # cpy 0 c
        # cpy 0 d
        # could also just use 5x jnz 0 0

        registers[instruction[3]] = registers[instruction[2]] * registers[instruction[1]]
        position += 1

    else:
        print('Invalid instruction:', ' '.join(instruction))
        position += 1

    return position


def compute(file_name: str, initial_a: int) -> str:
    """Computes the value of register 'a' after processing all instructions."""
    instructions = read_input_file(file_name)
    registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
    position = 0
    while position < len(instructions):
        position = process_instruction(position, instructions, registers)

    return f'{registers["a"]= }'


if __name__ == '__main__':
    print(f"Part I: {compute('input/input23.txt', initial_a=7)}")
    print(f"Part II: {compute('input/input23.txt', initial_a=12)}")

    # output = a! + 8100
