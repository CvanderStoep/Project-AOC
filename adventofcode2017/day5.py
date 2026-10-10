def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
        # return f.read().strip()
    content = list(map(int, content))

    return content

def process_instructions(instructions: list, position: int=0) -> int:

    steps = 0
    while 0<= position < len(instructions):
        steps += 1
        old_position = position
        position += instructions[position]
        instructions[old_position] += 1

    return steps

def process_instructions_two(instructions: list, position: int=0) -> int:

    steps = 0
    while 0<= position < len(instructions):
        steps += 1
        old_position = position
        offset = instructions[position]
        position += instructions[position]
        instructions[old_position] += -1 if offset >= 3 else 1

    return steps

def compute_part(file_name: str, jump_function) -> str:
    instructions = read_input_file(file_name)
    number_of_steps = jump_function(instructions)

    return f'{number_of_steps= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input5.txt', process_instructions)}")
    print(f"Part II: {compute_part('input/input5.txt', process_instructions_two)}")
