def generate_spiral(n):
    # x points to the right, y points up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 0  # Start with moving right

    x, y = 0, 0  # Starting at the center
    visited = {(x, y): 1}  # Track visited coordinates, initializing (0, 0)

    for i in range(2, n + 1):
        # Move in the current direction
        dx, dy = directions[direction_index]
        x, y = x + dx, y + dy

        # Check if a left turn is needed
        left_index = (direction_index + 1) % 4  # Determine the left direction
        left_dx, left_dy = directions[left_index]
        if (x + left_dx, y + left_dy) not in visited:
            direction_index = left_index  # Turn left

        # Mark the current cell as visited
        visited[(x, y)] = i

    return visited



def get_keys_by_value(d, value):
    """
    Retrieve all keys in the dictionary 'd' that correspond to the specified 'value'.

    Parameters:
        d (dict): The dictionary to search.
        value: The value to look for.

    Returns:
        list: A list of keys that match the specified value. If no keys are found, the list will be empty.
    """
    return [key for key, val in d.items() if val == value]

# Example usage
value_to_find = 368078
grid = generate_spiral(value_to_find)

keys = get_keys_by_value(grid, value_to_find)
print(f"Keys corresponding to value {value_to_find}: {keys}")



