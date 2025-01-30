import numpy as np

matrix = np.random.rand(5, 5)

normalized_matrix = (matrix-np.min(matrix))/(np.max(matrix) - np.min(matrix))

print("Original matrix:\n", matrix)
print("Normalized matrix:\n", normalized_matrix)