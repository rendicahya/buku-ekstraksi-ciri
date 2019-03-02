import cv2
import numpy as np
from skimage import feature

img1 = cv2.imread('teddy.jpg', 0)
lbp1 = feature.local_binary_pattern(img1, 8, 1)

img2 = cv2.addWeighted(img1, .7, img1, 0, 0)
lbp2 = feature.local_binary_pattern(img2, 8, 1)

img3 = cv2.addWeighted(img1, 1.3, img1, 0, 0)
lbp3 = feature.local_binary_pattern(img3, 8, 1)

stack = np.hstack((
    np.vstack((img1, lbp1.astype(np.uint8))),
    np.vstack((img2, lbp2.astype(np.uint8))),
    np.vstack((img3, lbp3.astype(np.uint8)))
))

cv2.imshow('LBP', stack)
cv2.imwrite('teddy-demo.jpg', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
