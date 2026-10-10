import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split(', ')

    return content


def calculate_distance(position) -> int:
    x, y = position
    return abs(x) + abs(y)


def process_instruction(position, direction, instruction) -> (int, int):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    turn = instruction[0]

    if turn == 'R':
        direction = (direction + 1) % 4
    elif turn == 'L':
        direction = (direction - 1) % 4

    x, y = position
    dx, dy = directions[direction]

    pattern = r'\d+'
    steps = int(re.findall(pattern, instruction)[0])

    position = (x + steps * dx, y + steps * dy)

    return direction, position


def add_positions(previous_position, position, visited_locations):
    visited_twice = None
    x1, y1 = previous_position
    x2, y2 = position

    if y1 == y2:  # horizontal movement
        xb = min(x1, x2)
        xe = max(x1, x2)
        for x in range(xb + 1, xe):
            if (x, y1) in visited_locations:
                visited_twice = (x, y1)
                break
            else:
                visited_locations.add((x, y1))
    else:  # vertical movement
        yb = min(y1, y2)
        ye = max(y1, y2)
        for y in range(yb + 1, ye):
            if (x1, y) in visited_locations:
                visited_twice = (x1, y)
                break
            else:
                visited_locations.add((x1, y))

    return visited_locations, visited_twice


def compute_part_one(file_name: str) -> str:
    instructions = read_input_file(file_name)
    print(instructions)
    direction = 0
    position = (0, 0)

    for instruction in instructions:
        direction, position = process_instruction(position, direction, instruction)

    distance = calculate_distance(position)

    return f'{distance= }'


def compute_part_two(file_name: str) -> str:
    instructions = read_input_file(file_name)
    direction = 0
    position = (0, 0)
    visited_locations = set()
    visited_locations.add(position)
    previous_position = position
    for instruction in instructions:
        direction, position = process_instruction(position, direction, instruction)
        visited_locations, visited_twice = add_positions(previous_position, position, visited_locations)
        if visited_twice:
            print(f'{visited_twice= }')
            break
        else:
            previous_position = position

    distance = calculate_distance(visited_twice)

    return f'{distance= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input1.txt')}")
    print(f"Part II: {compute_part_two('input/input1.txt')}")
