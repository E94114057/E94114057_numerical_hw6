import numpy as np

A = np.array([
    [4, 1, -1, 0],
    [1, 3, -1, 0],
    [-1, -1, 6, 2],
    [0, 0, 2, 5]
], dtype=float)

A_inv = np.linalg.inv(A)
print("Inverse of matrix A:\n")
print(np.round(A_inv, 6))
