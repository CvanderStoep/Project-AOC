import re
from collections import defaultdict, deque


def read_input_file(file_name: str) -> defaultdict[int, list[int]]:
    connections = defaultdict(list)
    with open(file_name) as f:
        for line in f:
            node, neighbors = line.split('<->')
            connections[int(node)] = list(map(int, re.findall(r'\d+', neighbors)))
    return connections


def get_connected_graph(connections: dict, start: int) -> set:
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(n for n in connections[node] if n not in visited)

    return visited

def compute_part_one(file_name: str) -> str:
    connections = read_input_file(file_name)
    connected_graph = get_connected_graph(connections, 0)

    return f'{len(connected_graph)= }'

def compute_part_two(file_name: str) -> str:
    connections = read_input_file(file_name)
    all_graphs = set()
    number_of_graphs = 0
    for node in connections:
        if node not in all_graphs:
            number_of_graphs += 1
            connected_graph = get_connected_graph(connections, node)
            all_graphs.update(connected_graph)

    return f'{number_of_graphs= }'



if __name__ == '__main__':
    file_path = 'input/input12.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")