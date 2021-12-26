import cv2
import numpy as np

# In this tutorial we will learn about Template Matching aka Object Detection
# we have a photo of a football (Soccer) match we will try to detect the ball from it.

# The algorithm we use in this tutorial uses gray-scale (reason it to be zero)
img = cv2.imread('football.jpg', 0)
template = cv2.imread('shoe.jpg', 0)
#template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)
# since it is a gray-scale it is a 2-dimensional array so only height and width
h, w = template.shape

# So here we have template matching methods you have to try with all the methods.
# The method that gives you the best result is the method you should use. (Advice from the documentation)
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
	# copy the image for all methods
	img2 = img.copy()

	# W: width of the original image
	# w: width of our template
	# H: height of the original image
	# h: height of our template
	# result will return us (W - w + 1, H - h + 1) array
	# Our matchTemplate will slide the template through the image
	# and it will give an output to show us where it matches the most
	result = cv2.matchTemplate(img2, template, method)

	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result);
	
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_loc
	else:
		location = max_loc

	bottom_right = (location[0] + w, location[1] + h)
	cv2.rectangle(img2, location, bottom_right, 255, 5)
	img2 = cv2.resize(img2, (0,0), fx=0.5, fy=0.5)
	cv2.imshow('match',img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

