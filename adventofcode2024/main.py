import itertools

# Define the list of 8 numbers
numbers = list(range(10))
print(numbers)

# Find all possible combinations of 8 elements (which is just the entire list)
comb = numbers

# Generate all ways to split them into 4 distinct pairs
all_pairs = list(itertools.combinations(comb, 2))
valid_combinations = []

# Find all unique sets of 4 pairs with no repeating elements
for combination in itertools.combinations(all_pairs, 4):
    flat_list = [item for sublist in combination for item in sublist]
    if len(set(flat_list)) == 8:  # Ensure there are no repeated elements
        valid_combinations.append(combination)

# Print the valid combinations of 4 distinct pairs
# for vc in valid_combinations:
#     print(vc)

print(len(valid_combinations))
