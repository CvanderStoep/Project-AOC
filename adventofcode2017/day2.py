from itertools import permutations, combinations


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        return [list(map(int, line.split('\t'))) for line in f.read().splitlines()]


def calculate_checksum(spreadsheet: list) -> int:
    return sum(max(line) - min(line) for line in spreadsheet)


def divide_evenly(spreadsheet):
    return sum(n1 // n2 for line in spreadsheet
               for n1, n2 in permutations(line, 2)
               if n1 % n2 == 0)


def compute_part_one(file_name: str) -> str:
    spreadsheet = read_input_file(file_name)
    print(spreadsheet)
    checksum = calculate_checksum(spreadsheet)

    return f'{checksum= }'

def compute_part_two(file_name: str) -> str:
    spreadsheet = read_input_file(file_name)
    sum_rows = divide_evenly(spreadsheet)

    return f'{sum_rows= }'



if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input2.txt')}")
    print(f"Part II: {compute_part_two('input/input2.txt')}")


## alternative implementation found on reddit:
def digits(string: str):
    return [int(n) for n in string.split()]

with open('input/input2.txt') as fp:
    rows = [digits(line) for line in fp.read().strip().splitlines()]

print(sum(b-a for a, *_, b in map(sorted, rows)))
print(sum(b//a for row in rows for a, b in combinations(sorted(row), 2) if b%a==0))