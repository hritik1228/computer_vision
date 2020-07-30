#Image Thresholding

import cv2
import matplotlib.pyplot as plt
#Read in gray scale image
img=cv2.imread('rainbow.jpg',0)
plt.imshow(img,cmap='gray')
#any value below 127 shifted to 0
#any value above 127 shifted to 255
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret
plt.imshow(thresh1,cmap='gray')

#to inverve the output
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret
plt.imshow(thresh1,cmap='gray')

#TO TRUNC
ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret
plt.imshow(thresh1,cmap='gray')



img=cv2.imread('crossword.jpg',0)
plt.imshow(img,cmap='gray')

def show_pic(img):
    fig=plt.figure(figsize=(15,15))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    
show_pic(img)

ret,th1=cv2.threshold(img,180,255,cv2.THRESH_BINARY)
show_pic(th1)


#Adaptive Threshold
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
show_pic(th2)













