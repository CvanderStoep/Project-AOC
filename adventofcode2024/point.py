import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# Example usage
point1 = Point(3, 5)
point2 = Point(2, 4)

sum_points = point1 + point2
diff_points = point1 - point2

print("Sum of points:", sum_points)  # Output: Point(5, 9)
print("Difference of points:", diff_points)  # Output: Point(1, 1)

print(point1.x)

# Example coordinates
coord1 = np.array([3, 5])
coord2 = np.array([2, 4])

# Direct addition of NumPy arrays
result = coord1 + coord2

print("Sum of coordinates:", result)  # Output: [5 9]
print(result[0])
x, y = result
print(y)
print(y == int(y))
