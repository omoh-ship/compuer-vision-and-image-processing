import matplotlib.pyplot as plt
import cv2
import numpy as np


def plot_image(image_1, image_2,title_1="Orignal", title_2="New Image"):
    plt.figure(figsize=(10,10))
    plt.subplot(1, 2, 1)
    plt.imshow(image_1,cmap="gray")
    plt.title(title_1)
    plt.subplot(1, 2, 2)
    plt.imshow(image_2,cmap="gray")
    plt.title(title_2)
    plt.show()


def plot_hist(old_image, new_image,title_old="Orignal", title_new="New Image"):
    intensity_values=np.array([x for x in range(256)])
    plt.subplot(1, 2, 1)
    plt.bar(intensity_values, cv2.calcHist([old_image],[0],None,[256],[0,256])[:,0],width = 5)
    #cv2.calcHist(CV array:[image] this is the image channel:[0],for this course it will always be [None],the number of bins:[L],the range of index of bins:[0,L-1])
    plt.title(title_old)
    plt.xlabel('intensity')
    plt.subplot(1, 2, 2)
    plt.bar(intensity_values, cv2.calcHist([new_image],[0],None,[256],[0,256])[:,0],width = 5)
    plt.title(title_new)
    plt.xlabel('intensity')
    plt.show()


toy_image = np.array([[0,2,2],[1,1,1],[1,1,2]],dtype=np.uint8)
plt.imshow(toy_image, cmap="gray")
plt.show()
print("toy_image:",toy_image)

plt.bar([x for x in range(6)],[1,5,2,0,0,0])
plt.show()

plt.bar([x for x in range(6)],[0,1,0,5,0,2])
plt.show()

##GRAYSCALE HISTOGRAMS

goldhill = cv2.imread("goldhill.bmp",cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10,10))
plt.imshow(goldhill,cmap="gray")
plt.show()

hist = cv2.calcHist([goldhill],[0], None, [256], [0,256])

intensity_values = np.array([x for x in range(hist.shape[0])])
print(hist.shape[0])
plt.bar(intensity_values, hist[:,0], width = 5)
plt.title("Bar histogram")
plt.show()

PMF = hist / (goldhill.shape[0] * goldhill.shape[1])

plt.plot(intensity_values,hist)
plt.title("histogram")
plt.show()

# We can also apply a histogram to each image color channel
baboon = cv2.imread("baboon.png")
plt.imshow(cv2.cvtColor(baboon, cv2.COLOR_BGR2RGB))
plt.show()

color = ('blue', 'green', 'red')
for i, col in enumerate(color):
    histr = cv2.calcHist([baboon], [i], None, [256], [0, 256])
    plt.plot(intensity_values, histr, color=col, label=col + " channel")

    plt.xlim([0, 256])
plt.legend()
plt.title("Histogram Channels")
plt.show()