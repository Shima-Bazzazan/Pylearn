import cv2 
import numpy as np 
import imageio

array = []
image = cv2.imread("snow.jpeg")
image = cv2.resize(image, [680, 450])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
rows, cols = image.shape
for i in range(3000):
    speed = np.random.randint(1, 10)
    domain = np.random.randint(-4, 4)
    size = np.random.randint(1, 3)
    array.append([np.random.randint(0, cols), np.random.randint(0, rows), size, domain , speed])

frames = []
while True :
    image = cv2.imread("snow.jpeg")
    image = cv2.resize(image, [680, 450])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    for i in range(2000):
        image[array[i][0] : array[i][0]+array[i][2]  ,  array[i][1] : array[i][1]+array[i][2]  ] = 255
        array[i][0] +=  array[i][4]
        array[i][1] +=  array[i][3]
        if array[i][0] > cols:
            array[i][0] = 0
    frames.append(image)
    
    cv2.imshow("snowfall" , image)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

imageio.mimsave ("snowfall.gif", frames)
