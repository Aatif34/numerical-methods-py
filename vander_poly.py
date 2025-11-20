import numpy as np
def vandermonde_coeffs(A):
    x = A[:, 0]
    y = A[:, 1]

    v = np.vander(x, N = len(x), increasing = True)
    c = np.linalg.solve(v, y)
    return c
if __name__ == "__main__":
    filename = "input3.txt"
    A = np.loadtxt(filename)
    coeffs = vandermonde_coeffs(A)

    print("coeffs:", coeffs)

    s = np.sum(coeffs)
    print(f"\nSum S = {s:.6f}")