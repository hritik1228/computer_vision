import cv2
import numpy as np
import matplotlib.pyplot as plt

full=cv2.imread('sammy.jpg')
full=cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
plt.imshow(full)


face=cv2.imread('sammy_face.jpg')
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
plt.imshow(face)

"""
#Using eval function
mystring='sum'
eval(mystring)
myfunc=eval(mystring)
myfunc([1,2,3])
"""

# All the 6 methods for comparison in a list
# Note how we are using strings, later on we'll use the eval() function to convert to function
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED',
           'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 
           'cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
for m in methods:
    
    # Create a copy of the image
    full_copy = full.copy()
    
    # Get the actual function instead of the string
    method = eval(m)

    # Apply template Matching with the method
    res = cv2.matchTemplate(full_copy,face,method)
    
    # Grab the Max and Min values, plus their locations
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # Set up drawing of Rectangle
    
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    # Notice the coloring on the last 2 left hand side images.
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc    
    else:
        top_left = max_loc
    
    height,width,channels=face.shape
        
    # Assign the Bottom Right of the rectangle
    bottom_right = (top_left[0] + width, top_left[1] + height)

    # Draw the Red Rectangle
    cv2.rectangle(full_copy,top_left, bottom_right, 255, 10)

    # Plot the Images
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Result of Template Matching')
    
    plt.subplot(122)
    plt.imshow(full_copy)
    plt.title('Detected Point')
    plt.suptitle(m)
    
    
    plt.show()
    print('\n')
    print('\n')
    
"""    
my_method=eval('cv2.TM_CCOEFF')
res=cv2.matchTemplate(full,face,my_method)
plt.imshow(res)
"""










