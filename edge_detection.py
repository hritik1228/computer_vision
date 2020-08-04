#Edge Detection
import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('sammy_face.jpg')
plt.imshow(img)

#Applying edge detection(Method-1)-play around the threshold value

edges=cv2.Canny(image=img,threshold1=127,threshold2=127)
plt.imshow(edges)

#by applying foremula to know the threshold value
#Lower threshold to either 0 or 70% of the median value whichever is greater
med_val=np.median(img)
lower=int(max(0,0.7*med_val))
#upper threshold to either 130% of the median or the max 255,whichever is small
upper=int(min(255,1.3*med_val))
edges=cv2.Canny(image=img,threshold1=lower,threshold2=upper)
plt.imshow(edges)

#Applying edge detection(Method-2)blurring the image and applying edge detection
blurred_img=cv2.blur(img,ksize=(5,5))
edges=cv2.Canny(image=blurred_img,threshold1=lower,threshold2=upper+110)
plt.imshow(edges)



