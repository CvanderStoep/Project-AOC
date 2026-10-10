def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().split('\n\n')

    schematics = []
    keys = []
    locks = []
    for line in content:
        schematics.append(line.split())
    for schematic in schematics:
        if "##" in schematic[0]:
            locks.append(schematic)
        else:
            keys.append(schematic)

    return locks, keys


def key_lock_fit(key: list, lock: list) -> bool:
    cols = len(key[0])
    rows = len(key)

    def _convert_lock_to_numbers() -> list:
        lock_numbers = []
        for col in range(cols):
            height = 0
            for row in range(rows):
                if lock[row][col] == "#":
                    height += 1
                else:
                    break
            lock_numbers.append(height - 1)
        return lock_numbers

    def _convert_key_to_numbers() -> list:
        key_numbers = []
        for col in range(cols):
            height = 0
            for row in range(rows - 1, 0, -1):
                if key[row][col] == "#":
                    height += 1
                else:
                    break
            key_numbers.append(height - 1)
        return key_numbers

    lock_numbers = _convert_lock_to_numbers()
    key_numbers = _convert_key_to_numbers()
    sum_height = [lock + key for lock, key in zip(lock_numbers, key_numbers)]
    fits = all(height <= 5 for height in sum_height)

    return fits


def compute_part_one(file_name: str) -> int:
    locks, keys = read_input_file(file_name)
    total_fits = 0
    for lock in locks:
        for key in keys:
            if key_lock_fit(key, lock):
                total_fits += 1

    return total_fits


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input25.txt')}")
