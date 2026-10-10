def read_input_file(file_name: str) -> int:
    with open(file_name) as f:
        content = f.read().splitlines()
    content = list(map(int, content))

    return content[0]


def calculate_circular_sum(number: int) -> int:
    digits = str(number)
    circular_sum = 0
    length = len(digits)
    for i in range(length):
        if digits[i] == digits[(i+1)%length]:
            circular_sum += int(digits[i])

    return circular_sum

def calculate_circular_sum_half(number: int) -> int:
    digits = str(number)
    circular_sum = 0
    length = len(digits)
    for i in range(length):
        if digits[i] == digits[(i+length//2)%length]:
            circular_sum += int(digits[i])

    return circular_sum

def compute_part(file_name: str, sum_function) -> str:
    number = read_input_file(file_name)
    circular_sum = sum_function(number)

    return f'{circular_sum= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input1.txt', sum_function=calculate_circular_sum)}")
    print(f"Part II: {compute_part('input/input1.txt', sum_function=calculate_circular_sum_half)}")
