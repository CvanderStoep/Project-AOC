# https://github.com/TimHuisman1703/AdventOfCode/blob/master/2024/Day%2012/aoc12_2.py

file = open("input/input12.txt")
g = file.read().split("\n")
file.close()

seen = [[False] * len(g[0]) for _ in range(len(g))]

r = 0
for sy in range(len(g)):
    for sx in range(len(g[0])):
        if seen[sy][sx]:
            continue
        print(sx, sy, g[sy][sx])
        q = [(sx, sy)]
        area = 0
        sides = set()
        while q:
            x, y = q.pop()

            if seen[y][x]:
                continue
            seen[y][x] = True
            area += 1

            for d in range(4):
                nx = x + (d == 0) - (d == 1)
                ny = y + (d == 2) - (d == 3)

                if nx < 0 or nx >= len(g[0]) or ny < 0 or ny >= len(g):
                    sides.add((nx, ny, d))
                    continue
                if g[ny][nx] != g[sy][sx]:
                    sides.add((nx, ny, d))
                    continue

                q.append((nx, ny))
        print(sides)
        sides = {
            (x, y, d) for x, y, d in sides
            if (x - (d >= 2), y - (d < 2), d) not in sides
        }
        print(sides)
        print(len(sides))

        r += area * len(sides)

print(r)