def find_number(r, c):
    return (r + c - 2) * (r + c - 1) // 2 + c

# Example: Find the number at row 4, column 2
r = 4
c = 3
number = find_number(r, c)

print(f"The number at row {r} and column {c} is {number}")
