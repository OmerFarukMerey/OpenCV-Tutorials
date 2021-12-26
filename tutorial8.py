import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# In this tutorial we will use Face Detection using Haar Cascades

# Loading Classifiers
# We don't need to download or anything they come with the OpenCV installation
# cv2.data.haarcascades is the path in our system.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# now let's use them.

while True:
	ret, frame = cap.read()

	# Just like many algorithms in OpenCV we use gray-scale of our frame or image
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# returns all of the locations of faces in terms of coordinates
	# https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters 
	# The above link is a beautiful explanation of our parameters for the code line below.
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	# Now let's draw a blue rectangle to our faces
	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 5)

		# now let's give our face to eye detector so that it can tell us where our eyes are
		roi_gray = gray[y:y+w, x:x+w]
		roi_color = frame[y:y+h, x:x+w]

		# now let's look at our cgray-scale image for any of eyes
		eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)

		# now let's draw those eyes
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 5)

	
	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()		