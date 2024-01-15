import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


matrix_a = np.random.randint(1, 10, size=(3, 3))
matrix_b = np.random.randint(1, 10, size=(3, 3))

# Display the original matrices
print("Matrix A:")
print(matrix_a)
print("\nMatrix B:")
print(matrix_b)

# Matrix addition
matrix_sum = np.add(matrix_a, matrix_b)
print("\nMatrix Addition (A + B):")
print(matrix_sum)

# Matrix multiplication
matrix_product = np.dot(matrix_a, matrix_b)
print("\nMatrix Multiplication (A * B):")
print(matrix_product)

# Matrix transposition
matrix_transpose = np.transpose(matrix_a)
print("\nMatrix Transposition (Transpose of A):")
print(matrix_transpose)

# Part 2: Geometric Transformations

# Original 2D points
original_points = np.array([[1, 1], [2, 3], [3, 1]])

# Scaling matrix
scaling_matrix = np.array([[2, 0], [0, 0.5]])

# Rotation matrix (45 degrees counterclockwise)
theta = np.radians(45)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])

# Apply transformations
scaled_points = np.dot(original_points, scaling_matrix)
rotated_points = np.dot(original_points, rotation_matrix)

# Combine original and transformed points into a DataFrame for easier visualization
data = np.concatenate((original_points, scaled_points, rotated_points), axis=1)
df = pd.DataFrame(data, columns=['X', 'Y', 'Scaled_X', 'Scaled_Y', 'Rotated_X', 'Rotated_Y'])

# Plot original and transformed points
plt.figure(figsize=(10, 5))

plt.scatter(df['X'], df['Y'], label='Original Points', color='blue')
plt.scatter(df['Scaled_X'], df['Scaled_Y'], label='Scaled Points', color='green')
plt.scatter(df['Rotated_X'], df['Rotated_Y'], label='Rotated Points', color='red')

plt.title('Geometric Transformations on 2D Points')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
