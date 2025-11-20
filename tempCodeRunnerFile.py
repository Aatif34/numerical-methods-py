import numpy as np
def horner(c, x):
    result =0
    for coeff in reversed(c):
        result = result * x +coeff
    return result

if __name__ == "__main__":
    filename = "input1.txt"
    c = np.loadtxt(filename)

    x = 1.0427
    value = horner(c, x)
    print(f"{value:.6f}")