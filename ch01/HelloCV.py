import sys
import cv2

print('Hello OpenCV', cv2.__version__)

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load failed!")
    sys.exit()

cv2.imwrite('cat_gray.png', img)

cv2.nameWindow('image')
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()