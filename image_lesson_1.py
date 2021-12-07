from PIL import Image, ImageOps
import os
import matplotlib.pyplot as plt


def get_concat_h(img1, img2):
    """concatenate two images side-by-side"""
    dst = Image.new('RGB', (img1.width + img2.width, img2.height))
    dst.paste(img1, (0, 0))
    dst.paste(img2, (img1.width, 0))
    return dst


lenna = "lenna.png"

# get current path
cwd = os.getcwd()

# get image path since it is in same directory as current path
lenna_img_path = os.path.join(cwd, lenna)

lenna_image = Image.open('c:/Users/GLORIA ISEDU/Desktop/COURSERA COMPUTER VISION/lesson-1/lenna.png')
# lenna_image.show()

# OR for graph format
plt.figure(figsize=(10,10))
plt.imshow(lenna_image)
plt.show()

print(lenna_image.size)
print(lenna_image.mode)

# load the image into computer's memory
im = lenna_image.load()

# therefore, to check the intensity of the image RGB values at the  𝑥 -th column and  𝑦 -th row
x = 0
y = 1
print(im[x,y])

# You can save the image in `jpg` format using the following command.
lenna_image.save("lenna.jpg")
