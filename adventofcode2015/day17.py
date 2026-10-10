# making change problem with containers
# recursive, all combinations, minimum only
# with and without memoization
import time


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    content = list(map(int, content))

    return content


def fill_container_all_combinations(containers: list, liters: int) -> list:
    def find_combinations(containers, target, current_combination=None, all_combinations=None):
        if current_combination is None:
            current_combination = []
        if all_combinations is None:
            all_combinations = []

        if target == 0:
            all_combinations.append(current_combination.copy())
            return all_combinations

        if target < 0 or not containers:
            return all_combinations

        for i in range(len(containers)):
            current_combination.append(containers[i])
            find_combinations(containers[i + 1:], target - containers[i], current_combination, all_combinations)
            current_combination.pop()

        return all_combinations

    return find_combinations(containers, liters)


def fill_container_memo(containers: list, liters: int, memo=None) -> int:
    if memo is None:
        memo = {}

    key = (tuple(containers), liters)
    if key in memo:
        return memo[key]

    total = 0
    if liters < 0:
        return 0
    if liters == 0:
        total += 1
    elif len(containers) != 0:
        total = total + fill_container_memo(containers[1:], liters - containers[0], memo) + \
                fill_container_memo(containers[1:], liters, memo)

    memo[key] = total
    return total


def fill_container(containers: list, liters: int) -> int:
    total = 0
    if liters < 0:
        return 0

    if liters == 0:
        total += 1
    elif len(containers) != 0:
        total = total + fill_container(containers[1:], liters - containers[0]) + \
                fill_container(containers[1:], liters)
    return total


def fill_container_find_minimum_only(containers: list, liters: int) -> int:
    def find_minimum_combinations(containers, target, current_combination=None):
        if current_combination is None:
            current_combination = []

        if target == 0:
            return len(current_combination)

        if target < 0 or not containers:
            return float('inf')

        # Include the current container
        with_current = find_minimum_combinations(containers[1:], target - containers[0],
                                                 current_combination + [containers[0]])

        # Exclude the current container
        without_current = find_minimum_combinations(containers[1:], target, current_combination)

        return min(with_current, without_current)

    return find_minimum_combinations(containers, liters)


def compute_part_one(file_name: str) -> int:
    containers = read_input_file(file_name)
    print(containers)
    number_of_ways = fill_container(containers, 150)
    print(f'{number_of_ways= }')

    return number_of_ways


def compute_part_one_memo(file_name: str) -> int:
    containers = read_input_file(file_name)
    print(containers)
    number_of_ways = fill_container_memo(containers, 150)
    print(f'{number_of_ways= }')

    return number_of_ways


def compute_part_two(file_name: str) -> int:
    containers = read_input_file(file_name)
    combinations = fill_container_all_combinations(containers, 150)
    minimum_amount = float('inf')
    for combo in combinations:
        minimum_amount = min(minimum_amount, len(combo))
    total_different_minimum_ways = 0
    for combo in combinations:
        if len(combo) == minimum_amount:
            total_different_minimum_ways += 1
    print(f'{total_different_minimum_ways= }')

    return total_different_minimum_ways


if __name__ == '__main__':
    start_time = time.time()
    print(f"Part I: {compute_part_one('input/input17.txt')}")
    print("Elapsed time:", time.time() - start_time)

    start_time = time.time()
    print(f"Part I: {compute_part_one_memo('input/input17.txt')}")
    print("Elapsed time:", time.time() - start_time)

    start_time = time.time()
    print(f"Part II: {compute_part_two('input/input17.txt')}")
    print("Elapsed time:", time.time() - start_time)
