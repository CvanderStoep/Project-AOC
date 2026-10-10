"""
maze solving, queue, BFS, shortest route
"""
from collections import deque


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    content = [tuple(map(int, m.split(','))) for m in content]

    return content


def compute_part_one(file_name: str) -> int:
    memory = read_input_file(file_name)
    memory = memory[:1024]  # truncate memory to the first 1024 bytes
    rows, cols = 71, 71  # [0, 70] or [0, 71)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = (0, 0)
    finish = (rows - 1, cols - 1)
    visited = set(start)
    queue = deque([(start, 0)])
    while queue:
        (x, y), distance = queue.popleft()
        # print(len(queue), distance)
        if (x, y) == finish:
            return distance
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in memory:
                continue
            if 0 <= nx < rows and 0 <= ny < cols:
                if (nx, ny) not in visited:
                    queue.append(((nx, ny), distance + 1))
                    visited.add((nx, ny))


def compute_part_two(file_name: str) -> int:
    full_memory = read_input_file(file_name)
    rows, cols = 71, 71  # [0, 70]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    start = (0, 0)
    finish = (rows - 1, cols - 1)

    for bad_byte_index in range(5000):
        print(f'{bad_byte_index= }')
        memory = full_memory[:bad_byte_index + 1]  # truncate memory to the first bad byte
        visited = set(start)
        queue = deque([(start, 0)])
        # finished = False
        while queue:
            (x, y), distance = queue.popleft()
            if (x, y) == finish:
                # print(f'{distance= }')
                # finished = True
                break
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in memory:
                    continue
                if 0 <= nx < rows and 0 <= ny < cols:
                    if (nx, ny) not in visited:
                        queue.append(((nx, ny), distance + 1))
                        visited.add((nx, ny))
            # if finished:
            #     continue
            if len(queue) == 0:
                print(bad_byte_index, distance)
                print(full_memory[bad_byte_index])
                return full_memory[bad_byte_index]


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input18.txt')}")
    print(f"Part II: {compute_part_two('input/input18.txt')}")
