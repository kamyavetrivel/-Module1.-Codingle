import cv2
import mediapipe as mp
import pyautogui
import time


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7
)

draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(0)

last_scroll = 0

while True:

    success, img = cap.read()

    if not success:
        break


    img = cv2.flip(img, 1)

   
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    results = hands.process(rgb)

    gesture = "None"

    if results.multi_hand_landmarks:

        for hand in results.multi_hand_landmarks:

            
            draw.draw_landmarks(
                img,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand.landmark

            fingers = 0

            
            tip_ids = [8, 12, 16, 20]

            for tip in tip_ids:

                if landmarks[tip].y < landmarks[tip - 2].y:
                    fingers += 1

            
            if time.time() - last_scroll > 1:

                if fingers >= 4:

                    pyautogui.scroll(300)
                    gesture = "Scroll Up"

                
                elif fingers == 0:

                    pyautogui.scroll(-300)
                    gesture = "Scroll Down"

                last_scroll = time.time()

  
    cv2.putText(
        img,
        gesture,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    
    cv2.imshow("Gesture Scroll Control", img)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()