import matplotlib.pyplot as plt
import numpy as np

def visualize_maze(maze):
    n, m = maze.shape
    fig, ax = plt.subplots()
    for x in range(n):
        for y in range(m):
            if maze[x, y] == 1:
                rect = plt.Rectangle([y, n - x - 1], 1, 1, color='black')
                ax.add_patch(rect)
    plt.xlim(0, m)
    plt.ylim(0, n)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis('off')
    plt.show()

maze = np.array([
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
])

visualize_maze(maze)

# import numpy as np
# import matplotlib.pyplot as plt

# Create a 5x5 matrix
matrix = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20],
                   [21, 22, 23, 24, 25]])

# Visualize the matrix
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
plt.title('Matrix Visualization')
plt.show()

