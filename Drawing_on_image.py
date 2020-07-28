#DRWAING ON IMAGE-1

#black image with all zeros
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
cv2.circle(img=blank_img,center=(100,100),radius=20,color=(255,0,0),thickness=8)
plt.imshow(blank_img)

#Filled in circle 

#Drawing a filled circle
cv2.circle(img=blank_img,center=(400,400),radius=50,color=(255,0,0),thickness=-1)
plt.imshow(blank_img)
#Drawing a line
cv2.line(blank_img,pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
plt.imshow(blank_img)
