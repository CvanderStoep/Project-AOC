def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def make_disk_map(number: str) -> list:
    disk_map = [int(digit) for digit in number]
    return disk_map


def from_disk_map_to_disk(disk_map: list) -> list:
    disk = []
    id = 0
    counter = 0
    while True:
        disk.extend([id] * disk_map[counter])
        counter += 1
        if counter == len(disk_map):
            break
        disk.extend(['.'] * disk_map[counter])
        counter += 1
        id += 1
    return disk


def move_files(disk: list) -> list:
    counter = len(disk) - 1
    index = 0
    while True:
        index = disk.index('.')
        if index > counter:
            break
        # print(f'{index= }')
        number = disk[counter]
        if number != '.':
            disk[index], disk[counter] = disk[counter], disk[index]
        counter -= 1

    return disk


def find_consecutive_elements(lst, count):
    element = '.'
    for i in range(len(lst) - count + 1):
        if lst[i:i + count] == [element] * count:
            return i
    return -1  # Return -1 if the pattern is not found


# Example usage

def move_files_in_blocks(disk: list, disk_map: list) -> list:
    counter_disk = len(disk) - 1
    counter_disk_map = len(disk_map) - 1
    while True:
        id = disk[counter_disk]
        n_id = disk_map[counter_disk_map]
        index = find_consecutive_elements(disk, n_id)

        if index != -1 and index < counter_disk:
            for i in range(n_id):
                disk[index + i], disk[counter_disk - i] = disk[counter_disk - i], disk[index + i]
        counter_disk_map -= 1
        counter_disk = counter_disk - n_id - disk_map[counter_disk_map]  # move to the left, ignoring '.'
        counter_disk_map -= 1
        if id == 0:
            break

    return disk


def calc_checksum(disk: list) -> int:
    check_sum = 0
    for index, id in enumerate(disk):
        if id != '.':
            check_sum += index * id

    return check_sum


def compute_part_one(file_name: str) -> int:
    inputs = read_input_file(file_name)
    disk_map = make_disk_map(inputs[0])
    disk = from_disk_map_to_disk(disk_map)
    print(''.join(map(str, disk)))
    disk = move_files(disk)
    print(''.join(map(str, disk)))
    check_sum = calc_checksum(disk)
    print(f'{check_sum= }')
    return check_sum


def compute_part_two(file_name: str) -> int:
    inputs = read_input_file(file_name)
    disk_map = make_disk_map(inputs[0])
    disk = from_disk_map_to_disk(disk_map)
    print(''.join(map(str, disk)))
    disk = move_files_in_blocks(disk, disk_map)
    print(''.join(map(str, disk)))
    check_sum = calc_checksum(disk)
    print(f'{check_sum= }')
    return check_sum


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input9.txt')}")
    print(f"Part II: {compute_part_two('input/input9.txt')}")
