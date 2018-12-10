import cv2
import numpy as np
import numpy.random as npr
from PIL import Image, ImageDraw, ImageFont


if __name__ == '__main__':
    font_size = 20
    # the output coordinates in the image
    output_coordinate = [0, 0]
    rgb = (0, 0, 0)

    # font_files = os.listdir('font_set')
    # font_rand_inx = npr.randint(len(font_files))
    # for font_file in os.listdir('font_set'):
    #     font = ImageFont.truetype("font_set//" + font_file, font_size,
    #                               encoding="utf-8")
    font = ImageFont.truetype("font_set//arial.ttf", font_size,
                              encoding="utf-8")
    cv2img = cv2.imread('pos_img//1.jpg')  # NO 0 here. 300 * 300
    # 将uint8转成int8型
    # 此句也可换成 p8 = np.array(pic, dtype=np.int8) 效果一样
    p8 = np.int8(cv2img)
    # for num in range(10):
    pilimg = Image.fromarray(cv2img)
    # put digits on PIL image
    draw = ImageDraw.Draw(pilimg)

    result_list = []
    count = 1
    for i in range(425):
        # random digit in range(10)
        num = npr.randint(10)

        # h is 15     w is 11
        draw.text(output_coordinate, str(num), rgb, font=font)

        # result_list: [top-left, h, w]
        result_list.append(output_coordinate[0])
        result_list.append(output_coordinate[1] + 4)
        result_list.append(output_coordinate[0] + 11)
        result_list.append(output_coordinate[1] + 4 + 15)

        if count % 5 == 0:
            output_coordinate[0] += 6

        output_coordinate[0] += 11
        if output_coordinate[0] + 11 > 300:
            output_coordinate[0] = 0
            output_coordinate[1] += 17
        count += 1
        #  convert PIL image to numpy
        cv2charimg = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)

        # get_boundingbox(cv2charimg, img_name_pos)
        cv2.imwrite("pos_img//11.jpg", cv2charimg)

    print(result_list)
    print(len(result_list))

    # create txt and write
    txtfile = open('pos_img\\pos.txt', 'w')
    txtfile.write('pos_img/11.jpg ')
    for d in result_list:
        txtfile.write(str(d)+' ')
    txtfile.close()