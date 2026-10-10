from collections import deque


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def find_all_occurrences(grid):
    symbol = '0'
    occurrences = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == symbol:
                occurrences.append((i, j))
    return occurrences


def is_valid_position(number, position, topo_map) -> bool:
    size = len(topo_map)
    i, j = position
    if 0 <= i < size and 0 <= j < size:
        if topo_map[i][j] == '.':
            return False
        new_number = int(topo_map[i][j])
        if new_number - number == 1:
            return True
    return False


def find_trail(topo_map: list, starting_position: tuple) -> set:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    trails = set()
    current_path = []
    number = 0
    queue = deque()
    current_path.append([number, starting_position])
    queue.append(current_path)
    while queue:
        current_path = queue.popleft()
        number, current_position = current_path[-1]
        if number == 9:
            trails.add(tuple(current_path[-1]))
        for direction in directions:
            new_position = current_position[0] + direction[0], current_position[1] + direction[1]
            if is_valid_position(number, new_position, topo_map):
                new_path = list(current_path)
                new_path.append([number + 1, new_position])
                queue.append(new_path)

    return trails


def find_all_trails(topo_map: list, starting_position: tuple) -> int:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    number_of_trails = 0
    current_path = []
    number = 0
    queue = deque()
    current_path.append([number, starting_position])
    queue.append(current_path)
    while queue:
        current_path = queue.popleft()
        number, current_position = current_path[-1]
        if number == 9:
            number_of_trails += 1
        for direction in directions:
            new_position = current_position[0] + direction[0], current_position[1] + direction[1]
            if is_valid_position(number, new_position, topo_map):
                new_path = list(current_path)
                new_path.append([number + 1, new_position])
                queue.append(new_path)

    return number_of_trails


def compute_part_one(file_name: str) -> int:
    topographic_map = read_input_file(file_name)
    starting_positions = find_all_occurrences(topographic_map)
    total_score = 0
    for sp in starting_positions:
        trails = find_trail(topographic_map, sp)
        total_score += len(trails)
    print(f'{total_score= }')

    return total_score


def compute_part_two(file_name: str) -> int:
    topographic_map = read_input_file(file_name)
    starting_positions = find_all_occurrences(topographic_map)
    total_score = 0
    for sp in starting_positions:
        number_of_trails = find_all_trails(topographic_map, sp)
        total_score += number_of_trails
    print(f'{total_score= }')

    return total_score


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input10.txt')}")
    print(f"Part II: {compute_part_two('input/input10.txt')}")
