# z3 solver, pip install z3-solver
# dataclass
# optimize, constraints

import re
from z3 import *
from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    ingredients = []
    pattern = r'-?\d+'  # pattern for positive and negative integers
    for line in content:
        parts = line.split()
        name = parts[0][:-1]
        parts = re.findall(pattern, line)
        capacity = int(parts[0])
        durability = int(parts[1])
        flavor = int(parts[2])
        texture = int(parts[3])
        calories = int(parts[4])

        ingredient = Ingredient(name, capacity, durability, flavor, texture, calories)
        ingredients.append(ingredient)

    return ingredients


def compute_part(file_name: str, part=1) -> str:
    ingredients = read_input_file(file_name)
    print(ingredients)

    n = len(ingredients)
    s = Solver()
    teaspoons = [Int(f'ts{i}') for i in range(0, n)]
    for ts in teaspoons:
        s.add(ts >= 0)
        # s.add(ts <= 100)
    s.add(sum(teaspoons) == 100)

    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0

    for i in range(n):
        capacity += teaspoons[i] * ingredients[i].capacity
        durability += teaspoons[i] * ingredients[i].durability
        flavor += teaspoons[i] * ingredients[i].flavor
        texture += teaspoons[i] * ingredients[i].texture
        calories += teaspoons[i] * ingredients[i].calories

    # alternative, shorter functional
    # capacity = sum(teaspoons[i] * ingredients[i].capacity for i in range(n))

    if part == 2:
        s.add(calories == 500)

    capacity = If(capacity < 0, 0, capacity)
    durability = If(durability < 0, 0, durability)
    flavor = If(flavor < 0, 0, flavor)
    texture = If(texture < 0, 0, texture)

    objective = capacity * durability * flavor * texture

    optimize = Optimize()
    optimize.add(s.assertions())
    optimize.maximize(objective)

    if optimize.check() == sat:
        model = optimize.model()
        max_value = model.evaluate(objective)
        print(model)
        for ts in teaspoons:
            print(f"{ts} = {model.evaluate(ts)}")
        return f"Maximum value: {max_value}"
    else:
        return "No solution found"


if __name__ == '__main__':
    # print(f"Part I: {compute_part('input/input15.txt', part=1)}")
    print(f"Part II: {compute_part('input/input15.txt', part=2)}")
