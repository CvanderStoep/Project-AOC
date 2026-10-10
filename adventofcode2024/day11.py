from functools import lru_cache

from tqdm import tqdm


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split()

    return content


@lru_cache(maxsize=1024)
def calc_new_stones(stone: str) -> tuple:
    new_stone2 = None
    if stone == '0':
        new_stone1 = '1'
    elif len(stone) % 2 == 0:
        mid = int(len(stone) / 2)
        new_stone1 = stone[:mid]
        new_stone2 = str(int(stone[mid:]))
    else:
        new_stone1 = str(int(stone) * 2024)

    return new_stone1, new_stone2


def apply_rules(stones: list) -> list:
    # stones: list of strings
    new_stones = []
    for stone in stones:
        stone1, stone2 = calc_new_stones(stone)
        new_stones.append(stone1)
        if stone2 is not None:
            new_stones.append(stone2)
    return new_stones


@lru_cache(maxsize=1024)
# Issue: not clear why this is still slow, used memoization instead (see next code calc_stone_length_memo)
# Solved by increasing the maxsize
def calc_stone_length(stone: str, number: int) -> int:
    if number == 0:
        return 1
    stone1, stone2 = calc_new_stones(stone)
    if stone2 is not None:
        return calc_stone_length(stone1, number - 1) + calc_stone_length(stone2, number - 1)
    else:
        return calc_stone_length(stone1, number - 1)


def calc_stone_length_memo(stone: str, number: int, memo={}) -> int:
    if number == 0:
        return 1
    if (stone, number) in memo:
        return memo[(stone, number)]
    stone1, stone2 = calc_new_stones(stone)
    if stone2 is not None:
        memo[(stone, number)] = (calc_stone_length_memo(stone1, number - 1, memo) +
                                 calc_stone_length_memo(stone2, number - 1, memo))
    else:
        memo[(stone, number)] = calc_stone_length_memo(stone1, number - 1, memo)

    return memo[(stone, number)]


def compute_part_one(file_name: str) -> int:
    stones = read_input_file(file_name)
    for i in (range(1, 26)):
        stones = apply_rules(stones)
    print(f'{len(stones)= }')

    return len(stones)


def compute_part_two(file_name: str) -> int:
    stones = read_input_file(file_name)
    number_of_blinks = 75
    total_length = 0
    for stone in stones:
        l = calc_stone_length(stone, number_of_blinks)
        total_length += l

    print(f'{total_length= }')
    return total_length


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input11.txt')}")
    print(f"Part II: {compute_part_two('input/input11.txt')}")
