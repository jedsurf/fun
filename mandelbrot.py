import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
max_iters=100


def mandelbrot(c, iters=max_iters):
    z = 0
    zn1 = lambda z : z**2 + c
    for i in range(iters):
        if np.abs(z.real) <= 2:
            z = zn1(z)
        else:
            return i
    return iters


v = np.arange(-2, 2, 0.01)
mtx = np.zeros([len(v), len(v)], dtype="complex")
for i in range(len(v)):
    for j in range(len(v)):
        mtx[i][j] = complex(v[i], v[j])
result = np.apply_along_axis(lambda x: [mandelbrot(i) for i in x], 0, mtx)
with plt.style.context("dark_background"):
    plt.rcParams['figure.dpi'] = 300
    plt.scatter(mtx.real, mtx.imag, c=result, cmap="plasma")
    plt.show()
