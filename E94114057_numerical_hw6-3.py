import numpy as np

def crout_tridiagonal(a, b, c, d):
    n = len(d)
    L = np.zeros(n)
    U = np.zeros(n-1)
    y = np.zeros(n)
    x = np.zeros(n)

    L[0] = b[0]
    for i in range(1, n):
        U[i-1] = a[i-1] / L[i-1]
        L[i] = b[i] - U[i-1] * c[i-1]

    y[0] = d[0]
    for i in range(1, n):
        y[i] = d[i] - U[i-1] * y[i-1]

    x[-1] = y[-1] / L[-1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - c[i] * x[i+1]) / L[i]

    return x

a = [-1, -1, -1]         
b = [3, 3, 3, 3]         
c = [-1, -1, -1]          
d = [2, 3, 4, 1]        

solution = crout_tridiagonal(a, b, c, d)
print("\nSolution x:\n", np.round(solution, 6))
