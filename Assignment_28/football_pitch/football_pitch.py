import cv2 
import numpy as np 

football_pitch = np.ones((450 , 700 , 3) , dtype= np.uint8) * 255

y = 0 
for i in range(7):
    if i % 2 == 0 :
        cv2.rectangle(football_pitch, [0+y,0] , [100+y , 700] , (45 , 110 , 5) , -1 )
    else :
        cv2.rectangle(football_pitch, [0+y,0] , [100+y , 700] , (40 , 90 , 10) , -1 )
    y+= 100
cv2.rectangle(football_pitch, [20,20] , [680 ,430] , (255,255,255) , 2 )
cv2.line(football_pitch, [350,20] , [350 ,430] , (255,255,255) , 2 )
cv2.circle(football_pitch, [350,225] , 90 , (255,255,255) , 2 )
cv2.circle(football_pitch, [350,225] , 7 , (255,255,255) , -1 )
y = 0
y1 = 0

for i in range(2):
    cv2.rectangle(football_pitch, [20+y ,110] , [130+y ,340] , (255,255,255) , 2 )
    cv2.rectangle(football_pitch, [20+y1,160] , [80+y1 ,290] , (255,255,255) , 2 ) 
    y+= 550
    y1 = y+50

cv2.imshow("football pitch" , football_pitch)
cv2.waitKey()
cv2.imwrite("output\football_pitch.jpg" , football_pitch)