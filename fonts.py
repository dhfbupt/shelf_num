import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os


def get_boundingbox(src_image, img_name):
    gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)
    left, right, top, bottom = 0, 0, 0, 0

    for iCol in range(gray_image.shape[1]):
        for iRow in range(gray_image.shape[0]):
            if gray_image[iRow, iCol] < 100:
                left = iCol
                break
        if left != 0:
            break
    for iCol in range(gray_image.shape[1] - 1, -1, -1):
        for iRow in range(gray_image.shape[0]):
            if gray_image[iRow, iCol] < 100:
                right = iCol + 1
                break
        if right != 0:
            break
    for iRow in range(gray_image.shape[0]):
        for iCol in range(gray_image.shape[1]):
            if gray_image[iRow, iCol] < 100:
                top = iRow
                break
        if top != 0:
            break
    for iRow in range(gray_image.shape[0] - 1, -1, -1):
        for iCol in range(gray_image.shape[1]):
            if gray_image[iRow, iCol] < 100:
                bottom = iRow + 1
                break
        if bottom != 0:
            break

    # cv2.rectangle(gray_image, (left, top), (right, bottom), 0)
    # print(top, '\t', bottom, '\t', left, '\t', right)

    # _, bin_image = cv2.threshold(gray_image, 0, 255,
    #                              cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
    # cv2.namedWindow('image', 0)
    # cv2.imshow('image', bin_image)
    # cv2.waitKey()
    cropped = gray_image[top:bottom, left:right]

    cv2.imwrite(img_name, cropped)


if __name__ == '__main__':
    font_size = 20
    # the output coordinates in the image
    output_coordinate = (5, 5)
    rgb = (0, 0, 0)

    for bg_file in os.listdir("pos_img"):
        output_img_name = 0
        for font_file in os.listdir('font_set'):
            font = ImageFont.truetype("font_set//" + font_file, font_size,
                                      encoding="utf-8")
            cv2img = cv2.imread('pos_img//' + bg_file)  # NO 0 here
            # 将uint8转成int8型
            # 此句也可换成 p8 = np.array(pic, dtype=np.int8) 效果一样
            p8 = np.int8(cv2img)
            for num in range(10):
                pilimg = Image.fromarray(cv2img)
                # put digits on PIL image
                draw = ImageDraw.Draw(pilimg)
                draw.text(output_coordinate, str(num), rgb, font=font)
                #  convert PIL image to numpy
                cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

                img_name_pos = 'pos_samples//' + bg_file.split('.')[
                    0] + '%d.png' % output_img_name

                get_boundingbox(cv2charimg, img_name_pos)
                # cv2.imwrite("output//%d.png" % output_img_name, cv2charimg)
                output_img_name += 1
