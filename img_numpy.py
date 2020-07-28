import numpy as  np
import matplotlib.pyplot as plt
#Pyhton imgaging library
from PIL import Image
pic=Image.open('00-puppy.jpg')#open a image
#type of object
type(pic)

#transform into array
pic_arr=np.array(pic)
type(pic)

pic_arr=np.asarray(pic)
type(pic_arr)

#to check the shape of array
pic_arr.shape

#to show images that are transformed into array
plt.imshow(pic_arr)

#to copy the original image
pic_red=pic_arr.copy()
plt.imshow(pic_red)

#R G B

#RED Channel Values 0-no red,pure black-255 full pure red
plt.imshow(pic_red[:,:,0],cmap='gray')#closer,more red
#GREEN Channel Values
plt.imshow(pic_red[:,:,1],cmap='gray')
#BLUE Channel Values
plt.imshow(pic_red[:,:,2],cmap='gray')

#Green Channel
pic_red[:,:,1]=0
plt.imshow(pic_red)

#Blue Channel
pic_red[:,:,2]=0
plt.imshow(pic_red)

#Red Channel
pic_red[:,:,0]=0
plt.imshow(pic_red)

#it still have information of all the three channels but individually it gives the correct information all channels
pic_red.shape


