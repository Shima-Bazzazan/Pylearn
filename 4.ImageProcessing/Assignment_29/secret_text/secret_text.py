import cv2

image_text1= cv2.imread ("input/text1.png")
image_text2= cv2.imread ("input/text2.png")

secret_text= image_text2 - image_text1
secret_text= 255 - secret_text

cv2.imwrite ("output/secret_text.jpg", secret_text)