import cv2
import matplotlib.pyplot as plt
#BLENDING AND PASTING IMAGES

import cv2

img1=cv2.imread('dog_backpack.png') 
#CONVERT BGR TO RGB
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img1)

img2=cv2.imread('watermark_no_copy.png') 
#CONVERT BGR TO RGB
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.imshow(img2)

#RESIZE IMAGE TO EQUAL SIZE 1200x1200

#BLENDING IMAGES OF THE SAME SIZE

img1=cv2.resize(img1,(1200,1200))
img1.shape

img2=cv2.resize(img2,(1200,1200))
img2.shape

#BLENDING IMAGES
blended=cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.1,gamma=10)
plt.imshow(blended)


#OVERLAY SMALL IMAGE ON TOP OF A LARGER IMAGE(NO BLENDING)
#Numpy reassignment operation

import cv2

img1=cv2.imread('dog_backpack.png') 
#CONVERT BGR TO RGB
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img1)

img2=cv2.imread('watermark_no_copy.png') 
#CONVERT BGR TO RGB
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.imshow(img2)

img2=cv2.resize(img2,(600,600))
plt.imshow(img2)

large_img=img1
small_img=img2

x_offset=0
y_offset=0

x_end=x_offset+small_img.shape[1]
y_end=y_offset+small_img.shape[0]

large_img[y_offset:y_end,x_offset:x_end]=small_img
plt.imshow(large_img)


#BLEND TOGETHER IMAGES OF DIFFERENT SIZES
import cv2

img1=cv2.imread('dog_backpack.png') 
#CONVERT BGR TO RGB
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
plt.imshow(img1)

img2=cv2.imread('watermark_no_copy.png') 
#CONVERT BGR TO RGB
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.imshow(img2)

img2=cv2.resize(img2,(600,600))
plt.imshow(img2)

img1.shape

x_offset=934-600
y_offset=1401-600


img2.shape

rows,cols,channels=img2.shape

roi=img1[y_offset:1401,x_offset:934]
plt.imshow(roi)


#Building MASK

img2gray=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
plt.imshow(img2gray,cmap='gray')

#INVERSION OF THE INPUT-black=white,white=black

mask_inv=cv2.bitwise_not(img2gray)
plt.imshow(mask_inv,cmap='gray')

mask_inv.shape

#To add color channels create white backgrounds

import numpy as np
white_background=np.full(img2.shape,255,dtype=np.uint8)

plt.imshow(white_background)

white_background.shape

mask_inv.shape

#white background
bk=cv2.bitwise_or(white_background,white_background,mask=mask_inv)
plt.imshow(bk)

fg=cv2.bitwise_or(img2,img2,mask=mask_inv)
plt.imshow(fg)

final_roi=cv2.bitwise_or(roi,fg)
plt.imshow(final_roi)

large_img=img1
small_img=final_roi
large_img[y_offset:y_offset+small_img.shape[0],x_offset:x_offset+small_img.shape[1]]=small_img
plt.imshow(large_img)

