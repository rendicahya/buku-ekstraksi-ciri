import numpy as np


def lbp(img):
    if img.ndim != 2:
        print('Citra harus berformat grayscale')

    neigh = np.array(((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1)))
    multiply = 1, 2, 4, 8, 16, 32, 64, 128


if __name__ == '__main__':
    lbp()
