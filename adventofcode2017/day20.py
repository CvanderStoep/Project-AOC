import re
from collections import defaultdict
from dataclasses import dataclass


def read_input_file(file_name: str) -> dict:
    with open(file_name) as f:
        content = f.read().splitlines()

    particles = dict()
    for i, line in enumerate(content):
        p = list(map(int, re.findall(r'(-?\d+)', line)))
        particles[i] = Point(p[0:3], p[3:6], p[6:])

    return particles

@dataclass
class Point:
    p: list[int]
    v: list[int]
    a: list[int]

    def update(self):
        self.v[0] += self.a[0]
        self.v[1] += self.a[1]
        self.v[2] += self.a[2]
        self.p[0] += self.v[0]
        self.p[1] += self.v[1]
        self.p[2] += self.v[2]

def manhattan_distance(p: Point, i: int= 0) -> int | None:
    if i == 0:
        return abs(p.p[0]) + abs(p.p[1]) + abs(p.p[2])
    if i == 1:
        return abs(p.v[0]) + abs(p.v[1]) + abs(p.v[2])
    if i == 2:
        return abs(p.a[0]) + abs(p.a[1]) + abs(p.a[2])

def remove_collisions(particles: dict):

    particle_count =defaultdict(int)
    for key, particle in particles.items():
        particle_count[tuple(particle.p)] += 1

    new_particles = dict()
    for key, particle in particles.items():
        if particle_count[tuple(particle.p)] == 1:
            new_particles[key] = particle

    particles = dict(new_particles)
    return particles


def compute_part_one(file_name: str) -> str:
    particles = read_input_file(file_name)
    print(particles)

    min_key = min(particles.keys(), key=lambda k: manhattan_distance(particles[k], 2))

    return f'{min_key= }'

def compute_part_two(file_name: str) -> str:
    particles = read_input_file(file_name)

    for _ in range(100):
        for key, particle in particles.items():
            particle.update()
        particles = remove_collisions(particles)

    return f'{len(particles)= }'


if __name__ == '__main__':
    file_path = 'input/input20.txt'
    print(f"Part I: {compute_part_one(file_path)}")
    print(f"Part II: {compute_part_two(file_path)}")