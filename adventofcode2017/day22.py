from typing import Any

def read_input_file(file_name: str) -> tuple[dict[tuple[int, int], str], tuple[int, int]]:
    grid = {}
    with open(file_name) as f:
        for row_index, row in enumerate(f.read().splitlines()):
            for col_index, char in enumerate(row):
                grid[(col_index, row_index)] = char

    return grid, (row_index//2, col_index//2)

def process_step(grid, direction, position, infections)-> tuple[int | Any, tuple[int | Any, int | Any], Any]:
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    x, y = position
    char = grid.get(position, '.')
    if char == '#':
        direction += 1
        grid[position] = '.'
    else:
        direction -= 1
        grid[position] = '#'
        infections += 1
    direction = direction %4
    dx, dy = directions[direction]
    position = x + dx, y + dy

    return direction, position, infections


def process_step2(grid, direction, position, infections)-> tuple[int | Any, tuple[int | Any, int | Any], Any]:
    directions = {0: (0, -1), 1: (1, 0), 2: (0, 1), 3: (-1, 0)}
    x, y = position
    char = grid.get(position, '.')
    if char == '.':
        direction -= 1
        grid[position] = 'W'
    if char == 'W':
        grid[position] = '#'
        infections += 1
    if char == '#':
        direction += 1
        grid[position] = 'F'
    if char == 'F':
        direction += 2
        grid[position] = '.'


    direction = direction %4
    dx, dy = directions[direction]
    position = x + dx, y + dy

    return direction, position, infections

def print_grid(grid) -> None:
    for j in range(-10, 10):
        for i in range(-10, 10):
            print(grid.get((i,j), '.'),end='')
        print()

def visualize_grid(grid, position, direction):
    """Visualizes the grid with states and the current position of the virus carrier."""
    # Adjusting the display range dynamically based on virus position
    min_x = min(x for x, _ in grid.keys())
    max_x = max(x for x, _ in grid.keys())
    min_y = min(y for _, y in grid.keys())
    max_y = max(y for _, y in grid.keys())

    symbols = {
        '.': '.',  # Clean
        'W': 'W',  # Weakened
        '#': '#',  # Infected
        'F': 'F',  # Flagged
    }

    direction_arrows = {
        0: '^',  # Up
        1: '>',  # Right
        2: 'v',  # Down
        3: '<',  # Left
    }

    print("\nCurrent Grid State:")
    for y in range(min_y - 1, max_y + 2):  # Add a small buffer around the grid
        for x in range(min_x - 1, max_x + 2):
            if (x, y) == position:
                print(direction_arrows[direction], end='')  # Virus carrier direction
            else:
                print(symbols.get(grid.get((x, y), '.'), '.'), end='')  # Grid state
        print()


def compute_part_one(file_name: str) -> str:
    grid, virus = read_input_file(file_name)
    direction = 0
    position = virus
    infections = 0

    for i in range(10000):
        direction, position, infections = process_step(grid, direction, position, infections)

    return f'{infections= }'


def compute_part_two(file_name: str) -> str:
    grid, virus = read_input_file(file_name)
    direction = 0
    position = virus
    infections = 0

    for i in range(100000):
        direction, position, infections = process_step2(grid, direction, position, infections)
    visualize_grid(grid, position, direction)

    return f'{infections= }'


if __name__ == '__main__':
    file_path = 'input/input22.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")