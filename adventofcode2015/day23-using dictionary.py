import re

# Initialize registers
registers = {'a': 1, 'b': 0}
position = 0

# Sample instruction containing 'jio'
instruction = "jio a, +2"
pattern = r'[+-]?\d+'

if 'jio' in instruction:
    reg_name = instruction[4]
    r = registers[reg_name]
    if r == 1:
        jump = int(re.findall(pattern, instruction)[0])
        position += jump
    else:
        position += 1

print(f"Final position: {position}")
print(f"Register a: {registers['a']}, Register b: {registers['b']}")

# Initialize registers
registers = {'a': 1, 'b': 0}
position = 0

# Sample instruction containing 'inc'
instruction = "inc a"

if 'inc' in instruction:
    reg_name = instruction[-1]
    registers[reg_name] += 1
    position += 1

print(f"Final position: {position}")
print(f"Register a: {registers['a']}, Register b: {registers['b']}")

