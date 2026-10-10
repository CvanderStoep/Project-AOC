from day6 import add_tuples, check_out_of_bounds


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')
    grid = content[0].splitlines()
    grid2 = []
    for line in grid:
        grid2.append(list(line))
    moves = content[1].replace('\n', '')

    return grid2, moves


def find_dot(grid: list, location: tuple, move: tuple) -> tuple:
    # find the location of the first dot in the direction of the move
    # return (0, 0) if nothing was found
    while True:
        location = add_tuples(location, move)
        x, y = location
        if grid[y][x] == "#":
            return 0, 0
        if grid[y][x] == ".":
            return location


def move_robot(location: tuple, move: str, grid: list) -> (tuple, bool):
    directions = {'<': (-1, 0), 'v': (0, 1), '>': (1, 0), '^': (0, -1)}
    move = directions[move]
    new_location = add_tuples(location, move)
    x_new, y_new = new_location
    x_old, y_old = location
    if grid[y_new][x_new] == "#":
        return location
    if grid[y_new][x_new] == ".":
        grid[y_new][x_new], grid[y_old][x_old] = grid[y_old][x_old], grid[y_new][x_new]
        return new_location
    if grid[y_new][x_new] == "O":
        dot_location = find_dot(grid, new_location, move)
        if dot_location == (0, 0):
            return location

        grid[y_new][x_new], grid[y_old][x_old] = "@", "."
        x_dot, y_dot = dot_location
        grid[y_dot][x_dot] = "O"

    return new_location


def calc_gps(grid: list) -> int:
    gps = 0
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            if letter == "O":
                gps = gps + 100 * y + x

    return gps


def find_start_location(grid, symbol):
    for i, row in enumerate(grid):
        for j, element in enumerate(row):
            if element == symbol:
                return i, j


def print_grid(grid) -> None:
    for row in grid:
        print(row)


def compute_part_one(file_name: str) -> int:
    grid, moves = read_input_file(file_name)

    location = find_start_location(grid, symbol='@')
    for move in moves:
        location = move_robot(location, move, grid)

    sum_gps = calc_gps(grid)
    # print(f'{sum_gps= }')

    return sum_gps


def compute_part_two(file_name: str) -> int:
    grid, moves = read_input_file(file_name)
    return "not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input15.txt')}")
    print(f"Part II: {compute_part_two('input/input15.txt')}")
