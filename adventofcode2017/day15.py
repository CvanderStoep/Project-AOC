from tqdm import tqdm

def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = list(map(int, content))


    return content

def calculate_next_value(generator: int, factor: int) -> int:
    generator = generator * factor % 2147483647

    return generator

def compare_lowest_bit(number1: int, number2: int):
    return number1 & (2**16 -1) ==number2 & (2**16 -1)


def compute_part_one() -> str:
    generator_a, generator_b = 699, 124
    factor_a, factor_b = 16807, 48271

    total_matches = 0
    for _ in tqdm(range(40_000_000)):
        generator_a = calculate_next_value(generator_a, factor_a)
        generator_b = calculate_next_value(generator_b, factor_b)
        if compare_lowest_bit(generator_a, generator_b):
            total_matches += 1

    return f'{total_matches= }'


def compute_part_two() -> str:
    generator_a, generator_b = 699, 124
    factor_a, factor_b = 16807, 48271

    total_matches = 0
    for _ in tqdm(range(5_000_000)):
        while True:
            generator_a = calculate_next_value(generator_a, factor_a)
            if generator_a % 4 == 0:
                break

        while True:
            generator_b = calculate_next_value(generator_b, factor_b)
            if generator_b % 8 == 0:
                break

        if compare_lowest_bit(generator_a, generator_b):
            total_matches += 1

    return f'{total_matches= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one()}")
    print(f"Part II: {compute_part_two()}")