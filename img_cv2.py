import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread('00-puppy.jpg')
type(img)

img.shape
plt.imshow(img)

#Matplotlib-->RGB, RED GREEN BLUE
#OpenCV--> BLUE GREEN RED

#Transform to RGB
fix_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fix_img)


#Convert/Read to gray scale image
img_gray=cv2.imread('00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
#no third dimension no three channels
img_gray.shape
img_gray.min()
img_gray.max()
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
w_ratio=0.5
h_ratio=0.2#20%of original height
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


#DRWAING ON IMAGE-1

blank_img=np.zeros(shape=(512,512,3),dtype=np.int16)
blank_img.shape

plt.imshow(blank_img)
#draw rectangle on blank image-top left corner and bottom right corner 
cv2.rectangle(img=blank_img,pt1=(380,10),pt2=(500,150),color=(0,255,0),thickness=10)
plt.imshow(blank_img)

#Drwaing a square
cv2.rectangle(img=blank_img,pt1=(200,200),pt2=(300,300),color=(0,0,255),thickness=10)
plt.imshow(blank_img)

#Drawing a circle
cv2.circle(img=blank_img,center=(100,100),radius=50,color=(255,0,0),thickness=8)
plt.imshow(blank_img)

#Filled in circle 

#Drawing a filled circle
cv2.circle(img=blank_img,center=(400,400),radius=50,color=(255,0,0),thickness=-1)
plt.imshow(blank_img)
#Drawing a line
cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
plt.imshow(blank_img)


#WRITING TEXT IN IMAGE-2
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='Hello',org=(10,500),fontFace=font,fontScale=4,
            color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)
plt.imshow(blank_img)


#Draw your own custom polygon
blank_img=np.zeros(shape=(512,512,3),dtype=np.int32)
plt.imshow(blank_img)

vertices=np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)
#Reshape it in 3 Dimensional
vertices.shape
pts=vertices.reshape((-1,1,2))
pts.shape
cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
plt.imshow(blank_img)


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




















