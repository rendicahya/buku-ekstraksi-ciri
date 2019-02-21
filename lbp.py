import cv2
import numpy as np


def lbp(img):
    if img.ndim != 2:
        print('Citra harus berformat grayscale')

    neighbors = np.array(((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, -1)))
    multiply = 1, 2, 4, 8, 16, 32, 64, 128
    h, w = img.shape[:2]
    output = np.zeros((h - 2, w - 2), np.uint8)

    for Y in range(1, h - 1):
        for X in range(1, w - 1):
            bin = np.zeros(neighbors.size, np.uint8)

            for i, n in enumerate(neighbors):
                y, x = (Y, X) + n
                bin[i] = 0 if img[y, x] < img[Y, X] else 1

            print(bin)
            return


if __name__ == '__main__':
    img = cv2.imread('diva.jpg', 0)
    lbp(img)

    # cv2.imshow('Diva', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
