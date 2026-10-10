# https://github.com/TimHuisman1703/AdventOfCode/blob/master/2024/Day%2016/aoc16_1.py
""""
priority queue, heap, map, maze, shortest route, cheapest route
"""

file = open("input\input16.txt")
g = file.read().split("\n")
file.close()

import heapq

for iy in range(len(g)):
    for ix in range(len(g[0])):
        if g[iy][ix] == "S":
            sx, sy = ix, iy
        if g[iy][ix] == "E":
            ex, ey = ix, iy

q = [(0, sx, sy, 1, 0)]
visited = set()

while q:
    cost, x, y, dx, dy = heapq.heappop(q)

    if x == ex and y == ey:
        print(cost)
        break

    key = (x, y, dx, dy)
    if key in visited:
        continue
    visited.add(key)

    if g[y + dy][x + dx] != "#":
        nx = x + dx
        ny = y + dy
        heapq.heappush(q, (cost + 1, nx, ny, dx, dy))
    heapq.heappush(q, (cost + 1000, x, y, dy, -dx))
    heapq.heappush(q, (cost + 1000, x, y, -dy, dx))