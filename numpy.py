from PIL import Image
# import matplotlib.pyplot as plt
# from image_lesson_1 import get_concat_h
import numpy 


lenna_image = Image.open('c:/Users/GLORIA ISEDU/Desktop/COURSERA COMPUTER VISION/lesson-1/lenna.png')
lenna_array = numpy.array(lenna_image)
print(type(lenna_array))
