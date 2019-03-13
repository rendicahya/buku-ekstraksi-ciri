from math import sin, cos, pi

import cv2
import numpy as np

P = 12
R = 1.5
pts = []
w = int(R * 2 * 100 + 20)
img = np.zeros((w, w), np.uint8)

for p in range(P):
    m = 2 * pi * p / P
    x = -R * sin(m)
    y = R * cos(m)

    img[int((x * 100) + (w / 2)), int((y * 100) + (w / 2))] = 255
    pts.append((x, y))

cv2.imshow('LBP', img)
cv2.waitKey()
cv2.destroyAllWindows()
