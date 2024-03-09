import cv2 
import numpy as np 
import imageio


init_image = cv2.imread("tv_noise\picture\old_tv.jpg")
img = cv2.cvtColor(init_image , cv2.COLOR_BGR2GRAY)

rows, cols=img.shape

writer = cv2.VideoWriter("noise.mp4" , cv2.VideoWriter_fourcc(*'mp4v') , 30 , (rows , cols))

print(img.shape)
while True:
    noise1 = np.random.random(( 72, 99)) * 255 
    noise1 = np.array(noise1 , dtype=np.uint8)
    img[163:235 , 875:974] = noise1

    noise2 = np.random.random((100 , 135)) * 255 
    noise2 = np.array(noise2 , dtype=np.uint8)
    img[130:230 , 400:535] = noise2

    noise2 = np.random.random((134 , 162)) * 255 
    noise2 = np.array(noise2 , dtype=np.uint8)
    img[391:525 , 325:487] = noise2
    writer.write(img)

    cv2.imshow("tv_noise" , img)
    if cv2.waitKey(25) & 0xFF == ord("b"):
        break

writer.release()