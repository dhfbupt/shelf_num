import cv2
import numpy as np

img = np.ones((300, 300), dtype=np.uint8)  # random.random()方法后面不能加数据类型

bgr_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
# cv2.imshow('bgr_img',bgr_img)
bgr_img[:, :, 0] = 255
bgr_img[:, :, 1] = 255
bgr_img[:, :, 2] = 255
# cv2.imshow('bgr_img2',bgr_img)
# cv2.waitKey(0)

cv2.imwrite('pos_img//1.jpg', bgr_img)
