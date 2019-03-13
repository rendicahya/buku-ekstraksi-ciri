import cv2
import numpy as np
from skimage import feature


def lbp(img):
    neighbors = np.array(((-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)))
    multiply = 1, 2, 4, 8, 16, 32, 64, 128
    h, w = img.shape[:2]
    output = np.zeros((h - 2, w - 2), np.uint8)

    for Y in range(1, h - 1):
        for X in range(1, w - 1):
            bin = np.zeros(len(neighbors), np.uint8)

            for i, n in enumerate(neighbors):
                x, y = (X, Y) + n
                bin[i] = 0 if img[y, x] < img[Y, X] else 1
                # print('%d : %d = %d' % (img[y, x], img[Y, X], bin[i]))

            output[Y - 1, X - 1] = np.dot(bin, multiply)
            print(bin)

    return np.pad(output, 1, 'constant')


if __name__ == '__main__':
    # img = cv2.imread('../teddy.jpg', 0)
    img = np.array([[118, 98, 112, 104],
                    [105, 80, 111, 101],
                    [64, 90, 94, 107],
                    [57, 84, 101, 90]])

    lbp1 = lbp(img)
    lbp2 = feature.local_binary_pattern(img, 8, 1)

    print(lbp1)
    print(lbp2)
    # cv2.imshow('Diva', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
