import numpy as np
import cv2
import os

# 顺时针旋转90度


def RotateClockWise90(input_img):
    trans_img = cv2.transpose(input_img)
    new_img = cv2.flip(trans_img, 1)
    return new_img


# 逆时针旋转90度
def RotateAntiClockWise90(input_img):
    trans_img = cv2.transpose(input_img)
    new_img = cv2.flip(trans_img, 0)
    return new_img


files = os.listdir('output')

for file in files:
    n = int(file.split('.')[0])

    img = cv2.imread("output/" + file, 1)
    # cv2.imshow("temp", img)
    # cv2.waitKey(0)
    # img90 = np.rot90(img)

    # 顺时针旋转
    # img_new = RotateClockWise90(img)
    # 逆时针旋转
    img_new = RotateAntiClockWise90(img)

    # cv2.imshow("rotate", img90)
    # cv2.waitKey(0)

    cv2.imwrite('reversal/lrot%d.png' % n, img_new)
