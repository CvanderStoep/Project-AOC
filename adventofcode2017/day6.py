from typing import Any


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return list(map(int, f.read().split()))


def distribute_memory(memory: list) -> list:
    max_index = memory.index(max(memory))
    blocks = memory[max_index]
    memory[max_index] = 0

    for i in range(blocks):
        memory[(max_index + 1 + i) % len(memory)] += 1
    return memory


def find_cycle(memory: list) -> tuple[int | Any, list]:
    seen = set()
    seen.add(tuple(memory))
    cycle = 1
    while True:
        memory = distribute_memory(memory)
        if tuple(memory) in seen:
            return cycle, memory
        seen.add(tuple(memory))
        cycle += 1


def compute_part_one(file_name: str) -> str:
    memory = read_input_file(file_name)
    print(memory)
    cycle, memory = find_cycle(memory)
    return f'number of redistribution cycles before configuration is seen again: {cycle}'


def compute_part_two(file_name: str) -> str:
    memory = read_input_file(file_name)

    # the first call is identical to part I
    # the second call is to get the repeat cycle after it was found

    cycle, memory = find_cycle(memory)
    cycle, memory = find_cycle(memory)
    return f'cycle size: {cycle}'


if __name__ == '__main__':
    file_path = 'input/input6.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")
