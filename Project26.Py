import cv2
import mediapipe as mp
import numpy as np
import screen_brightness_control as sbc
import os

# MediaPipe Hands Setup
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

# Landmark IDs
THUMB_TIP = mp_hands.HandLandmark.THUMB_TIP
INDEX_TIP = mp_hands.HandLandmark.INDEX_FINGER_TIP


# Function to control volume
def set_volume(volume):
    volume = int(volume)

    # macOS volume control
    os.system(f"osascript -e 'set volume output volume {volume}'")


# Open webcam
cap = cv2.VideoCapture(0)

while True:

    success, img = cap.read()

    if not success:
        print("Failed to capture image")
        break

    # Flip image
    img = cv2.flip(img, 1)

    h, w = img.shape[:2]

    # Convert to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process hands
    result = hands.process(rgb)

    if result.multi_hand_landmarks and result.multi_handedness:

        for i, hand_landmarks in enumerate(result.multi_hand_landmarks):

            # Left or Right hand
            label = result.multi_handedness[i].classification[0].label

            # Draw landmarks
            draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Get landmark positions
            lm = hand_landmarks.landmark

            thumb = (
                int(lm[THUMB_TIP].x * w),
                int(lm[THUMB_TIP].y * h)
            )

            index = (
                int(lm[INDEX_TIP].x * w),
                int(lm[INDEX_TIP].y * h)
            )

            # Draw circles
            cv2.circle(img, thumb, 10, (255, 0, 0), -1)
            cv2.circle(img, index, 10, (0, 255, 0), -1)

            # Draw line between fingers
            cv2.line(img, thumb, index, (0, 0, 255), 3)

            # Distance between fingers
            distance = np.hypot(
                index[0] - thumb[0],
                index[1] - thumb[1]
            )

            # Convert distance to value
            value = np.interp(distance, [30, 300], [0, 100])

            # LEFT HAND = VOLUME
            if label == "Left":

                set_volume(value)

                cv2.putText(
                    img,
                    f"Volume: {int(value)}%",
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )

            # RIGHT HAND = BRIGHTNESS
            else:

                sbc.set_brightness(int(value))

                cv2.putText(
                    img,
                    f"Brightness: {int(value)}%",
                    (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 255, 255),
                    2
                )

    # Show output
    cv2.imshow("Gesture Control", img)

    # Exit key
    if cv2.waitKey(1) & 0xFF in [27, ord('q')]:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()