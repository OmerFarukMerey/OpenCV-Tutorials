import cv2

# open an image
# -1 --> cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will neglected. It is the default flag!
# 0 --> cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1 --> cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img = cv2.imread('photo.jpg', 1) 

# now let's resize our image
img = cv2.resize(img, (800,800))

# if you want to resize like half or quarter of the height or the width.
# fx=num1 for num1 times height and fy=num2 for num2 x width (nums are floating point numbers)
img = cv2.resize(img, (0,0), fx=0.75, fy=0.5)

# let's rotate our image
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# let's write to our image. The second argument will be written to the first argument.
cv2.imwrite('new_photo.jpg', img)

# display an image, frist argument is window name and second is the image itself.
cv2.imshow('Image', img)
cv2.waitKey(0) # parameter amount of wait (miliseconds) and 0 stands for infinty. 
cv2.destroyAllWindows()




