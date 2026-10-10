import itertools


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = list(map(int, content))

    return content


def prune(secret_number: int) -> int:
    return secret_number % 16777216


def mix(secret_number: int, number: int) -> int:
    number = number ^ secret_number

    return number


def find_sequence(lst, seq):
    seq_length = len(seq)
    for i in range(len(lst) - seq_length + 1):
        if lst[i:i + seq_length] == seq:
            return i  # Return the starting index of the sequence
    return -1  # Return -1 if the sequence is not found


def generate_next_number(secret_number: int) -> int:
    # result = secret_number * 64
    result = secret_number << 6
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)

    # result = int(secret_number / 32)
    result = secret_number >> 5
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)

    # result = secret_number * 2048
    result = secret_number << 11
    secret_number = mix(secret_number, result)
    secret_number = prune(secret_number)

    return secret_number


def compute_part_one(file_name: str) -> int:
    secret_numbers = read_input_file(file_name)
    # print(secret_numbers)

    total_secret_numbers = 0
    for secret_number in secret_numbers:
        secrets = [secret_number]
        for _ in range(10):
            secret_number = generate_next_number(secret_number)
            secrets.append(secret_number)
        total_secret_numbers += secret_number

    # print(f'{total_secret_numbers= }')
    return total_secret_numbers


def compute_part_two(file_name: str) -> int:
    # way too slow, see day22-2 instead for a much faster algorithm

    secret_numbers = read_input_file(file_name)
    print(secret_numbers)
    combinations = itertools.product(range(-9, 10), repeat=4)
    max_bananas = 0
    i = 0
    for combo in combinations:
        # i += 1
        # if i % 100 == 0:
        #     print(i)
        sequence = list(combo)
        # sequence = [0, 2, -2, 2]
        total_bananas = 0
        for secret_number in secret_numbers:
            secrets = [secret_number]
            for _ in range(2000):
                secret_number = generate_next_number(secret_number)
                secrets.append(secret_number)

            last_digits = []
            for secret in secrets:
                last_digits.append(secret % 10)

            changes = []
            for pos in range(len(last_digits) - 1):
                changes.append(last_digits[pos + 1] - last_digits[pos])

            index = find_sequence(changes, sequence)
            if index == -1:
                # print('no solution found')
                banana_price = 0
            else:
                banana_price = last_digits[index + 4]
            total_bananas += banana_price
        if total_bananas > max_bananas:
            max_bananas = total_bananas
            print(sequence, max_bananas)
    return max_bananas


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input22.txt')}")
    print(f"Part II: {compute_part_two('input/input22.txt')}")
    import itertools
