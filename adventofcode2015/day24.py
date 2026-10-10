# https://github.com/godarderik/adventofcode/blob/master/2015/problem2.py
import math


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    content = list(map(int, content))

    return set(content)


def generate_all_subsets_with_sum(nums, target):
    # Memoization dictionary to store results of subproblems
    memo = {}

    def dp(index, current_sum):
        # Base cases
        if current_sum == target:
            return {()}
        if current_sum > target or index == len(nums):
            return set()

        # Memoization check
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Include the current number in the subset
        include = dp(index + 1, current_sum + nums[index])
        include = {subset + (nums[index],) for subset in include}

        # Exclude the current number from the subset
        exclude = dp(index + 1, current_sum)

        # Combine results
        result = include.union(exclude)
        memo[(index, current_sum)] = result
        return result

    nums = sorted(nums)  # Convert set to a sorted list
    subsets = dp(0, 0)
    return subsets


def count_number_of_subsets_with_sum(nums, target):
    # Initialize a dictionary for memoization
    memo = {}

    def dp(index, current_sum):
        # Base cases
        if current_sum == target:
            return 1
        if current_sum > target or index == len(nums):
            return 0

        # Memoization check
        if (index, current_sum) in memo:
            return memo[(index, current_sum)]

        # Count subsets including the current number
        include_count = dp(index + 1, current_sum + nums[index])

        # Count subsets excluding the current number
        exclude_count = dp(index + 1, current_sum)

        # Store result in memoization dictionary
        memo[(index, current_sum)] = include_count + exclude_count
        return include_count + exclude_count

    nums = sorted(nums)  # Convert set to a sorted list
    return dp(0, 0)


def compute_part_one(file_name: str, input_list: list = []) -> int:
    # generate all sublists with a sum of total / 3
    # substract sublist from original list -> difference list
    # check for the difference list if a sum is also possible (count only)
    # store results, calculate QE and find the lowest value
    content = read_input_file(file_name)
    if len(input_list) != 0:
        content = set(input_list)
    target = sum(content) // 3
    print(content)
    subsets = generate_all_subsets_with_sum(content, target)
    final_list = []
    minimum_length = float('inf')
    i = 0
    for subset in subsets:
        if len(subset) <= minimum_length:
            minimum_length = min(len(subset), minimum_length)
            set_difference = content - set(subset)
            subset_count = count_number_of_subsets_with_sum(set_difference, target)
            if subset_count != 0:
                final_list.append(list(subset))

    sorted_list = sorted(final_list, key=len)
    min_length = len(sorted_list[0])
    min_product = float('inf')
    for l in sorted_list:
        if len(l) == min_length:
            if math.prod(l) < min_product:
                print(l, math.prod(l))
                min_product = math.prod(l)

    return min_product


def compute_part_two(file_name: str) -> int:
    # generate all sublists with a sum of total / 4
    # substract sublist from original list -> difference list
    # check for the difference list if a sum is also possible (count only)
    # store results, calculate QE and find the lowest value
    # this is a shortcut and not guaranteed to work
    # input [1, 2, 3, 4]
    # subset [1] and [2, 3, 4]; need to confirm that [2, 3, 4] can be split as well
    content = read_input_file(file_name)
    target = sum(content) // 4
    # print(content)
    subsets = generate_all_subsets_with_sum(content, target)
    final_list = []
    minimum_length = float('inf')
    i = 0
    for subset in subsets:
        if len(subset) <= minimum_length:
            minimum_length = min(len(subset), minimum_length)
            set_difference = content - set(subset)
            subset_count = count_number_of_subsets_with_sum(set_difference, target)
            if subset_count != 0:
                final_list.append(list(subset))

    sorted_list = sorted(final_list, key=len)
    min_length = len(sorted_list[0])
    min_product = float('inf')
    for l in sorted_list:
        if len(l) == min_length:
            if math.prod(l) < min_product:
                print(l, math.prod(l))
                min_product = math.prod(l)
                min_qe_list = l.copy()

    # final check if indeed the remaining list can be split into 3 equal parts
    # answer is not relevant, only if it is indeed possible
    print(f'{min_qe_list= }')
    difference = content - set(min_qe_list)
    print(f'{difference= }')
    check = compute_part_one(file_name, difference)
    print(f'{check= }')

    return min_product


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input24.txt')}")
    print(f"Part II: {compute_part_two('input/input24.txt')}")
