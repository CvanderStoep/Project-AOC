from collections import defaultdict


def read_input_file(file_name: str) -> list:
    try:
        with open(file_name) as f:
            content = f.read().splitlines()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return []
    except IOError:
        print(f"Error: Could not read the file '{file_name}'.")
        return []


def process_instruction(registers: dict, instruction: str, maximum_intermediate_value: int) -> tuple[dict, int]:
    register1, modify_instruction, digit1, _, register2, comparison_operator, digit2 = instruction.split()
    condition_met = eval(str(registers[register2]) + comparison_operator + digit2)
    if condition_met:
        if modify_instruction == 'inc':
            registers[register1] += int(digit1)
        else:
            registers[register1] -= int(digit1)

    maximum_intermediate_value = max(maximum_intermediate_value, max(registers.values()))
    return registers, maximum_intermediate_value

def compute_part(file_name: str) -> None:
    registers = defaultdict(int)

    instructions = read_input_file(file_name)
    maximum_intermediate_register_value = 0
    for instruction in instructions:
        registers, maximum_intermediate_register_value = process_instruction(registers, instruction, maximum_intermediate_register_value)

    max_register_value = max(registers.values())

    print(f'partI: The maximum value of the register after all operations is: {max_register_value}')
    print(f'partII: The maximum value during the operations: {maximum_intermediate_register_value}')



if __name__ == '__main__':
    file_path = 'input/input8.txt'
    compute_part(file_path)
