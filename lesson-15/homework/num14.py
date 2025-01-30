import numpy as np

# Define a 3x3 matrix A
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

# Define a 3x1 column vector b
b = np.array([
    [8],
    [-11],
    [-3]
])

# Solve the linear system Ax = b
x = np.linalg.solve(A, b)

print("Matrix A (3x3):")
print(A)
print("\nColumn Vector b (3x1):")
print(b)
print("\nSolution x (3x1):")
print(x)