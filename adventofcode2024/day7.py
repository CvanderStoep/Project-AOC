import itertools


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    # content = list(map(int, content))

    return content


def process_input_line(inputs: str) -> (int, list):
    answer, numbers = inputs.split(":")
    numbers = numbers.split()
    answer = int(answer)
    numbers = list(map(int, numbers))
    return answer, numbers


def generate_combinations(length):
    letters = ['+', '*']
    return [''.join(combination) for combination in itertools.product(letters, repeat=length)]


def generate_combinations_two(length):
    letters = ['+', '*', '|']
    return [''.join(combination) for combination in itertools.product(letters, repeat=length)]


def generate_expression(numbers, operators) -> str:
    # [16, 18, 24] '*+' -> '16 * 18 + 24'
    expression = ''
    for index, operator in enumerate(operators):
        expression = expression + str(numbers[index]) + ' ' + operator + ' '
    expression = expression + str(numbers[-1])
    return expression


def eval_left_to_right(expression):
    # '16 * 18 + 24' -> 312
    tokens = expression.split()
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        next_number = int(tokens[i + 1])
        if operator == '+':
            result += next_number
        elif operator == '*':
            result *= next_number
        elif operator == "|":  # 57 | 12 -> 5712
            result = int(str(result) + str(next_number))
        i += 2
    return result


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    total_calibration_result = 0
    for line in inputs:
        answer, numbers = process_input_line(line)
        combinations = generate_combinations(len(numbers) - 1)
        for combination in combinations:
            expression = generate_expression(numbers, combination)
            outcome = eval_left_to_right(expression)
            if outcome == answer:
                total_calibration_result += outcome
                print(f'{expression= }, {outcome= }')
                break

    return total_calibration_result


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    total_calibration_result = 0
    for line in inputs:
        answer, numbers = process_input_line(line)
        combinations = generate_combinations_two(len(numbers) - 1)
        for combination in combinations:
            expression = generate_expression(numbers, combination)
            outcome = eval_left_to_right(expression)
            if outcome == answer:
                total_calibration_result += outcome
                print(f'{expression= }, {outcome= }')
                break

    return total_calibration_result


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input7.txt')}")
    print(f"Part II: {compute_part_two('input/input7.txt')}")
