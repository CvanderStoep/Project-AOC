"""
grid[i][j]
i: vertical, j: horizontal
"""


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    return content


def get_grid(grid: list, i: int, j: int) -> str:
    if (0 <= i < len(grid[0])) and (0 <= j < len(grid[0])):
        return grid[i][j]
    else:
        return "."


def compute_part_one(file_name: str) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    secret_word = "XMAS"
    word_count = 0
    grid = read_input_file(file_name)
    cols, rows = len(grid[0]), len(grid)

    for direction in directions:
        di, dj = direction[0], direction[1]
        for i in range(rows):  # rows
            for j in range(cols):  # cols
                compose_word = ''
                for k in range(4):
                    compose_word += get_grid(grid, i + k * di, j + k * dj)
                if compose_word == secret_word:
                    word_count += 1

    print(f'{word_count= }')

    return word_count


def compute_part_two(file_name: str) -> int:
    # secret_word = "X-MAS"
    word_count = 0
    grid = read_input_file(file_name)
    cols, rows = len(grid[0]), len(grid)

    for i in range(rows):  # rows
        for j in range(cols):  # cols
            if get_grid(grid, i, j) != "A":
                continue
            else:
                l1 = get_grid(grid, i - 1, j - 1)
                l2 = get_grid(grid, i - 1, j + 1)
                l3 = get_grid(grid, i + 1, j - 1)
                l4 = get_grid(grid, i + 1, j + 1)
                if ((l1 == "M" and l4 == "S") or (l1 == "S" and l4 == "M")) and \
                        ((l2 == "M" and l3 == "S") or (l2 == "S" and l3 == "M")):
                    word_count += 1

    print(f'{word_count= }')

    return word_count


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input4.txt')}")
    print(f"Part II: {compute_part_two('input/input4.txt')}")
