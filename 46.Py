import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc
import os

Hands = mp.solutions.hands
hands = Hands.Hands(
min_detection_confidence=0.7,
min_tracking_confidence=0.7)
draw = mp.solutions.drawing_utils
TH = Hands.HandLandmark.THUMB_TIP
IX= Hands.HandLandmark.INDEX_FINGER_TIP

def set_volume(v):
    os.system(f"OSACRIPT -e 'set volume output volume{int(v)}")
cap = cv2.VideoCapture(0) 
while True:
    ok,img = cap.read()
    if not ok:break
    img = cv2.flip(img,1)
    h,w =img.shape [:2]

    res = hands.process(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks and res.multi_handedness:
        for i,hand in enumerate(res.multi_hand_landmarks):
            label = res.multi_handedness[i].classification[0].label
            draw.draw_landmarks(img, hand, Hands. HAND_CONNECTIONS)
            lm= hand.landmark
            tp= (int(lm[TH].x*w), int (lm[TH].y*h))
            ip= (int(lm[IX].x*w), int (lm[IX].y*h))

            dist= np.hypot(ip[0]-tp[0],ip[1]-tp[1])
            val = np.interp(dist,[30,300],[0,100])
            if label == "Left":
                set_volume(val)
            else: sbc.set_brightness(int(val))

    cv2.imshow("Control", img)
    if cv2.waitKey(1)& 0xFF in [27, ord ("q")]:
        break

cap.release()
cv2.destroyAllWindows
                

             
                
                


