import cv2

cap = cv2.VideoCapture(1)
_ , frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

while True:
    _ , frame = cap.read()
    frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    mask = cv2.rectangle(frame , (220 , 120) , (430, 330)  , 255 ,3)
    for i in range(125 , 325):
        for j in range(225,425):
            if frame[i ,j] <= 60 :
                cv2.putText(frame , "Black " , (250 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            if frame[i ,j] > 70 and frame[i ,j] <= 130 :
                cv2.putText(frame , "Gray " , (50 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)
            if frame[i ,j] > 180 and frame[i ,j] <= 255 :
                cv2.putText(frame , "White " , (450 , 90) , cv2.FONT_HERSHEY_SIMPLEX , 1 , 6 , 3)

    
    cv2.imshow("camera" , frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break
