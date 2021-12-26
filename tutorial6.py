import cv2
import numpy as np

# Corner Detection

img = cv2.imread('Chess_Board.png')
img = cv2.resize(img, (0,0), fx=0.50, fy=0.50)

# In corner detection algorithms you should use gray scaled image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# corner detection algorithm
# arguments: image, n of the best corners, minimum quality of a corner, minimum euclidean distance of corners
# slowly increase the quality if it detects some things that are not corners
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# print(corners) corners will be floating point numbers

# The code below will take corners floating point numbers and turn them into integers 
corners = np.int0(corners)

for corner in corners:
	x, y = corner.ravel() # flatten the array [[[1, 2, 3]]] ---> [1,2,3]
	cv2.circle(img, (x,y), 5, (255, 0, 0), -1) # drawing blue filled circles to our corners 

# Notice that we used a gray scale of our image to detect the corners and drway circles to that corners in the original colored image


# Now we will draw line between these corners
for i in range(len(corners)):
	for j in range(i+1, len(corners)):
		corner1 = tuple(corners[i][0])
		corner2 = tuple(corners[j][0])
		color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
		cv2.line(img, corner1, corner2, (color), 1) # draws lines between corners with random colors

cv2.imshow('Chess Board',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
