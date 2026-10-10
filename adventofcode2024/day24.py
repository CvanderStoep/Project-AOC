def read_input_file(file_name: str) -> dict:
    with open(file_name) as f:
        content = f.read().split('\n\n')
    first_part = content[0].splitlines()
    second_part = content[1].splitlines()

    system_dictionary = dict()
    for line in first_part:
        gate, value = line.split(': ')
        system_dictionary[gate] = int(value)

    for line in second_part:
        connection, gate = line.split(' -> ')
        system_dictionary[gate] = connection

    return system_dictionary


def get_wire_value(system_dictionary: dict, value: str):
    if isinstance(system_dictionary[value], int):
        return system_dictionary[value]
    else:
        wire1, operator, wire2 = system_dictionary[value].split()
        match operator:
            case 'AND':
                return get_wire_value(system_dictionary, wire1) & get_wire_value(system_dictionary, wire2)
            case 'OR':
                return get_wire_value(system_dictionary, wire1) | get_wire_value(system_dictionary, wire2)
            case 'XOR':
                return get_wire_value(system_dictionary, wire1) ^ get_wire_value(system_dictionary, wire2)


def compute_part_one(file_name: str) -> int:
    system_dictionary = read_input_file(file_name)

    wires = system_dictionary.keys()
    wires = [wire for wire in wires if wire.startswith("z")]
    wires.sort(reverse=True)

    binary_number = ''
    for wire in wires:
        binary_number += str(get_wire_value(system_dictionary, wire))
    # print(f'{binary_number= }')
    decimal_number = int(binary_number, 2)
    # print(f'{decimal_number= }')

    return decimal_number


def compute_part_two(file_name: str) -> int:
    system_dictionary = read_input_file(file_name)

    wires = system_dictionary.keys()

    # for output_wire in wires:
    #     if not isinstance(system_dictionary[output_wire],int):
    #         print(output_wire)
    x_wires = [wire for wire in wires if wire.startswith("x")]
    x_wires.sort(reverse=True)
    y_wires = [wire for wire in wires if wire.startswith("y")]
    y_wires.sort(reverse=True)
    z_wires = [wire for wire in wires if wire.startswith("z")]
    z_wires.sort(reverse=True)

    x_binary = ''
    for wire in x_wires:
        x_binary += str(get_wire_value(system_dictionary, wire))
    x = int(x_binary, 2)
    print(f'{x_binary= } ({x})')

    y_binary = ''
    for wire in y_wires:
        y_binary += str(get_wire_value(system_dictionary, wire))
    y = int(y_binary, 2)
    print(f'{y_binary= } ({y})')

    bitwise_and = int(x_binary, 2) & int(y_binary, 2)

    z_binary = ''
    for wire in z_wires:
        z_binary += str(get_wire_value(system_dictionary, wire))
    z = int(z_binary, 2)
    print(f'{z_binary= } ({z})')

    print(f'{x} & {y} = {bitwise_and}, {z=  } ({bitwise_and == z})')

    return "not yet implemented"


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input24.txt')}")
    print(f"Part II: {compute_part_two('input/input24.txt')}")
