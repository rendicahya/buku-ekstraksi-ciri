import cv2

img = cv2.imread('../face.jpg', 0)
h, w = img.shape[:2]

for x in range(0, w, 40):
    cv2.line(img, (x, 0), (x, h), (0, 0, 0), 1)

for y in range(0, h, 40):
    cv2.line(img, (0, y), (w, y), (0, 0, 0), 1)

cv2.imshow('Image', img)
cv2.imwrite('../face-block.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()
