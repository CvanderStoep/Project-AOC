"""
graph networkx visualization itertools combinations fully connected components
"""

import itertools
import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def compute_part_one_slow(file_name: str) -> int:
    connections = read_input_file(file_name)
    combinations = itertools.combinations(connections, 3)
    number_of_3_sets = 0
    number_of_3_sets_with_t = 0
    for combination in combinations:
        set_three_computers = set()
        for connection in combination:
            comp1, comp2 = connection.split('-')
            set_three_computers.add(comp1)
            set_three_computers.add(comp2)
        if len(set_three_computers) == 3:
            number_of_3_sets += 1
            if any(computer.startswith("t") for computer in set_three_computers):
                number_of_3_sets_with_t += 1
    print(number_of_3_sets)
    print(number_of_3_sets_with_t)

    return number_of_3_sets_with_t


def compute_part_one_fast(file_name: str) -> int:
    connections = read_input_file(file_name)
    total_sets = set()
    for connection in connections:
        substring1, substring2 = connection.split("-")
        result1 = set(
            computer.replace("-", "").replace(substring1, "") for computer in connections if substring1 in computer)
        result2 = set(
            computer.replace("-", "").replace(substring2, "") for computer in connections if substring2 in computer)
        result3 = result1.intersection(result2)
        if len(result3) != 0:
            for result in result3:
                lan_party = (substring1, substring2, result)
                lan_party = tuple(sorted(list(lan_party)))  # sort the tuple to get rid of duplicates later
                # lan_party.sort()
                # lan_party = tuple(lan_party)
                total_sets.add(lan_party)

    number_start_with_t = 0
    for lan in total_sets:
        if any(computer.startswith("t") for computer in lan):
            number_start_with_t += 1

    print(f'{len(total_sets)= }')
    print(f'{number_start_with_t= }')

    return number_start_with_t


def compute_part_two(file_name: str) -> int:
    connections = read_input_file(file_name)
    edges = []
    for connection in connections:
        computer1, computer2 = connection.split('-')
        edge = (computer1, computer2)
        edges.append(edge)

    G = nx.Graph()
    G.add_edges_from(edges)
    # largest_cc = max(nx.connected_components(G), key=len)
    # print(largest_cc)

    cliques = list(nx.find_cliques(G))
    largest_fully_connected_component = max(cliques, key=len)
    largest_fully_connected_component.sort()
    print(f'{largest_fully_connected_component= }')
    pwd = ','.join(largest_fully_connected_component)
    print(f'{pwd= }')

    # Draw the graph
    nx.draw(G, with_labels=True, node_color='lightblue', node_size=50, font_size=6)

    # Display the graph
    plt.show()

    return pwd


if __name__ == '__main__':
    # print(f"Part I-slow: {compute_part_one_slow('input/input23.txt')}")
    print(f"Part I-fast: {compute_part_one_fast('input/input23.txt')}")
    print(f"Part II: {compute_part_two('input/input23.txt')}")
