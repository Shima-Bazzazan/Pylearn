import cv2
import numpy as np

image_miss_1= cv2.imread ("input/miss_1.png")
image_miss_2= cv2.imread ("input/miss_2.png")

image_miss_1= cv2.resize (image_miss_1, [395,395])
image_miss_2= cv2.resize (image_miss_2, [395,395])

image_miss_1= image_miss_1.astype (np.float32)
image_miss_2= image_miss_2.astype (np.float32)

temp1= image_miss_1 *3/4 + image_miss_2 *1/4
temp2= image_miss_1 *2/4 + image_miss_2 *2/4
temp3= image_miss_1 *1/4 + image_miss_2 *3/4

temp1= temp1.astype(np.uint8)
temp2= temp2.astype(np.uint8)
temp3= temp3.astype(np.uint8)

result= np.concatenate ((image_miss_1, temp1, temp2, temp3, image_miss_2),axis=1)

cv2.imwrite("output/miss.jpg", result)
