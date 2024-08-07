
import cv2  
import keyboard 


def chess_face(frame) :
    faces = face_detector.detectMultiScale(frame)
    for face in faces :
        x , y , w , h  = face
        face_image = frame[y:y+h , x:x+w ]
        face_image_small = cv2.resize(face_image , [10,10])
        face_image_big = cv2.resize(face_image_small , [w,h] , interpolation=cv2.INTER_NEAREST)
        frame[y:y+h , x:x+w ] = face_image_big
    return frame


def sticker(frame):
    faces = face_detector.detectMultiScale(frame)
    for face in faces :
        x , y , w , h  = face
        min_y_sticker = int(y-20)
        max_y_sticker = int(h+y+20)
        sticker_height = max_y_sticker - min_y_sticker
        sticker_region = frame[min_y_sticker:max_y_sticker, x-10:x+w+900]

        sticker = cv2.resize(sticker_img, (w, sticker_height),interpolation=cv2.INTER_CUBIC)
        transparentOverlay(sticker_region,sticker)
    return frame 


def eye_lip_sticker(frame, _):
    global lip
    faces=face_cascade.detectMultiScale(frame, 1.2, 5, 0, (120, 120), (350, 350))
    for (x, y, w, h) in faces:
        if h > 0 and w > 0:
            min_y_glass = int(y + 1.5 * h / 8)
            max_y_glass = int(y + 7.5 * h / 12)
            glasses_height = max_y_glass - min_y_glass

            min_y_lip = int(y + 2 * h / 5 + 60)
            max_y_lip = int(y + 6 * h / 5 - 55)
            lip_height = max_y_lip - min_y_lip

            glasses_region = frame[min_y_glass:max_y_glass, x+10:x+w-10]
            lip_region = frame[min_y_lip:max_y_lip, x+75:x+w+75]

            glasses = cv2.resize(eyeglasses, (w-20, glasses_height),interpolation=cv2.INTER_CUBIC)
            lip= cv2.resize(lip, (w-140, lip_height),interpolation=cv2.INTER_CUBIC)
            transparentOverlay(glasses_region,glasses)
            transparentOverlay(lip_region,lip)
    return frame


def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  
    rows, cols, _ = src.shape  
    y, x = pos[0], pos[1]  
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src



def mirror_filter(frame):    
    for j in range(480):
        for i in range (320):
           frame[j, 639-i ] =frame[j, i] 
    return frame


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 30)

face_detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") 
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eyeglasses = cv2.imread("input\glasses.png", -1)
lip = cv2.imread("input\lip.png",-1)
sticker_img  = cv2.imread("input\tiger.png" , -1)

while True :   
    _ , frame = cap.read()

    if keyboard.is_pressed('1'):
        frame = sticker(frame)
    elif keyboard.is_pressed('2'):
        frame = eye_lip_sticker(frame , _)
    elif keyboard.is_pressed('3'):
        frame = chess_face(frame)
    elif keyboard.is_pressed('4'):
        frame = mirror_filter(frame)

    cv2.imshow("" , frame)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break