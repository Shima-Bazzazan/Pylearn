import cv2
import numpy as np

character_image = np.ones((800, 800))

character_image[120:170, 500:550] = 0
character_image[70:120, 300:500] = 0
character_image[120:270, 250:300] = 0
character_image[270:320, 300:500] = 0
character_image[320:470, 500:550] = 0
character_image[470:520, 300:500] = 0
character_image[390:470, 250:300] = 0

cv2.imshow("character", character_image)
cv2.imwrite("charactor.jpg" ,character_image)
cv2.waitKey()