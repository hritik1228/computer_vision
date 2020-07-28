"""
We can use CallBacks to connect images to
event functions with opencv
This allows us to directly interact with images 
(and later on videos)
Points to cover:-
1.Connecting CallBack Functions
2.Adding functionality through Event Choices
3.Dragging the mouse for functionality
"""
#Drawing with Mouse-1
import cv2
import numpy as np

################
##Function######
################
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

#################################
#####SHOWING IMAGE WITH OPENCV###
#################################

img=np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    #if we have waited at least 20 ms AND we have pressed the ESC
    if cv2.waitKey(20) & 0xFF==27:
        break
    
cv2.destroyAllWindows()


#Adding functionality with event choices-2
import cv2
import numpy as np

################
##Function######
################
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,255,0),-1)
    
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    
        
cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_circle)

#################################
#####SHOWING IMAGE WITH OPENCV###
#################################

img=np.zeros((512,512,3),np.int8)

while True:
    cv2.imshow('my_drawing',img)
    #if we have waited at least 20 ms AND we have pressed the ESC
    if cv2.waitKey(20) & 0xFF==27:
        break
    
cv2.destroyAllWindows()
