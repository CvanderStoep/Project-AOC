import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def process_instruction(instruction: str, light_grid: dict) -> None:
    pattern = r'\d+'
    xb, yb, xe, ye = map(int, re.findall(pattern, instruction))

    if instruction.startswith('turn on'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] = 1
    if instruction.startswith('turn off'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] = 0
    if instruction.startswith('toggle'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] = 1 - light_grid[(x, y)]


def process_instruction_two(instruction: str, light_grid: dict) -> None:
    pattern = r'\d+'
    xb, yb, xe, ye = map(int, re.findall(pattern, instruction))

    if instruction.startswith('turn on'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] += 1
    if instruction.startswith('turn off'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] = max(0, light_grid[(x, y)] - 1)
    if instruction.startswith('toggle'):
        for x in range(xb, xe + 1):
            for y in range(yb, ye + 1):
                light_grid[(x, y)] += 2


def compute_part(file_name: str, function) -> int:
    # function call to either process_instruction() or process_instruction_two()
    light_grid = dict()
    for x in range(1000):
        for y in range(1000):
            light_grid[(x, y)] = 0
    instructions = read_input_file(file_name)
    for instruction in instructions:
        function(instruction, light_grid)

    return sum(light_grid.values())


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input6.txt', process_instruction)}")
    print(f"Part II: {compute_part('input/input6.txt', process_instruction_two)}")
