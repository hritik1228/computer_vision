import cv2
import matplotlib.pyplot as plt
img=cv2.imread('00-puppy.jpg')
plt.imshow(img)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)

#CONVERT TO HSV OR HLS

img=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
plt.imshow(img)

img=cv2.cvtColor(img,cv2.COLOR_RGB2HLS)
plt.imshow(img)
