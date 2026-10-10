import itertools
import copy
from tqdm import tqdm

def add_tuples(tuple1, tuple2):
    return tuple([a + b for a, b in zip(tuple1, tuple2)])


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def find_symbol_location(grid, symbol):
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == symbol:
                return i, j


def direction_sequence(directions: list):
    for direction in itertools.cycle(directions):
        yield direction


def check_out_of_bounds(location, grid) -> bool:
    i, j = location
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid):
        return True
    else:
        return False


def compute_part_one(file_name: str) -> int:
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    directions = direction_sequence(directions)
    different_positions = set()
    grid = read_input_file(file_name)
    print(len(grid), len(grid[0]))
    symbol = '^'
    current_location = find_symbol_location(grid, symbol)
    different_positions.add(tuple(current_location))
    print(f'The location of the start-symbol "{symbol}" is: {current_location}')
    direction = next(directions)
    while True:
        new_location = add_tuples(current_location, direction)
        if check_out_of_bounds(new_location, grid):
            print('out of bounds at', new_location)
            break
        if grid[new_location[0]][new_location[1]] == "#":
            direction = next(directions)
        else:
            current_location = new_location
        different_positions.add(current_location)

    return len(different_positions)


def modify_grid(grid, i, j):
    grid_copy = copy.deepcopy(grid)
    if grid[i][j] == ".":
        grid_copy[i] = grid_copy[i][:j] + "#" + grid_copy[i][j+1:]
    return grid_copy


def compute_part_two(file_name: str) -> int:
    original_grid = read_input_file(file_name)
    number_of_possible_obstructions = 0
    for i in tqdm(range(len(original_grid))):
        for j in range(len(original_grid)):
            grid = modify_grid(original_grid, i, j)
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            directions = direction_sequence(directions)
            direction = next(directions)
            symbol = '^'
            current_location = find_symbol_location(grid, symbol)
            different_positions = set()
            different_positions.add(tuple(current_location) + (direction,))
            while True:
                new_location = add_tuples(current_location, direction)
                if check_out_of_bounds(new_location, grid):
                    break
                if grid[new_location[0]][new_location[1]] == "#":
                    direction = next(directions)
                else:
                    current_location = new_location
                if (current_location + (direction,)) in different_positions:
                    number_of_possible_obstructions += 1
                    break
                different_positions.add(current_location + (direction,))

    print(f'{number_of_possible_obstructions= }')
    return number_of_possible_obstructions


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input6.txt')}")
    print(f"Part II: {compute_part_two('input/input6.txt')}")
