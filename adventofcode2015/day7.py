def read_input_file(file_name: str) -> dict:
    with open(file_name) as f:
        content = f.read().splitlines()

    circuit = dict()
    for line in content:
        left, right = line.split(' -> ')
        circuit[right] = left

    return circuit

# def build_circuit(circuit: dict, wire: str):
#     """
#     below code will work, but way too slow, as it needs to recalculate every time.
#     optimized code further down.
#     """
#     if wire not in circuit:
#         return int(wire)
#
#     operation = circuit[wire].split()
#     if len(operation) == 1:  # isinstance integer
#         # pattern = r'\d+'
#         # value = re.findall(pattern, operation[0])
#         if operation[0].isdigit():
#             return int(operation[0])
#         else:
#             return build_circuit(circuit, operation[0])
#     if operation[0] == 'NOT':
#         return (~build_circuit(circuit, operation[1])) % 65536
#     if operation[1] == 'AND':
#         return build_circuit(circuit, operation[0]) & build_circuit(circuit, operation[2])
#     if operation[1] == 'OR':
#         return build_circuit(circuit, operation[0]) | build_circuit(circuit, operation[2])
#     if operation[1] == 'LSHIFT':
#         return build_circuit(circuit, operation[0]) << int(operation[2])
#     if operation[1] == 'RSHIFT':
#         return build_circuit(circuit, operation[0]) >> int(operation[2])


def build_circuit(circuit: dict, wire: str):
    """the original dictionary circuit will be overwritten"""
    if wire not in circuit:
        return int(wire)

    if isinstance(circuit[wire], int):
        return circuit[wire]

    operation = circuit[wire].split()

    if len(operation) == 1:
        value = int(operation[0]) if operation[0].isdigit() else build_circuit(circuit, operation[0])
        circuit[wire] = value
        return value

    if operation[0] == 'NOT':
        value = (~build_circuit(circuit, operation[1])) % 65536
        circuit[wire] = value
        return value

    op1 = build_circuit(circuit, operation[0])
    op2 = build_circuit(circuit, operation[2]) if not operation[2].isdigit() else int(operation[2])

    if operation[1] == 'AND':
        value = op1 & op2
    elif operation[1] == 'OR':
        value = op1 | op2
    elif operation[1] == 'LSHIFT':
        value = op1 << op2
    elif operation[1] == 'RSHIFT':
        value = op1 >> op2
    circuit[wire] = value
    return value


def compute_part_one(file_name: str) -> int:
    circuit = read_input_file(file_name)
    for wire in ['a']:
        wire_a_signal = build_circuit(circuit, wire)

    return wire_a_signal


def compute_part_two(file_name: str) -> int:
    """
    Now, take the signal you got on wire a,
    override wire b to that signal,
    and reset the other wires (including wire a).
    What new signal is ultimately provided to wire a?
    """
    circuit = read_input_file(file_name)
    wire_a_signal = build_circuit(circuit, wire='a')

    circuit = read_input_file(file_name)
    circuit['b'] = wire_a_signal

    wire_a_signal = build_circuit(circuit, wire='a')

    return wire_a_signal


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input7.txt')}")
    print(f"Part II: {compute_part_two('input/input7.txt')}")
