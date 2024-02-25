
import cv2 
import numpy as np 


chess_board = np.zeros((560, 560))
for i in range(8):
    for j in range(8):
        if j % 2 == 0 and i%2==0:
            chess_board [70*i:70*(i+1) , 70*j:70*(j+1)] = 255
        elif i % 2!=0 and j %2!=0:
            chess_board [70*i:70*(i+1) , 70*j:70*(j+1)] = 255


cv2.imshow('Chess Board', chess_board)
cv2.waitKey()