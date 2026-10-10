import numpy as np
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Define the maze as a numpy array
maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])


# Define the heuristic function for A* (Manhattan distance)
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# Implement the A* algorithm
def astar(maze, start, goal):
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    open_heap = []

    heappush(open_heap, (fscore[start], start))

    while open_heap:
        current = heappop(open_heap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + 1

            if 0 <= neighbor[0] < maze.shape[0]:
                if 0 <= neighbor[1] < maze.shape[1]:
                    if maze[neighbor[0]][neighbor[1]] == 1:
                        continue
                else:
                    continue
            else:
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_heap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(open_heap, (fscore[neighbor], neighbor))

    return False


# Define start and goal points
start = (1, 1)
goal = (5, 8)

# Find the path
path = astar(maze, start, goal)
path = path[::-1]  # Reverse the path to start-to-goal order


# Function to visualize the maze with the path
def visualize_maze_with_path(maze, path):
    n, m = maze.shape
    fig, ax = plt.subplots()
    for x in range(n):
        for y in range(m):
            if maze[x, y] == 1:
                rect = plt.Rectangle([y, n - x - 1], 1, 1, color='black')
                ax.add_patch(rect)
            elif (x, y) in path:
                rect = plt.Rectangle([y, n - x - 1], 1, 1, color='green')
                ax.add_patch(rect)
    plt.xlim(0, m)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.title('Maze with Path')
    plt.show()

# Visualize the maze and the found path
visualize_maze_with_path(maze, path)
