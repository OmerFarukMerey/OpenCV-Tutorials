import cv2
import numpy as np

# loading a video capture device (webcam) and the argument num will be the numth webcam of your computer since we have only one we have to write 0 
cap = cv2.VideoCapture(0)

# now our device will capture untill we press a keyboard in our computer
while True:
	# in the below code frame is the image itself the numpy array itself and ret will be the returned value to tell if it was successfull or not
	ret, frame = cap.read()

	# getting the width and the height of our capture.
	width = int(cap.get(3)) # 3 is the identifier for width (Look at the documentary for more)
	height = int(cap.get(4)) # 4 is the identifier for height (Look at the documentary for more)


	# let's now make four of me (webcam) and display it.
	# Mirroring video multiple times
	image = np.zeros(frame.shape, np.uint8) # blank image with the frame we want and the second argument will be the type of the integer

	smaller_frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5) # We have halfen our frame so that we can use it 4 times make it fill the blank frame
	
	image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # top left (rotated) 
	image[height//2:, :width//2] = smaller_frame # bottom left
	image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) # top right
	image[height//2:, width//2:] = smaller_frame # bottom right (rotated)
	
	# you can change the second argument of the next line of code and see the empty black frame
	# now let's display the frame
	cv2.imshow('frame', image)

	# cv2.waitKey(1) will return the key you press and if it's q then break
	# alse ord(char) returns the ASCII of the char value
	if cv2.waitKey(1) == ord('q'):
		break

# release our capture device so it can be used by other program
cap.release()	
cv2.destroyAllWindows()	