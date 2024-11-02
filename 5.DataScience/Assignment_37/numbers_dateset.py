import os
import cv2

img = cv2.imread("input/number.png")
rows, cols, _ = img.shape

num=0
count=0

os.makedirs("output", exist_ok=True)

for row in range(0, rows, 20):
    for col in range(0, cols, 20):
        crop_img = img[row:row+20, col:col+20]
        
        os.makedirs(f"output/{num}", exist_ok=True)
        cv2.imwrite(f"output/{num}/{count}.jpg", crop_img)
        count += 1
        
        if count%500 == 0:
            num += 1