import math
from collections import defaultdict
from day3copilot import generate_spiral, get_keys_by_value

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
        # return f.read().strip()
    content = list(map(int, content))


    return content

def get_coordinates(n):
    if n == 1:
        return (0, 0)  # The center of the spiral

    # Find the layer (k) of the spiral
    k = math.ceil((math.sqrt(n) - 1) / 2)

    # Maximum number in the current layer
    max_num_in_layer = (2 * k + 1) ** 2

    # Distance from n to the bottom-right corner of the layer
    d = max_num_in_layer - n

    # Determine the side and offset along that side
    side_length = 2 * k
    if d < side_length:  # Bottom side
        return (k - d, -k)
    elif d < 2 * side_length:  # Left side
        d -= side_length
        return (-k, -k + d)
    elif d < 3 * side_length:  # Top side
        d -= 2 * side_length
        return (-k + d, k)
    else:  # Right side
        d -= 3 * side_length
        return (k, k - d)

def calculate_manhattan_distance(coordinates: tuple) -> int:
    x, y = coordinates
    return abs(x) + abs(y)

def compute_part_one(n: int) -> str:
    coordinates = get_coordinates(n)
    print(f"The coordinates of {n} are: {coordinates}")
    print(f'The Manhattan distance is: {calculate_manhattan_distance(coordinates)}')

    # using alternative way to make the grid, suggested by copilot
    grid = generate_spiral(n)
    keys = get_keys_by_value(grid, n)
    print(f'{keys= }')

    return f'{calculate_manhattan_distance(coordinates)= }'

def compute_part_two(n: int) -> str:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    square = defaultdict(int)
    square[(0,0)] = 1

    i = 2
    while True:
        x, y = get_coordinates(i)
        n_sum = 0
        for dx, dy in directions:
            n_sum += square[(x+dx,y+dy)]
        square[(x, y)] = n_sum
        if n_sum > n:
            return f'{n_sum= }'
        i += 1



if __name__ == '__main__':
    print(f"Part I: {compute_part_one(n = 368078)}")
    print(f"Part II: {compute_part_two(n = 368078)}")
