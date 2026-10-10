def read_input_file(file_name: str) -> str:
    with open(file_name) as f:
        return f.read().strip()


def dragon_curve(a: str) -> str:
    b = str(a)[::-1]
    b = b.replace('0', '-')
    b = b.replace('1', '0')
    b = b.replace('-', '1')
    a = str(a) + '0' + b
    return a


def calc_checksum(a: str) -> str:
    checksum = ''
    for i in range(0, len(a) - 1, 2):
        p1, p2 = a[i], a[i + 1]
        if p1 == p2:
            checksum += '1'
        else:
            checksum += '0'
    return checksum


def compute_part(file_name: str, length: int) -> str:
    a = read_input_file(file_name)
    print(f'{a= } {length= }')
    while len(a) < length:
        a = dragon_curve(a)
    a = a[:length]
    checksum = calc_checksum(a)
    while len(checksum) % 2 == 0:
        checksum = calc_checksum(checksum)

    return f'{checksum= }'


if __name__ == '__main__':
    print(f"Part I: {compute_part('input/input16.txt', length=272)}")
    print(f"Part II: {compute_part('input/input16.txt', length=35651584)}")
