from PIL import Image, ImageOps
import matplotlib.pyplot as plt
from image_lesson_1 import get_concat_h

baboon_image = Image.open('c:/Users/GLORIA ISEDU/Desktop/COURSERA COMPUTER VISION/lesson-1/baboon.png')
red, green, blue = baboon_image.split()
get_concat_h(baboon_image, red)
get_concat_h(baboon_image, green)
get_concat_h(baboon_image, blue)