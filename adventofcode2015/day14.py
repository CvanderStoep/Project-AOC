# the plural of reindeer is reindeer, but I use reindeers for convenience.
from dataclasses import dataclass


@dataclass
class Reindeer:
    name: str
    speed: int
    fly_time: int
    rest_time: int
    distance: int = 0
    points: int = 0


def read_input_file(file_name: str) -> list:
    with open(file_name) as f:
        content = f.read().splitlines()

    reindeers = []
    for line in content:
        # Splitting the line by whitespace
        parts = line.split()

        # Extracting relevant data
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])

        # Creating a Reindeer object and adding it to the list
        reindeer = Reindeer(name, speed, fly_time, rest_time)
        reindeers.append(reindeer)

    return reindeers


def calculate_distance_travelled(speed, time, rest, seconds) -> int:
    # check the amount of full timeblocks (time + rest) has passed and correct for the remainder
    total_time = time + rest
    number_of_time_blocks = int(seconds / total_time)
    remaining_time = seconds - number_of_time_blocks * total_time
    remaining_time = min(remaining_time, time)
    distance = number_of_time_blocks * time * speed
    distance += remaining_time * speed

    return distance


def compute_part_one(file_name: str) -> int:
    reindeers = read_input_file(file_name)
    max_distance = 0
    for reindeer in reindeers:
        distance = calculate_distance_travelled(reindeer.speed, reindeer.fly_time, reindeer.rest_time, 2503)
        max_distance = max(max_distance, distance)
    print(f'{max_distance= }')

    return max_distance


def compute_part_two(file_name: str) -> int:
    reindeers = read_input_file(file_name)
    for time in range(1, 2504):
        max_distance = 0
        for reindeer in reindeers:
            distance = calculate_distance_travelled(reindeer.speed, reindeer.fly_time, reindeer.rest_time, time)
            max_distance = max(max_distance, distance)
            reindeer.distance = distance
        for reindeer in reindeers:
            if reindeer.distance == max_distance:
                reindeer.points += 1

    max_points = 0
    for reindeer in reindeers:
        max_points = max(max_points, reindeer.points)
    print(f'{max_points= }')

    return max_points


if __name__ == '__main__':
    print(f"Part I: {compute_part_one('input/input14.txt')}")
    print(f"Part II: {compute_part_two('input/input14.txt')}")
