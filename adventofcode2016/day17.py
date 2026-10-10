import hashlib
from collections import deque


def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def md5_hash_string(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()


def is_valid(code: str, direction: str) -> bool:
    valid = 'bcdef'
    hashed = md5_hash_string(code)
    u, d, l, r = hashed[0], hashed[1], hashed[2], hashed[3]
    if u in valid and direction == 'U':
        return True
    if d in valid and direction == 'D':
        return True
    if l in valid and direction == 'L':
        return True
    if r in valid and direction == 'R':
        return True

    return False


def compute_part_one(file_name: str) -> str:
    passcode = read_input_file(file_name)
    print(f'{passcode= }')
    directions = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}

    start = (0, 0)
    finish = (3, 3)
    size = 4
    path = ''
    steps = 0
    queue = deque()
    queue.append((steps, start, path))
    while queue:
        steps, position, path = queue.popleft()
        passcode_path = passcode + path
        if position == finish:
            return f'{path= }'
        for direction, (dx, dy) in directions.items():
            x, y = position
            nx, ny = x + dx, y + dy
            if (0 <= nx < size) and (0 <= ny < size):
                if is_valid(passcode_path, direction):
                    queue.append((steps + 1, (nx, ny), path + direction))

    return "no solution found"


def compute_part_two(file_name: str) -> str:
    passcode = read_input_file(file_name)
    directions = {'R': (1, 0), 'D': (0, 1), 'L': (-1, 0), 'U': (0, -1)}

    start = (0, 0)
    finish = (3, 3)
    size = 4
    path = ''
    steps = 0
    queue = deque()
    queue.append((steps, start, path))
    longest_path = 0
    while queue:
        steps, position, path = queue.popleft()
        passcode_path = passcode + path
        if position == finish:
            longest_path = max(longest_path, steps)
        else:
            for direction, (dx, dy) in directions.items():
                x, y = position
                nx, ny = x + dx, y + dy
                if (0 <= nx < size) and (0 <= ny < size):
                    if is_valid(passcode_path, direction):
                        queue.append((steps + 1, (nx, ny), path + direction))

    return f'{longest_path= } steps'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input17.txt')}")
    print(f"Part II: {compute_part_two('input/input17.txt')}")
