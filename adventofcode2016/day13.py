from collections import deque


def read_input_file(file_name: str) -> int:
    with open(file_name) as f:
        content = f.read().splitlines()

    return int(content[0])


def make_grid(number: int, size: int) -> list:
    grid = [['' for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            n = x * x + 3 * x + 2 * x * y + y + y * y + number
            binary_representation = bin(n)[2:]
            count_of_ones = binary_representation.count('1')
            if count_of_ones % 2 == 0:
                grid[y][x] = '.'
            else:
                grid[y][x] = '#'
    return grid


def is_valid(grid: list, position: tuple) -> bool:
    x, y = position
    if grid[y][x] == '.':
        return True
    return False


def compute_part_one(file_name: str) -> str:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    number = read_input_file(file_name)
    print(f'{number= }')
    start = (1, 1)
    finish = (31, 39)
    size = max(finish) + 1
    grid = make_grid(number, size)
    steps = 0
    queue = deque()
    queue.append((steps, start))
    visited = set()
    while queue:
        steps, position = queue.popleft()
        if position == finish:
            return f'goal {finish} reached in {steps} steps'
        visited.add(position)
        for direction in directions:
            x, y = position
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if (0 <= nx < size) and (0 <= ny < size):
                if is_valid(grid, (nx, ny)) and (nx, ny) not in visited:
                    queue.append((steps + 1, (nx, ny)))


def compute_part_two(file_name: str) -> str:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    number = read_input_file(file_name)
    start = (1, 1)
    size = 60
    grid = make_grid(number, size)
    steps = 0
    max_steps = 50
    queue = deque()
    queue.append((steps, start))
    visited = set()
    while queue:
        steps, position = queue.popleft()
        if steps == max_steps + 1:
            return f'after maximum {steps-1} steps, total reach: {len(visited)= }'
        visited.add(position)
        for direction in directions:
            x, y = position
            dx, dy = direction
            nx, ny = x + dx, y + dy
            if (0 <= nx < size) and (0 <= ny < size):
                if is_valid(grid, (nx, ny)) and (nx, ny) not in visited:
                    queue.append((steps + 1, (nx, ny)))


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input13.txt')}")
    print(f"Part II: {compute_part_two('input/input13.txt')}")
