import re
from typing import Any


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content

def get_parents(programs: list) -> dict[Any, Any]:
    # converts the programs list into a dictionay with child-parent relations
    p_list = [re.findall(r'[a-z]+', line) for line in programs]
    p_dict = dict()
    for p in p_list:
        for c in p[1:]:
            p_dict[c] = p[0]
    return p_dict

def find_bottom(programs: list) -> str:
    child_parent_dictionary = get_parents(programs)
    # gets the first child at the end of the child-parent-tree
    child = next(re.findall(r'[a-z]+', line)[0] for line in programs if '->' not in line)

    while child in child_parent_dictionary:
        child = child_parent_dictionary[child]
    return child


def get_weight(programs: list, program: str) -> int:
    weight = 0
    for line in programs:
        if line.startswith(program):
            # Get the weight of the current program
            weight = int(re.findall(r'(\d+)', line)[0])

            # If the program has no children, return its weight
            if '->' not in line:
                return weight
            else:
                # Extract the children and their weights
                children = re.findall(r'[a-z]+', line)[1:]
                child_weights = [get_weight(programs, child) for child in children]

                # Check if the children's weights are balanced
                if len(set(child_weights)) != 1:
                    print(f"Imbalance found in '{program}':")
                    print(f"Child weights: {child_weights}")
                    print(f"Expected weight: {max(set(child_weights), key=child_weights.count)}")

                    # Correct the weight of the unbalanced child
                    unbalanced_child = children[child_weights.index(min(child_weights))]
                    corrected_weight = max(set(child_weights), key=child_weights.count) - (sum(child_weights) - weight)
                    print(f"'{unbalanced_child}' should be adjusted to weight: {corrected_weight}")
                    exit()  # Stop execution after finding the correction

                # Sum the weights of the program and its children
                weight += sum(child_weights)
    return weight


def get_weight(programs: list, program: str) -> int:
    weight = 0
    for line in programs:
        if line.startswith(program):
            # Get the weight of the current program
            weight = int(re.findall(r'(\d+)', line)[0])

            # If the program has no children, return its weight
            if '->' not in line:
                return weight
            else:
                # Extract the children and their weights
                children = re.findall(r'[a-z]+', line)[1:]
                child_weights = [get_weight(programs, child) for child in children]

                # Check if the children's weights are balanced
                if len(set(child_weights)) != 1:
                    # Find the correct and incorrect weights
                    weight_counts = {w: child_weights.count(w) for w in child_weights}
                    correct_weight = [w for w in weight_counts if weight_counts[w] > 1][0]
                    incorrect_weight = [w for w in weight_counts if weight_counts[w] == 1][0]

                    # Find the unbalanced child
                    unbalanced_child = children[child_weights.index(incorrect_weight)]

                    # Compute the corrected weight for the unbalanced child
                    unbalanced_child_line = [l for l in programs if l.startswith(unbalanced_child)][0]
                    unbalanced_child_current_weight = int(re.findall(r'(\d+)', unbalanced_child_line)[0])
                    corrected_weight = unbalanced_child_current_weight + (correct_weight - incorrect_weight)

                    print(f"Unbalanced child: '{unbalanced_child}'")
                    print(f"Current weight: {unbalanced_child_current_weight}")
                    print(f"Corrected weight: {corrected_weight}")
                    exit()  # Stop execution after finding the correction

                # Sum the weights of the program and its children
                weight += sum(child_weights)
    return weight




def compute_part_one(file_name: str) -> str:
    programs = read_input_file(file_name)
    bottom = find_bottom(programs)

    return f'{bottom= }'

def compute_part_two(file_name: str) -> str:
    programs = read_input_file(file_name)
    bottom = find_bottom(programs)
    weight = get_weight(programs, bottom)

    return f'{weight= }'



if __name__ == '__main__':
    file_path = 'input/input7.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")