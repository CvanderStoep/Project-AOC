import itertools

from tqdm import tqdm


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    return content


def process_input(inputs: list) -> (list, list):
    rules = inputs[0].splitlines()
    all_pages = inputs[1].splitlines()
    rules = [list(map(int, rule.split('|'))) for rule in rules]
    all_pages = [list(map(int, page.split(','))) for page in all_pages]

    return rules, all_pages


def generate_combinations(input_list: tuple):
    return itertools.combinations(input_list, 2)


def generate_permutations(input_list: list):
    return itertools.permutations(input_list)


def check_rule(combination: tuple, rule: list) -> bool:
    rule1, rule2 = rule
    page1, page2 = combination
    if page1 == rule2 and page2 == rule1:
        return False
    else:
        return True


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    rules, all_pages = process_input(inputs)
    total_middle_page_numbers = 0
    for pages in all_pages:
        correct = True
        combinations = generate_combinations(pages)
        for combination in combinations:
            for rule in rules:
                correct = check_rule(combination, rule)
                if not correct:
                    break
            if not correct:
                break
        if correct:
            total_middle_page_numbers += pages[len(pages) // 2]

    return total_middle_page_numbers


def compute_part_two_slow(file_name: str) -> int:
    inputs = read_input_file(file_name)
    rules, all_pages = process_input(inputs)
    total_middle_page_numbers = 0
    for pages in all_pages:
        for np in generate_permutations(pages):
            correct = True
            combinations = generate_combinations(np)
            for combination in combinations:
                for rule in rules:
                    correct = check_rule(combination, rule)
                    if not correct:
                        break
                if not correct:
                    break
            if correct:
                if list(np) == pages:
                    pass
                else:
                    total_middle_page_numbers += np[len(np) // 2]
                break

    return total_middle_page_numbers


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    rules, all_pages = process_input(inputs)
    total_middle_page_numbers = 0
    for pages in tqdm(all_pages):
        original_pages = list(pages)
        correct = False
        while not correct:
            correct = True
            combinations = generate_combinations(pages)
            for combination in combinations:
                for rule in rules:
                    correct = check_rule(combination, rule)
                    if not correct:
                        index1 = pages.index(rule[0])
                        index2 = pages.index(rule[1])
                        pages[index1], pages[index2] = pages[index2], pages[index1]
                        break
                if not correct:
                    break
            if correct:
                if list(original_pages) == pages:
                    pass
                else:
                    total_middle_page_numbers += pages[len(pages) // 2]
                break

    return total_middle_page_numbers


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input5.txt')}")
    # print(f"Part II: {compute_part_two_slow('input/input5.txt')}")
    print(f"Part II: {compute_part_two('input/input5.txt')}")
