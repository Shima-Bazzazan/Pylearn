import cv2

image = cv2.imread("3.jpg" )
sad_man_img = cv2.resize(image ,[1000 , 600])
happy_man_img= cv2.rotate(sad_man_img, cv2.ROTATE_180)

cv2.imshow("Happy_Men" ,happy_man_img)
cv2.imwrite("happy_man.jpg" , happy_man_img)
cv2.waitKey()