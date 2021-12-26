import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))

	# We have 3 types of Acronym Breakdown:
	# RGB: Red Green Blue
	# BGR: Blue Green Red
	# HSV: Hue Saturation and Lightness/Brightness

	# HSV Color
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# now we have to extract the colors or pixels we want to extract.
	lower_blue = np.array([90, 50, 50]) # light blue 
	upper_blue = np.array([130, 255, 255]) # dark blue

	# mask is a portion of an image
	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	# so all of the pixels we had in our range of blue will stay as they were before but all the other pixels will blacked out.
	# source one and two (frame and frame)
	result = cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', result)
	cv2.imshow('mask', mask) # to show the mask
	cv2.imshow('HSV', hsv) # to show the hsv

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		