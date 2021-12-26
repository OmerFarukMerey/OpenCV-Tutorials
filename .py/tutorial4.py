import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	width = int(cap.get(3))
	height = int(cap.get(4))

	# Drawing lines
	# img : The image where you want to draw the shapes
	#color : Color of the shape. for BGR, pass it as a tuple, eg: (255,0,0) for blue. For grayscale, just pass the scalar value.
  	#thickness : Thickness of the line or circle etc. If -1 is passed for closed figures like circles, it will fill the shape. default thickness = 1
	#lineType : Type of line, whether 8-connected, anti-aliased line etc. By default, it is 8-connected. cv.LINE_AA gives anti-aliased line which looks great for curve
	img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)
	# you can either write frame or img to the first argument to the below code (works the same)
	img = cv2.line(frame, (0,height), (width,0), (0,255,0), 10)


	# Drawing Rectangles
	# To draw a rectangle, you need top-left corner and bottom-right corner of rectangle. This time we will draw a green rectangle at the top-right corner of image.
	# If you put -1 as the last argument for shapes it just covers all the shape 
	img = cv2.rectangle(frame, (100,100), (200,200), (128,128,128), 3)


	# Drawing Circle
	# To draw a circle, you need its center coordinates and radius. We will draw a circle inside the rectangle drawn above.
	img = cv2.circle(frame, (300,300), 50, (0,0,255), -1)


	# Drawing a text
	# First you need to have a font
	# To put texts in images, you need specify following things.
	# Text data that you want to write
	# Position coordinates of where you want put it (bottom-left corner where data starts).
	# Font type (Check cv.putText() docs for supported fonts)
	# Font Scale (specifies the size of font)
	# regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(img, 'Omer Faruk Merey', (20,height-10), font, 2, (255,255,255), 2, cv2.LINE_AA)

	# In this part you don't have to change frame to img (works the sameq)
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		
