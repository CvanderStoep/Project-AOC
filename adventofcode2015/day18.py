def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    grid = []
    for line in content:
        grid.append(list(line))

    return grid


def get_grid_value(grid: list, i: int, j: int) -> str:
    # i --> : rows, j: columns

    if (0 <= i < len(grid[0])) and (0 <= j < len(grid[0])):
        return grid[j][i]
    else:
        return "."


def update_cell(grid: list, i: int, j: int, part: int = 1) -> str:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    cols, rows = len(grid[0]), len(grid)

    corners = [(0, 0), (0, rows - 1), (cols - 1, 0), (rows - 1, cols - 1)]
    if (i, j) in corners and part == 2:
        return '#'
    number_on_neighbours = 0
    for direction in directions:
        di, dj = direction
        if get_grid_value(grid, i + di, j + dj) == "#":
            number_on_neighbours += 1

    if get_grid_value(grid, i, j) == "#":
        if 2 <= number_on_neighbours <= 3:
            light = "#"
        else:
            light = "."
    else:
        if number_on_neighbours == 3:
            light = "#"
        else:
            light = '.'

    return light


def update_grid(grid, part=1) -> list:
    cols, rows = len(grid[0]), len(grid)

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(cols):
        for j in range(rows):
            new_grid[j][i] = update_cell(grid, i, j, part)

    return new_grid


def light_count(grid) -> int:
    count = 0
    char = "#"
    for row in grid:
        count += row.count(char)
    return count


def compute_part(file_name: str, part=1) -> int:
    grid = read_input_file(file_name)
    print(grid)
    for i in range(1, 101):
        grid = update_grid(grid, part)
    number_of_lights = light_count(grid)
    print(f'{light_count(grid)= }')

    return number_of_lights


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input18.txt', part=1)}")
    print(f"Part II: {compute_part('input/input18.txt', part=2)}")
