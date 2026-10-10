from collections import deque

def get_circular_position(circular_list: list, position: int) -> int:
    return position%len(circular_list)

def compute_part_one() -> str:
    steps = 301
    size = 2017
    position = 0
    circular_buffer = [0]
    for i in range(1,size+1):
        position = get_circular_position(circular_buffer,position + steps) + 1
        # circular_buffer = circular_buffer[:position] + [i] + circular_buffer[position:]
        circular_buffer.insert(position,i)
    index_2017 = circular_buffer.index(size)
    print(circular_buffer[index_2017-3: index_2017+3])

    return f'{circular_buffer[index_2017 + 1]= }'

def compute_part_two() -> str:
    steps = 301
    size = 50000000
    circular_buffer = deque([0])
    for i in range(1, size + 1):
        circular_buffer.rotate(-steps)
        circular_buffer.append(i)

    return f'{circular_buffer[circular_buffer.index(0) + 1] }'


if __name__ == '__main__':
    print(f"Part I: {compute_part_one()}")
    print(f"Part II: {compute_part_two()}")