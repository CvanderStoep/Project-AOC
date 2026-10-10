"""
maze solving, queue, BFS, shortest route, heapq, visualization
"""
from collections import deque

from tqdm import tqdm

import heapq

import matplotlib.pyplot as plt
import numpy as np


def visualize_maze(track: list, visited: set = set()) -> None:
    matrix = []
    for x,y in visited:
        track[y][x] = "V"

    for row in track:
        line = []
        for symbol in row:
            match symbol:
                case ".":
                    line.append(1)
                case "#":
                    line.append(0)
                case "S":
                    line.append(2)
                case "E":
                    line.append(2)
                case _:
                    line.append(2)

        matrix.append(line)

    plt.imshow(matrix, cmap='viridis')
    plt.colorbar()
    plt.title('Matrix Visualization')
    plt.show()


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
    visualize_maze(track)
    rows, cols = len(track[0]), len(track)
    start, finish = find_start_end(track)

    walls = get_walls(track)
    cheats = []
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
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
    print(f'{regular_distance= }')
    # visualize_maze(track, visited)

    # using a heapq
    for (wx, wy) in tqdm(walls):
        track[wy][wx] = "."
        queue = [(0, start)]
        visited = set(start)
        while queue:
            distance, (x, y) = heapq.heappop(queue)
            if (x, y) == finish:
                track[wy][wx] = "#"
                cheats.append(distance - regular_distance)
                # print(distance)
                break
                # return distance
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if track[ny][nx] != "#":
                    if 0 <= nx < rows and 0 <= ny < cols:  # could be removed
                        if (nx, ny) not in visited:
                            heapq.heappush(queue, (distance + 1, (nx, ny)))
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


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    return 2


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input20.txt')}")
    print(f"Part II: {compute_part_two('input/input20.txt')}")
