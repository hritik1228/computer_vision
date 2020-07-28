#Part-3 Draw rectangle by dragging the mouse

import numpy as np
import cv2
#VARIABLES
#True while mouse button down,False while mouse button up
drawing=False
ix=-1
iy=-1

#FUNCTIONS
def draw_rectangle(event,x,y,flags,prams):
    
    global ix,iy,drawing
    
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        
    
#SHOWING THE IMAGE
img=np.zeros((512,512,3),np.int8)
cv2.namedWindow(winname='my_drawing')
cv2.setMouseCallback('my_drawing',draw_rectangle)


while True:
    cv2.imshow('my_drawing',img)
    #if we have waited at least 20 ms AND we have pressed the ESC
    if cv2.waitKey(20) & 0xFF==27:
        break
    
cv2.destroyAllWindows()
