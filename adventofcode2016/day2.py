def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_instruction(position: tuple, instruction: str) -> tuple:
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    r, c = position
    for move in instruction:
        match move:
            case 'U':
                r -= 1
            case 'D':
                r += 1
            case 'L':
                c -= 1
            case 'R':
                c += 1
            case _:
                print('invalid move')
        if r < 0:
            r = 0
        if r > 2:
            r = 2
        if c < 0:
            c = 0
        if c > 2:
            c = 2

    number = keypad[r][c]
    return (r, c), number


def process_instruction_two(position: tuple, instruction: str) -> tuple:
    keypad = [[0, 0, 1, 0, 0],
              [0, 2, 3, 4, 0],
              [5, 6, 7, 8, 9],
              [0, 'A', 'B', 'C', 0],
              [0, 0, 'D', 0, 0]]
    r, c = position
    moves = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }

    for move in instruction:
        r_org, c_org = r, c
        if move in moves:
            dr, dc = moves[move]
            r = max(0, min(4, r + dr))
            c = max(0, min(4, c + dc))
        else:
            print('invalid move')
        if keypad[r][c] == 0:
            r, c = r_org, c_org

    number = keypad[r][c]
    return (r, c), number


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    print(instructions)
    position = (1, 1)  # start at keypad == 5
    code = ''
    for instruction in instructions:
        position, number = process_instruction(position, instruction)
        code = code + str(number)

    return f'{code= }'


def compute_part_two(file_name: str) -> str:
    instructions = read_input_file(file_name)
    position = (2, 0)  # start at keypad == 5 (row=2,col=0)
    code = ''
    for instruction in instructions:
        position, number = process_instruction_two(position, instruction)
        code = code + str(number)

    return f'{code= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")
