from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_lesson_1  import get_concat_h

lenna_image = Image.open('c:/Users/GLORIA ISEDU/Desktop/COURSERA COMPUTER VISION/lesson-1/lenna.png')

lenna_img_gray = ImageOps.grayscale(lenna_image)
# lenna_img_gray.show()
lenna_img_gray.quantize(256 // 2)
# lenna_img_gray.show()
# print(lenna_img_gray.mode)

#get_concat_h(image_gray,  image_gray.quantize(256//2)).show(title="Lena") 
for n in range(3,8):
    plt.figure(figsize=(10,10))

    plt.imshow(get_concat_h(lenna_img_gray,  lenna_img_gray.quantize(256//2**n))) 
    plt.title("256 Quantization Levels  left vs {}  Quantization Levels right".format(256//2**n))
    plt.show()
