import numpy as np

def newton_sum(A):
    x = A[:, 0]
    y = A[:, 1]
    n = len(x)

    # Create Divided Difference (DD) table
    DD = np.zeros((n, n))
    DD[:, 0] = y  # first column is y

    for j in range(1, n):
        for i in range(n - j):
            DD[i, j] = (DD[i + 1, j - 1] - DD[i, j - 1]) / (x[i + j] - x[i])

    coeffs = DD[0, :]  # top row → Newton coefficients
    s = np.sum(coeffs)
    return s


if __name__ == "__main__":
    filename = "input_txt.txt"
    A = np.loadtxt(filename)
    s = newton_sum(A)
    print(f"{s:.6f}")
