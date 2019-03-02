import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage import feature

img1 = np.zeros((200, 200), np.uint8)
img1[100:] = 255
lbp1 = feature.local_binary_pattern(img1, 8, 1)

img2 = np.array([np.full(200, v) for v in range(200)], np.uint8)
lbp2 = feature.local_binary_pattern(img2, 8, 1)

img3 = cv2.imread('rope.jpg', 0)
lbp3 = feature.local_binary_pattern(img3, 8, 1)

stack = np.hstack((
    np.vstack((img1, lbp1.astype(np.uint8))),
    np.vstack((img2, lbp2.astype(np.uint8))),
    np.vstack((img3, lbp3.astype(np.uint8)))
))

stack[200] = 0
stack[:, 200] = 0
stack[:, 400] = 0

plt.hist(lbp3.astype(np.uint8).ravel(), 256, [0, 256])
plt.show()

cv2.imshow('LBP', stack)
# cv2.imwrite('demo-textures.jpg', stack)
cv2.waitKey(0)
cv2.destroyAllWindows()
