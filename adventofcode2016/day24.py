from collections import deque


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    cols, rows = len(content[0]), len(content)
    grid = [['' for _ in range(cols)] for _ in range(rows)]
    keys = ''
    for y, line in enumerate(content):
        for x, symbol in enumerate(line):
            grid[y][x] = symbol
            if symbol not in '.#':
                keys = keys + symbol
    keys = ''.join(sorted(keys))

    return grid, keys


def is_valid(grid: list, position: tuple) -> bool:
    x, y = position
    if grid[y][x] != '#':
        return True
    return False


def find_start(grid: list, start='0') -> tuple:
    for y, line in enumerate(grid):
        for x, symbol in enumerate(line):
            if symbol == start:
                print('start= ', x, y)
                return x, y


def compute_part(file_name: str, part=1) -> str:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    grid, all_keys = read_input_file(file_name)
    cols, rows = len(grid[0]), len(grid)

    print(grid)
    print(f'{all_keys= }')
    start = find_start(grid)
    queue = deque([(0, start, '0')])
    visited = set()
    keys_found = 0
    while queue:
        steps, position, keys = queue.popleft()
        if len(keys) > keys_found:
            print(steps, position, keys)
            keys_found = len(keys)
        if keys == all_keys and part == 1:
            return f'{steps= }'

        if keys == all_keys and position == start and part == 2:
            return f'{steps= }'

        if (position, keys) in visited:
            continue
        visited.add((position, keys))

        for (dx, dy) in directions:
            x, y = position
            nx, ny = x + dx, y + dy
            if (0 <= nx < cols) and (0 <= ny < rows) and is_valid(grid, (nx, ny)):
                char = grid[ny][nx]
                new_keys = keys
                if char not in keys and char != '.':
                    new_keys = ''.join(sorted(keys + char))
                queue.append((steps + 1, (nx, ny), new_keys))


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input24.txt', part=1)}")
    print(f"Part II: {compute_part('input/input24.txt', part=2)}")
