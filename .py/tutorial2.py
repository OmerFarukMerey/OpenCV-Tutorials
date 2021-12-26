import cv2
import random

img = cv2.imread('photo.jpg', -1)

# printing the shape of the image (height, width, channels) channels are the color space of our image for example red green blue.
print(img.shape)
# in OpenCV we have [blue, green, red] for example [12, 231, 156] the values vary from 0 to 255

# printing the third row of our picture
print(img[3])
# printing the first row's from 45 to 400
print(img[3][40:400])


# putting random values to the first 100 rows of our picture and show it.
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# now let's copy a part of the image and paste it to somewhere else.
# the below code will copy 600 to 899th rows in 500 to 699th coulumn 
tag = img[500:700, 600:900]
# needs to the same shape to finish with success
img[100:300,650:950] = tag

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
