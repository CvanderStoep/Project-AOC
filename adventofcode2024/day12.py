from collections import deque

from tqdm import tqdm


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def valid_position(location: tuple, garden: list) -> bool:
    i, j = location
    if i < 0 or j < 0 or i >= len(garden) or j >= len(garden):
        return False
    else:
        return True


def find_connected_region(location: tuple, garden: list) -> set:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    region = set()
    visited = set()
    region.add(location)
    visited.add(location)
    i, j = location
    garden_letter = garden[i][j]
    queue = deque()
    queue.append(location)

    while queue:
        next_location = queue.popleft()
        region.add(next_location)
        visited.add(next_location)
        for direction in directions:
            new_location = next_location[0] + direction[0], next_location[1] + direction[1]
            if new_location in visited:
                continue
            i, j = new_location
            is_valid = valid_position(new_location, garden)
            if is_valid:
                new_garden_letter = garden[i][j]
                if new_garden_letter == garden_letter:
                    if new_location not in queue:
                        queue.append(new_location)

    return region


def calc_price(region: set) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    area = len(region)

    total_neighbours = 0
    for plant in region:
        for direction in directions:
            neighbour = plant[0] + direction[0], plant[1] + direction[1]
            if neighbour in region:
                total_neighbours += 1

    perimeter = 4 * len(region) - total_neighbours
    price = area * perimeter

    return price


def compute_part_one(file_name: str) -> int:
    garden_map = read_input_file(file_name)
    rows, cols = len(garden_map), len(garden_map[0])
    visited_nodes = set()
    total_price = 0
    for i in range(rows):
        for j in range(cols):
            starting_position = (i, j)
            if (i, j) in visited_nodes:
                continue
            region = find_connected_region(starting_position, garden_map)
            visited_nodes = visited_nodes | region
            price = calc_price(region)
            total_price += price


    return total_price


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    return "not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input12.txt')}")
    print(f"Part II: {compute_part_two('input/input12.txt')}")
