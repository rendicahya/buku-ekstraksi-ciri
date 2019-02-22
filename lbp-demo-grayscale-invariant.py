import cv2
import numpy as np
from skimage import feature

img = cv2.imread('teddy.jpg', 0)
img = cv2.addWeighted(img, .6, img, 0, 39)
lbp = feature.local_binary_pattern(img, 8, 1)

inc = 50

dark = np.where(img >= inc, img - inc, 0)
dark_lbp = feature.local_binary_pattern(dark, 8, 1)

bright = np.where(img <= 255 - inc, img + inc, 255)
bright_lbp = feature.local_binary_pattern(bright, 8, 1)

stack = np.hstack((
    np.vstack((img, lbp.astype(np.uint8))),
    np.vstack((dark, dark_lbp.astype(np.uint8))),
    np.vstack((bright, bright_lbp.astype(np.uint8)))
))

cv2.imshow('LBP', stack)
cv2.imwrite('teddy-demo.jpg', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
