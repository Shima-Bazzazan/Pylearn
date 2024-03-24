import cv2 
import numpy as np 
import imageio


image = cv2.imread("old_tv.jpg")
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

rows, cols=image.shape

frames = []
while True:
    noise = np.random.random((164 , 216)) * 255 
    noise = np.array(noise , dtype=np.uint8)
    image[179:343 , 317:533] = noise

    new_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    frames.append(new_image)

    cv2.imshow("tv_noise" , new_image)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

imageio.mimsave ("tv_noise.gif", frames)
