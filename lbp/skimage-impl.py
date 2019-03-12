import cv2
import numpy as np
from skimage import feature

img = cv2.imread('../teddy.jpg', 0)
lbp = feature.local_binary_pattern(img, 8, 1)

a, b = 196, 201

print(img[a:b, a:b])
print(lbp[a:b, a:b])

cv2.imshow('Citra', img)
cv2.imshow('LBP', lbp.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()
