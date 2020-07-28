#WRITING TEXT IN IMAGE-2
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,text='Hello',org=(10,500),fontFace=font,fontScale=7,
            color=(255,255,255),thickness=3,lineType=cv2.LINE_AA)#font face--how large the text
plt.imshow(blank_img) 


#Draw your own custom polygon
#step 1 Reshape the vertices
#step 2 Draw the polygon

blank_img=np.zeros(shape=(512,512,3),dtype=np.int32)
plt.imshow(blank_img)
#vertices of polygon
vertices=np.array([[100,300],[200,200],[400,300],[200,400]],dtype=np.int32)
#Reshape it in 3 Dimensional openCV wants in 3 dimensional
vertices.shape
pts=vertices.reshape((-1,1,2))
pts.shape

cv2.polylines(blank_img,[pts],isClosed=True,color=(255,0,0),thickness=5)
plt.imshow(blank_img)