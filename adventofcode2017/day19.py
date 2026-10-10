def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def process_step(direction: str, position: tuple) -> tuple:
    directions = {'n': (0, -1), 's': (0, 1), 'e': (1, 0), 'w': (-1, 0)}
    dx, dy = directions[direction]
    x, y = position
    position = x + dx, y + dy
    return position

def get_symbol(diagram, position) -> str:
    i, j = position
    try:
        return diagram[j][i]
    except IndexError:
        return ' '


def change_direction(diagram, position, direction) -> str:
    i, j = position
    if direction in 'ns':
        if get_symbol(diagram, (i-1, j)) != " ":
            direction = 'w'
        else:
            direction = 'e'
    else:
        if get_symbol(diagram, (i, j-1)) != " ":
            direction = 'n'
        else:
            direction = 's'
    return direction


def compute_part_one(file_name: str) -> str:
    diagram = read_input_file(file_name)
    position = (diagram[0].find('|'), 0)
    direction = 's'
    print(position, get_symbol(diagram, position))
    symbol = get_symbol(diagram, position)
    letters = ''
    steps = 0
    while symbol != ' ':
        steps += 1
        position = process_step(direction, position)
        symbol = get_symbol(diagram, position)
        if symbol == '+':
            direction = change_direction(diagram, position, direction)
        if symbol not in '|-+':
            letters = letters + symbol
    print(f'Part II: {steps= }')

    return letters


if __name__ == '__main__':
    file_path = 'input/input19.txt'
    print(f"Part I: {compute_part_one(file_path)}")
