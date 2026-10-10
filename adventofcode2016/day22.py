import itertools
import re
from dataclasses import dataclass


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content[2:]


@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    available: int
    percentage: int


def get_viable_pairs(nodes: dict) -> int:
    viable_pairs = 0
    combinations = itertools.permutations(nodes, 2)
    for combination in combinations:
        a, b = combination
        nodeA: Node = nodes[a[0], a[1]]
        nodeB: Node = nodes[b[0], b[1]]
        if nodeA.used != 0 and nodeA.used <= nodeB.available:
            viable_pairs += 1

    return viable_pairs


def compute_part_one(file_name: str) -> str:
    content = read_input_file(file_name)
    nodes = dict()
    for line in content:
        x, y, size, used, available, percentage = map(int, re.findall(r'(\d+)', line))
        node = Node(x, y, size, used, available, percentage)
        nodes[(x, y)] = node

    number_of_viable_pairs = get_viable_pairs(nodes)

    return f'{number_of_viable_pairs= }'


def compute_part_two(file_name: str) -> str:
    content = read_input_file(file_name)
    nodes = dict()
    full_nodes = []
    for line in content:
        x, y, size, used, available, percentage = map(int, re.findall(r'(\d+)', line))
        node = Node(x, y, size, used, available, percentage)
        nodes[(x, y)] = node
        if node.used == 0:
            x0, y0 = node.x, node.y
            print(f'{node= }')
    for key, node in nodes.items():
        if node.used >= nodes[(x0, y0)].available:
            full_nodes.append(key)
    for y in range(24):
        for x in range(38):
            if (x, y) == (0, 0):
                print('F', end='')
            elif (x, y) == (37, 0):
                print('G', end='')
            elif (x, y) == (x0, y0):
                print('0', end='')
            elif (x, y) in full_nodes:
                print('#', end='')
            else:
                print('.', end='')
        print()

    print('it takes 6 + 21 + 8 steps to get the 0-node to top right')
    print('it takes 5 switches to move the G-data one position to the left')
    print('it takes 36 steps = 180 switches')

    fewest_number_of_steps = 36 * 5 + 6 + 21 + 8

    return f'{fewest_number_of_steps= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input22.txt')}")
    print(f"Part II: {compute_part_two('input/input22.txt')}")
