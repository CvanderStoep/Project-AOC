from collections import deque

import numpy as np
def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        content = f.read()
    return content

# Function to convert hexadecimal to binary with 4-digit formatting
def hex_to_binary(hex_string):
    # Convert to integer, then format as binary and ensure 4-digit padding for each hex digit
    binary_string = ''.join(bin(int(digit, 16))[2:].zfill(4) for digit in hex_string)
    return binary_string

def knot_hash(lst: list, l, pos):

    array_length = len(lst)
    new_array = lst.copy()
    for i in range(l):
        new_array[(pos + i) % array_length] = lst[(pos + l -i -1) % array_length]
    return new_array

def calculate_knot_hash(key_string: str) -> str:
    lengths = [ord(x) for x in key_string] + [17, 31, 73, 47, 23]
    lst = list(range(256))
    skip = 0
    pos = 0
    for _ in range(64):
        for l in lengths:
            lst = knot_hash(lst, l, pos)
            pos += (l + skip)
            pos = pos % len(lst)
            skip += 1
    arr = np.array(lst)
    hex_string = ''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(arr.reshape(16, 16), axis=1))
    return hex_string

def compute_part_one(file_name: str) -> str:
    puzzle_input = read_input_file(file_name)
    number_of_squares = 0
    size = 128
    print(f'{puzzle_input= }')
    for i in range(size):
        key_string = puzzle_input + '-' + str(i)
        hex_string = calculate_knot_hash(key_string)
        binary_string = hex_to_binary(hex_string)
        number_of_squares += binary_string.count('1')

    return f'{number_of_squares}'

def compute_part_two(file_name: str) -> str:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    puzzle_input = read_input_file(file_name)
    grid = []
    size = 128
    for i in range(size):
        key_string = puzzle_input + '-' + str(i)
        hex_string = calculate_knot_hash(key_string)
        binary_string = hex_to_binary(hex_string)
        grid.append(binary_string)

    visited = set()
    number_of_regions = 0

    for y in range(size):
        for x in range(size):
            if (x, y) not in visited and grid[y][x] == '1':
                # Use BFS to explore a new region
                queue = deque([(x, y)])
                while queue:
                    cx, cy = queue.popleft()
                    if (cx, cy) not in visited:
                        visited.add((cx, cy))
                        for dx, dy in directions:
                            nx, ny = cx + dx, cy + dy
                            if 0 <= nx < size and 0 <= ny < size and grid[ny][nx] == '1' and (nx, ny) not in visited:
                                queue.append((nx, ny))
                number_of_regions += 1


    return f'{number_of_regions= } '


if __name__ == '__main__':
    file_path = 'input/input14.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
