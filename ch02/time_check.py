import sys
import time
import cv2

img = cv2.imread('.\\ch02\\hongkong.jpg')

if img is None:
    print("Image load failed!")
    sys.exit()

tm = cv2.TickMeter()

tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop()
t2 = time.time()
print('time:', (t2 - t1) * 1000)
print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))

