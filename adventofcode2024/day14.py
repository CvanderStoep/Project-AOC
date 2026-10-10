from dataclasses import dataclass
import re


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    return content


def transform_input(content: list) -> list:
    robots = []
    for line in content:
        x, y, vx, vy = map(int, re.findall(r'-?\d+', line))
        robots.append(Robot(x, y, vx, vy))

    return robots


@dataclass
class Robot:
    x: int = 0
    y: int = 0
    vx: int = 0
    vy: int = 0


def print_tiles(robots, rows, cols) -> None:
    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for robot in robots:
        x = robot.x % cols
        y = robot.y % rows
        grid[y][x] += 1

    print('---')
    for row in grid:
        for symbol in row:
            if symbol == 0:
                print('.', end='')
            else:
                print('#', end='')
        print()


def update_robot_location(robot: Robot) -> None:
    robot.x += robot.vx
    robot.y += robot.vy


def count_robots(robots: list, rows: int, cols: int) -> int:
    q1, q2, q3, q4 = 0, 0, 0, 0
    mid_x = cols // 2
    mid_y = rows // 2

    for robot in robots:
        robot.x = robot.x % cols
        robot.y = robot.y % rows
        if mid_x < robot.x < cols and 0 <= robot.y < mid_y:
            q1 += 1
        if 0 <= robot.x < mid_x and 0 <= robot.y < mid_y:
            q2 += 1
        if mid_x < robot.x < cols and mid_y < robot.y < rows:
            q4 += 1
        if 0 <= robot.x < mid_x and mid_y < robot.y < rows:
            q3 += 1

    print(q1, q2, q3, q4)

    return q1 * q2 * q3 * q4


def find_tree(robots: list, rows: int, cols: int) -> bool:
    grid = [["." for _ in range(cols)] for _ in range(rows)]

    for robot in robots:
        x = robot.x % cols
        y = robot.y % rows
        grid[y][x] = "#"

    for row in grid:
        line = ''.join(row)
        if "##########" in line:
            print('found')
            print_tiles(robots, rows, cols)
            return True

    return False


def compute_part_one(file_name: str) -> int:
    content = read_input_file(file_name)
    robots = transform_input(content)
    rows, cols = 103, 101
    for i in range(1, 1001):
        for robot in robots:
            update_robot_location(robot)

    safety_factor = count_robots(robots, rows, cols)
    return safety_factor


def compute_part_two(file_name: str) -> int:
    content = read_input_file(file_name)
    robots = transform_input(content)
    rows, cols = 103, 101
    for i in range(1, 10001):
        # print(i)
        for robot in robots:
            update_robot_location(robot)
        if find_tree(robots, rows, cols):
            break
    return i


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input14.txt')}")
    print(f"Part II: {compute_part_two('input/input14.txt')}")
