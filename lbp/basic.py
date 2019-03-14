import cv2
import numpy as np
from skimage import feature


def lbp(img):
    img = np.pad(img, 1, 'constant', constant_values=0)
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
            # print('{} {} {}'.format(img[Y,X], bin, output[Y - 1, X - 1]))

    return output


if __name__ == '__main__':
    # img = cv2.imread('../teddy.jpg', 0)
    img = np.array([[120, 180, 190, 170],
                    [110, 150, 240, 220],
                    [100, 140, 210, 180],
                    [120, 160, 130, 240]])

    print(img)

    lbp1 = lbp(img)
    print(lbp1)

    lbp2 = feature.local_binary_pattern(img, 8, 1)
    print(lbp2)

    # cv2.imshow('Diva', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
