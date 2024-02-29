import cv2

image = cv2.imread("1.jpg" )
inverted_image = image
x = image.shape[0] 
y = image.shape[1]

for row in range(x) :
    for column in range(y):
            inverted_image[row][column] = 255 - inverted_image[row][column]

cv2.imshow("inverted_image" ,inverted_image)
cv2.imwrite("inverted_image" , inverted_image)
cv2.waitKey()