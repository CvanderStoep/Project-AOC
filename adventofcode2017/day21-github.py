def parse_input(file_name):
    rules = {}
    with open(file_name) as f:
        content = f.read().strip()

    for line in content.split('\n'):
        # print(line)
        pattern, result = line.split(' => ')
        rules[tuple(pattern.split('/'))] = tuple(result.split('/'))
    print(rules)
    return rules

def rotate(pattern):
    return tuple(''.join(row[i] for row in reversed(pattern)) for i in range(len(pattern)))

def flip(pattern):
    return tuple(row[::-1] for row in pattern)

def get_variations(pattern):
    variations = set()
    for _ in range(4):
        pattern = rotate(pattern)
        variations.add(pattern)
        variations.add(flip(pattern))
    return variations

def enhance(grid, rules):
    size = len(grid)
    if size % 2 == 0:
        step = 2
    else:
        step = 3

    new_size = size // step * (step + 1)
    new_grid = [[''] * new_size for _ in range(new_size)]

    for i in range(0, size, step):
        for j in range(0, size, step):
            block = tuple(grid[x][j:j+step] for x in range(i, i+step))
            for variation in get_variations(block):
                if variation in rules:
                    result = rules[variation]
                    break
            for x in range(step + 1):
                for y in range(step + 1):
                    new_grid[i // step * (step + 1) + x][j // step * (step + 1) + y] = result[x][y]

    return [''.join(row) for row in new_grid]

def count_on_pixels(grid):
    return sum(row.count('#') for row in grid)

def main(input_data, iterations):
    rules = parse_input(input_data)
    grid = ['.#.', '..#', '###']

    for _ in range(iterations):
        grid = enhance(grid, rules)

    return count_on_pixels(grid)

# Example usage:
iterations = 5
file_path = 'input/input21.txt'
# read_input_file(file_path)
print(main(file_path, iterations))
