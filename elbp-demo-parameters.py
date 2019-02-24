import cv2
import numpy as np
from skimage import feature

img = cv2.imread('teddy.jpg', 0)
lbp1 = feature.local_binary_pattern(img, 8, 3)
lbp2 = feature.local_binary_pattern(img, 12, 3)
lbp3 = feature.local_binary_pattern(img, 24, 3)
stack = np.hstack((
    np.vstack((img, lbp1.astype(np.uint8))),
    np.vstack((img, lbp2.astype(np.uint8))),
    np.vstack((img, lbp2.astype(np.uint8)))
))

cv2.imshow('LBP', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
