import cv2
import numpy as np
import matplotlib.pyplot as plt

flat_chess=cv2.imread('flat_chessboard.png')
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)

#convert to gray scale image
gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_flat_chess,cmap='gray')

#Importing real chess image
real_chess=cv2.imread('real_chessboard.jpg')
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)

#convert the real chess to gray
gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)
plt.imshow(gray_real_chess,cmap='gray')


#Converting in float as it accepts float value not an integer
gray=np.float32(gray_flat_chess)
 
#Applying Harris Corner Detection
dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst=cv2.dilate(dst,None)

flat_chess[dst>0.01*dst.max()]=[255,0,0]
plt.imshow(flat_chess)


#Converting in float as it accepts float value not an integer
gray=np.float32(gray_real_chess)

#Applying Harris Corner Detection
dst=cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst=cv2.dilate(dst,None)

real_chess[dst>0.01*dst.max()]=[255,0,0]
plt.imshow(real_chess)






















#Shi-Thomasi Detection

real_chess=cv2.imread('real_chessboard.jpg')
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
plt.imshow(real_chess)

flat_chess=cv2.imread('flat_chessboard.png')
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
plt.imshow(flat_chess)

gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)
gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

#Apply detection on image 1
corners=cv2.goodFeaturesToTrack(gray_flat_chess,64,0.01,10)
corners=np.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv2.circle(flat_chess,(x,y),3,(255,0,0),-1)
plt.imshow(flat_chess)

#Apply detection on image 2
corners=cv2.goodFeaturesToTrack(gray_real_chess,100,0.01,10)
corners=np.int0(corners)
for i in corners:
    x,y=i.ravel()
    cv2.circle(real_chess,(x,y),3,(255,0,0),-1)
plt.imshow(real_chess)
