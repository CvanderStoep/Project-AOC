from collections import deque


def read_input_file(file_name: str) -> int:
    with open(file_name) as f:
        return int(f.read().strip())


def compute_part_one(file_name: str) -> str:
    number = read_input_file(file_name)
    print(f'{number= }')
    # queue = deque()
    # for n in range(1, number + 1):
    #     queue.append(n)
    queue = deque(range(1, number + 1))

    while queue:
        winner = queue.popleft()
        if queue:
            _ = queue.popleft()
            queue.append(winner)

    return f'{winner= }'


def compute_part_two(file_name: str) -> str:
    """slow but it works..."""
    number = read_input_file(file_name)
    # elves = []
    # for n in range(1, number + 1):
    #     elves.append(n)
    elves = list(range(1, number + 1))

    while elves:
        len_elves_list = len(elves)
        winner = elves.pop(0)
        if elves:
            mid = len_elves_list // 2
            loser = elves.pop(mid - 1)
            elves.append(winner)

    return f'{winner= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input19.txt')}")
    print(f"Part II: {compute_part_two('input/input19.txt')}")

