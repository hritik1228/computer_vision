import numpy as np
import matplotlib.pyplot as plt
import cv2
#If we provide wrong file location it doesn't give any error we need to check by using type() it returns NoneType
img=cv2.imread('00-puppy.jpg')
type(img)

img.shape
plt.imshow(img)

#Matplotlib-->it reads the image in this order-->>>>RGB, RED GREEN BLUE
#OpenCV--> it reads the image in this order--->>>>BLUE GREEN RED

#Transform to RGB
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)

 
#Convert/Read to gray scale image
img_gray=cv2.imread('00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
#no third dimension no three channels
img_gray.shape
img_gray.min() 
img_gray.max()

#default color mapping of imshow()--->darker value it shows as blue,lighter values it shows as yellowish green
plt.imshow(img_gray)
#Display image using matplotlib you have to specify the cmap as gray
plt.imshow(img_gray,cmap='gray')
plt.imshow(img_gray,cmap='magma')


#Resizing,flipping and saving image files

plt.imshow(fix_img)
fix_img.shape

#Resize
new_img=cv2.resize(fix_img,(1000,400))
plt.imshow(new_img)

#Resize by ratio
w_ratio=0.5#50% of original width
h_ratio=0.2#20% of original height
new_img=cv2.resize(fix_img,(0,0),fix_img,w_ratio,h_ratio)
plt.imshow(new_img)

new_img.shape

#Flip-Horizontal or vertical 0,1,-1
new_img=cv2.flip(fix_img,-1)
plt.imshow(new_img)

#Save Image

type(fix_img)
cv2.imwrite('totally_new.jpg',fix_img)


#To enlarge or make small the image size
fig=plt.figure(figsize=(2,2))
ax=fig.add_subplot(111)
ax.imshow(fix_img)





























