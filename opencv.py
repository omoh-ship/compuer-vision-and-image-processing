from PIL import Image
import os
import cv2


def get_concat_h(img1, img2):
    dst = Image.new("RGB", (img1.width + img2.width, img1.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (img1.width, 0))
    return dst


lenna = "lenna.png"
cwd = os.getcwd()
lenna_img_path = os.path.join(f"{cwd}\lesson-1", lenna)
# print(lenna_img_path)

###########################################Load in Image in Python############################################################

lenna_image = cv2.imread(lenna_img_path)
