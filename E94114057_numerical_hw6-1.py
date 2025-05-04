import numpy as np

A = np.array([
    [1.19, 2.11, -100, 1],
    [14.2, -0.112, 12.2, -1],
    [0, 100, -99.9, 1],
    [15.3, 0.110, -13.1, -1]
], dtype=float)

b = np.array([1.12, 3.44, 2.15, 4.16], dtype=float)

n = len(b)

for k in range(n - 1):
    max_row = np.argmax(abs(A[k:n, k])) + k
    if max_row != k:
        A[[k, max_row]] = A[[max_row, k]]
        b[[k, max_row]] = b[[max_row, k]]

    for i in range(k + 1, n):
        factor = A[i][k] / A[k][k]
        A[i, k:] -= factor * A[k, k:]
        b[i] -= factor * b[k]

x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

for i, xi in enumerate(x, 1):
    print(f"x{i} = {xi:.6f}")