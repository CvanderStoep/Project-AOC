"""
maze solving, queue, BFS, shortest route, heapq in day20-heap, visualization in day20-heap
"""
import itertools
from collections import deque

from tqdm import tqdm


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    grid = []
    for line in content:
        grid.append(list(line))

    return grid


def find_start_end(track: list) -> tuple:
    for iy in range(len(track)):
        for ix in range(len(track[0])):
            if track[iy][ix] == "S":
                sx, sy = ix, iy
            if track[iy][ix] == "E":
                ex, ey = ix, iy
    start = (sx, sy)
    finish = (ex, ey)
    return start, finish


def get_walls(track: list) -> set:
    walls = set()
    for iy in range(1, len(track) - 1):
        for ix in range(1, len(track[0]) - 1):
            if track[iy][ix] == "#":
                wall = (ix, iy)
                walls.add(wall)
    return walls


def compute_part_one(file_name: str) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    track = read_input_file(file_name)
    rows, cols = len(track[0]), len(track)
    start, finish = find_start_end(track)

    walls = get_walls(track)
    cheats = []
    queue = deque([(start, 0)])
    visited = set(start)
    while queue:
        (x, y), distance = queue.popleft()
        if (x, y) == finish:
            regular_distance = distance
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if track[ny][nx] != "#":
                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited:
                        queue.append(((nx, ny), distance + 1))
                        visited.add((nx, ny))

    for (wx, wy) in tqdm(walls):
        track[wy][wx] = "."
        queue = deque([(start, 0)])
        visited = set(start)
        while queue:
            (x, y), distance = queue.popleft()
            if (x, y) == finish:
                track[wy][wx] = "#"
                cheats.append(distance - regular_distance)
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if track[ny][nx] != "#":
                    if 0 <= nx < rows and 0 <= ny < cols:  # could be removed
                        if (nx, ny) not in visited:
                            queue.append(((nx, ny), distance + 1))
                            visited.add((nx, ny))

    cheats.sort()
    count_cheats = {}
    total_savings_over_100 = 0
    for number in cheats:
        if number in count_cheats:
            count_cheats[number] += 1
        else:
            count_cheats[number] = 1
        if number <= -100:
            total_savings_over_100 += 1
    print(f'{total_savings_over_100= }')

    return total_savings_over_100


def manhattan_distance(c1: tuple, c2: tuple) -> int:
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def compute_part_two(file_name: str) -> int:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    track = read_input_file(file_name)
    rows, cols = len(track[0]), len(track)
    start, finish = find_start_end(track)

    visited = set(start)
    path = [start]
    queue = deque([(start, 0, path)])

    while queue:
        (x, y), distance, path = queue.popleft()
        if (x, y) == finish:
            regular_distance = distance
            break
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if track[ny][nx] != "#":
                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited:
                        queue.append(((nx, ny), distance + 1, path + [(nx, ny)]))
                        visited.add((nx, ny))
    print(f'{regular_distance= }')
    print(f'{path= }')
    combinations = itertools.combinations(path, 2)
    count_cheats = {}
    print(regular_distance * regular_distance / 2)

    for c1, c2 in tqdm(combinations):
        manh_difference = manhattan_distance(c1, c2)
        if manh_difference > 20:
            continue
        path_difference = path.index(c2) - path.index(c1)
        if path_difference <= 20:
            continue
        saving = path_difference - manh_difference
        if saving in count_cheats:
            count_cheats[saving] += 1
        else:
            count_cheats[saving] = 1

    total_savings_over_100 = 0
    print(count_cheats)
    for key, value in count_cheats.items():
        print(f'{key}: {value}')
        if key >= 100:
            total_savings_over_100 += value
    print(f'{total_savings_over_100= }')

    return total_savings_over_100


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input20.txt')}")
    print(f"Part II: {compute_part_two('input/input20.txt')}")
