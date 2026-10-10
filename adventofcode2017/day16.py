import re

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split(',')

    return content

def process_move(move: str, programs: str) ->str:
    if move.startswith('s'):
        m = int(re.findall(r'(\d+)', move)[0])
        programs = programs[-m:] + programs[:len(programs)-m]
    if move.startswith('x'):
        x1, x2 = map(int, re.findall(r'(\d+)', move))
        programs = list(programs)
        programs[x1], programs[x2] = programs[x2], programs[x1]
        programs = ''.join(programs)
    if move.startswith('p'):
        p1, p2 = move[1], move[3]
        x1, x2 = programs.index(p1), programs.index(p2)
        programs = list(programs)
        programs[x1], programs[x2] = programs[x2], programs[x1]
        programs = ''.join(programs)
    return programs

def compute_part_one(file_name: str) -> str:
    moves = read_input_file(file_name)
    programs = 'abcdefghijklmnop'

    for move in moves:
        programs = process_move(move, programs)

    return f'{programs= }'

def compute_part_two(file_name: str) -> str:
    moves = read_input_file(file_name)
    programs = 'abcdefghijklmnop'

    seen = set()
    cycle = 1
    seen.add(programs)
    while True:
        for move in moves:
            programs = process_move(move, programs)
        if programs in seen:
            break
        seen.add(programs)
        cycle += 1

    for _ in range((1000000000-1) % cycle + 1):
        for move in moves:
            programs = process_move(move, programs)
    return f'{programs= }'


if __name__ == '__main__':
    file_path = 'input/input16.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")