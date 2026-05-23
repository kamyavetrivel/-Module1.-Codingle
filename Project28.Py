import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands

hands = mp_hands.Hands()

draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

current_filter = "Normal"

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    h, w = img.shape[:2]

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        hand = results.multi_hand_landmarks[0]

        draw.draw_landmarks(
            img,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        lm = hand.landmark

        thumb_x = int(lm[4].x * w)
        index_x = int(lm[8].x * w)
        middle_x = int(lm[12].x * w)

        if abs(thumb_x - index_x) < 30:

            filename = f"photo_{int(time.time())}.jpg"

            cv2.imwrite(filename, img)

            cv2.putText(
                img,
                "Photo Saved",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        if abs(thumb_x - middle_x) < 30:

            if current_filter == "Normal":
                current_filter = "Gray"

            elif current_filter == "Gray":
                current_filter = "Blur"

            else:
                current_filter = "Normal"

        if current_filter == "Gray":

            img = cv2.cvtColor(
                img,
                cv2.COLOR_BGR2GRAY
            )

        elif current_filter == "Blur":

            img = cv2.GaussianBlur(
                img,
                (15, 15),
                0
            )

    cv2.imshow("Gesture Photo App", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()