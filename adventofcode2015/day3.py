def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read()

    return content


def compute_part_one(file_name: str) -> int:
    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}

    moves = read_input_file(file_name)
    location = (0, 0)
    locations = set()
    locations.add(location)

    for move in moves:
        x, y = location
        dx, dy = directions[move]
        location = x + dx, y + dy
        locations.add(location)

    number_of_visited_houses = len(locations)

    return number_of_visited_houses


def compute_part_two(file_name: str) -> int:
    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}

    moves = read_input_file(file_name)
    location_santa = (0, 0)
    location_robo_santa = (0, 0)
    locations = set()
    locations.add(location_santa)

    for position in range(0, len(moves), 2):
        x, y = location_santa
        dx, dy = directions[moves[position]]
        location_santa = x + dx, y + dy
        locations.add(location_santa)

        x, y = location_robo_santa
        dx, dy = directions[moves[position + 1]]
        location_robo_santa = x + dx, y + dy
        locations.add(location_robo_santa)

    number_of_visited_houses = len(locations)

    return number_of_visited_houses


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input3.txt')}")
    print(f"Part II: {compute_part_two('input/input3.txt')}")
