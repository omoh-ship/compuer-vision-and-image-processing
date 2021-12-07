import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

##COPYING IMAGES
baboon = np.array(Image.open('baboon.png'))
plt.figure(figsize=(5,5))
plt.imshow(baboon )
plt.show()

A = baboon
id(A) == id(baboon)
B = baboon.copy()
id(B)==id(baboon)
baboon[:,:,] = 0

plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(baboon)
plt.title("baboon")
plt.subplot(122)
plt.imshow(A)
plt.title("array A")
plt.show()

plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(baboon)
plt.title("baboon")
plt.subplot(122)
plt.imshow(B)
plt.title("array B")
plt.show()

##FLIPPING IMAGES
image = Image.open("cat.png")
plt.figure(figsize=(10,10))
plt.imshow(image)
plt.show()

array = np.array(image)
width, height, C = array.shape
print('width, height, C', width, height, C)
array_flip = np.zeros((width, height, C), dtype=np.uint8)
for i,row in enumerate(array):
    array_flip[width - 1 - i, :, :] = row

OR

from PIL import ImageOps

im_flip = ImageOps.flip(image)
plt.figure(figsize=(5,5))
plt.imshow(im_flip)
plt.show()

#mirror
im_mirror = ImageOps.mirror(image)
plt.figure(figsize=(5,5))
plt.imshow(im_mirror)
plt.show()

#transpose
im_flip = image.transpose(1)
plt.imshow(im_flip)
plt.show()


#flip dict
flip = {"FLIP_LEFT_RIGHT": Image.FLIP_LEFT_RIGHT,
        "FLIP_TOP_BOTTOM": Image.FLIP_TOP_BOTTOM,
        "ROTATE_90": Image.ROTATE_90,
        "ROTATE_180": Image.ROTATE_180,
        "ROTATE_270": Image.ROTATE_270,
        "TRANSPOSE": Image.TRANSPOSE, 
        "TRANSVERSE": Image.TRANSVERSE}

flip["FLIP_LEFT_RIGHT"]

for key, values in flip.items():
    plt.figure(figsize=(10,10))
    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.title("orignal")
    plt.subplot(1,2,2)
    plt.imshow(image.transpose(values))
    plt.title(key)
    plt.show()

##CROPPING IMAGE

upper = 150
lower = 400
crop_top = array[upper: lower,:,:]
plt.figure(figsize=(5,5))
plt.imshow(crop_top)
plt.show()

left = 150
right = 400
crop_horizontal = crop_top[: ,left:right,:]
plt.figure(figsize=(5,5))
plt.imshow(crop_horizontal)
plt.show()

image = Image.open("cat.png")
crop_image = image.crop((left, upper, right, lower))
plt.figure(figsize=(5,5))
plt.imshow(crop_image)
plt.show()

crop_image = crop_image.transpose(Image.FLIP_LEFT_RIGHT)


##CHANGING SPECIFIC IMAGE PIXELS
array_sq = np.copy(array)
array_sq[upper:lower, left:right, 1:2] = 0

plt.figure(figsize=(5,5))
plt.subplot(1,2,1)
plt.imshow(array)
plt.title("orignal")
plt.subplot(1,2,2)
plt.imshow(array_sq)
plt.title("Altered Image")
plt.show()

from PIL import ImageDraw 

image_draw = image.copy()
image_fn = ImageDraw.Draw(im=image_draw)

shape = [left, upper, right, lower] 
image_fn.rectangle(xy=shape,fill="red")

plt.figure(figsize=(10,10))
plt.imshow(image_draw)
plt.show()

from PIL import ImageFont

image_fn.text(xy=(0,0),text="box",fill=(0,0,0))

plt.figure(figsize=(10,10))
plt.imshow(image_draw)
plt.show()

image_lenna = Image.open("lenna.png")
array_lenna = np.array(image_lenna)

array_lenna[upper:lower,left:right,:]=array[upper:lower,left:right,:]
plt.imshow(array_lenna)
plt.show()

image_lenna.paste(crop_image, box=(left,upper))

plt.imshow(image_lenna)
plt.show()

image = Image.open("cat.png")
new_image=image
copy_image=image.copy()

id(image)==id(new_image)

id(image)==id(copy_image)

image_fn= ImageDraw.Draw(im=image)
image_fn.text(xy=(0,0),text="box",fill=(0,0,0))
image_fn.rectangle(xy=shape,fill="red")

plt.figure(figsize=(10,10))
plt.subplot(121)
plt.imshow(new_image)
plt.subplot(122)
plt.imshow(copy_image)
plt.show()