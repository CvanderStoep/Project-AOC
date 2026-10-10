import re
from collections import deque
from functools import lru_cache


def read_input_file(file_name: str) -> tuple:
    with open(file_name) as f:
        content = f.read().split('\n\n')
    patterns = content[0].split(', ')
    designs = content[1].splitlines()

    return patterns, designs


def check_design_recursive(design: str, patterns: list) -> bool:
    @lru_cache
    def _check_design_recursive(design: str) -> bool:
        if design == '':
            return True

        fitted_patterns = [pattern for pattern in patterns if design.startswith(pattern)]
        for pattern in fitted_patterns:
            remainder = design[len(pattern):]
            if _check_design_recursive(remainder):
                return True
        return False

    return _check_design_recursive(design)


def check_design_recursive_count(design: str, patterns: list) -> int:
    @lru_cache
    def _check_design_recursive(design: str) -> int:
        if design == '':
            return 1

        fitted_patterns = [pattern for pattern in patterns if design.startswith(pattern)]
        total_sum = 0
        for pattern in fitted_patterns:
            remainder = design[len(pattern):]
            total_sum += _check_design_recursive(remainder)
        return total_sum

    return _check_design_recursive(design)


def check_design_queue(design: str, patterns: list) -> bool:
    queue = deque([design])
    while queue:
        design = queue.popleft()

        fitted_patterns = [pattern for pattern in patterns if design.startswith(pattern)]

        for pattern in fitted_patterns:
            remainder = design[len(pattern):]
            if remainder == '':
                return True
            else:
                queue.append(remainder)

    return False


def check_design_regex(design: str, patterns: list) -> bool:

    pattern_ = ''
    for pattern in patterns:
        pattern_ = pattern_ + '|' + pattern
    pattern = re.compile(r"^(" + pattern_ + ")+$")

    if re.fullmatch(pattern, design):
        # print(f"'{design}' matches the pattern.")
        return True
    else:
        # print(f"'{design}' does not match the pattern.")
        return False


def compute_part_one(file_name: str) -> int:
    patterns, designs = read_input_file(file_name)

    possible_designs = 0
    for design in designs:
        fits = check_design_recursive(design, patterns)
        # fits = check_design_regex(design, patterns)
        if fits:
            possible_designs += 1

    return possible_designs


def compute_part_two(file_name: str) -> int:
    patterns, designs = read_input_file(file_name)

    total_count = 0
    for design in designs:
        count = check_design_recursive_count(design, patterns)
        total_count += count

    return total_count


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input19.txt')}")
    print(f"Part II: {compute_part_two('input/input19.txt')}")
