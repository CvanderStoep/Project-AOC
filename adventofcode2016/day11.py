from collections import deque

# if all elements are above floor-0, no need to return here.
# needed for part II, otherwise it will take forever to run.
completed_floors = set()


def is_valid(state):
    elevator, items = state
    if elevator in completed_floors:
        return False
    for i in range(len(items) // 2):
        chip_floor = items[2 * i]
        generator_floor = items[2 * i + 1]
        # If the chip is not on the same floor as its generator
        if chip_floor != generator_floor:
            # Check if any generator is on the same floor as the chip
            for j in range(len(items) // 2):
                if chip_floor == items[2 * j + 1]:
                    return False
    return True


def generate_moves(state):
    elevator, items = state
    possible_moves = []
    # Move one item up or down
    for i in range(len(items)):
        for move in [-1, 1]:
            new_elevator = elevator + move
            if 0 <= new_elevator < 4:
                new_items = list(items)
                new_items[i] += move
                if new_items[i] == new_elevator:
                    new_state = (new_elevator, tuple(new_items))
                    if is_valid(new_state):
                        possible_moves.append(new_state)
    # Move two items up or down
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            for move in [-1, 1]:
                new_elevator = elevator + move
                if 0 <= new_elevator < 4:
                    new_items = list(items)
                    new_items[i] += move
                    new_items[j] += move
                    if new_items[i] == new_items[j] == new_elevator:
                        new_state = (new_elevator, tuple(new_items))
                        if is_valid(new_state):
                            possible_moves.append(new_state)
    return possible_moves


def are_all_elements_greater_than(state, threshold):
    elevator, items = state
    return all(item > threshold for item in items)


def bfs(start, goal):
    queue = deque([(start, 0, [start])])
    visited = set()
    visited.add(start)

    while queue:
        current_state, steps, path = queue.popleft()
        if are_all_elements_greater_than(current_state, 0) and 0 not in completed_floors:
            completed_floors.add(0)
        if current_state == goal:
            print("Path to goal state:")
            for state in path:
                print(state)
            return steps
        for move in generate_moves(current_state):
            if move not in visited:
                visited.add(move)
                queue.append((move, steps + 1, path + [move]))
    return -1


# # Example
# initial_state = (0, (0, 1, 0, 2))  # (elevator, (HM, HG, LM, LG))
# goal_state = (3, (3, 3, 3, 3))

# part I
initial_state = (0, (0, 0, 0, 0, 2, 1, 1, 1, 1, 1))  # (elevator, (SM, SG, PM, PG, TM, TG, RM, RG, CM, CG))
goal_state = (3, (3, 3, 3, 3, 3, 3, 3, 3, 3, 3))

# # part II
# initial_state = (0, (0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0))  # (elevator, (SM, SG, PM, PG, TM, TG, RM, RG, CM, CG))
# goal_state = (3, (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3))

steps = bfs(initial_state, goal_state)
print(f"Minimum steps required: {steps}")
