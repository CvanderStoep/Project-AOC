import numpy as np
def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split(',')
    # content = list(map(int, content))


    return content

def process_list(lst: list, l, pos):
    array_length = len(lst)
    new_array = lst.copy()
    for i in range(l):
        new_array[(pos + i) % array_length] = lst[(pos + l -i -1) % array_length]
    return new_array


def compute_part_one(file_name: str) -> str:
    lengths = read_input_file(file_name)
    lst = list(range(256))
    skip = 0
    pos = 0
    for l in lengths:
        lst = process_list(lst, l, pos)
        pos += (l + skip)
        pos = pos % len(lst)
        skip += 1

    return f'{lst[0] * lst[1]= }'

def compute_part_two(file_name: str) -> str:
    lengths = read_input_file(file_name)
    s = ','.join(map(str,lengths))
    lengths = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    lst = list(range(256))
    skip = 0
    pos = 0
    for _ in range(64):
        for l in lengths:
            lst = process_list(lst, l, pos)
            pos += (l + skip)
            pos = pos % len(lst)
            skip += 1
    arr = np.array(lst)
    return ''.join(hex(x)[2:].zfill(2) for x in np.bitwise_xor.reduce(arr.reshape(16, 16), axis=1))

if __name__ == '__main__':
    file_path = 'input/input10.txt'
    # print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")