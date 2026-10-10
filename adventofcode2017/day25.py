import re
from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, Tuple

# Constants for directions
LEFT = 'left'
RIGHT = 'right'

@dataclass
class State:
    name: str
    write: Tuple[int, int]
    move: Tuple[str, str]
    next: Tuple[str, str]

def read_input_file(file_name: str) -> Tuple[Dict[str, State], int]:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    blueprint = {}
    steps = int(re.search(r'(\d+)', content[0].splitlines()[1]).group(1))

    for block in content[1:]:
        lines = block.splitlines()
        state = lines[0][-2]
        write = (int(lines[2][-2]), int(lines[6][-2]))
        move = (lines[3].split()[-1][:-1], lines[7].split()[-1][:-1])
        next_state = (lines[4][-2], lines[8][-2])
        blueprint[state] = State(state, write, move, next_state)

    return blueprint, steps

def process_step(position: int, blueprint: Dict[str, State], state: str, turing: defaultdict) -> Tuple[int, str]:
    current_value = turing[position]
    write_value = blueprint[state].write[current_value]
    move_direction = blueprint[state].move[current_value]
    next_state = blueprint[state].next[current_value]

    turing[position] = write_value
    position += -1 if move_direction == LEFT else 1

    return position, next_state

def compute_part_one(file_name: str) -> str:
    blueprint, steps = read_input_file(file_name)
    turing = defaultdict(int)
    position, state = 0, 'A'

    for _ in range(steps):
        position, state = process_step(position, blueprint, state, turing)

    return f'{sum(turing.values()) = }'

def compute_part_two(file_name: str) -> str:
    # Placeholder for Part Two implementation
    print("Part two not yet implemented")
    return ""

if __name__ == '__main__':
    file_path = 'input/input25.txt'
    print(f"Part I: {compute_part_one(file_path)}")
