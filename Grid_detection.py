#Grid detection
import cv2
import numpy as np
import matplotlib.pyplot as plt

#importing the image
flat_chess=cv2.imread('flat_chessboard.png')
plt.imshow(flat_chess)

#find chess board corners-found variable is used to check whether the image is clear to draw or not
found,corners=cv2.findChessboardCorners(flat_chess,(7,7))

#to draw corners
cv2.drawChessboardCorners(flat_chess,(7,7),corners,found)
plt.imshow(flat_chess)


#circle based image-grid detection

#importing the image
dots=cv2.imread('dot_grid.png')
plt.imshow(dots)

#find chess board corners-found variable is used to check whether the image is clear to draw or not
found,corners=cv2.findCirclesGrid(dots,(10,10),cv2.CALIB_CB_SYMMETRIC_GRID)

#to draw corners
cv2.drawChessboardCorners(dots,(10,10),corners,found)
plt.imshow(dots)
