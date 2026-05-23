import cv2
import numpy as np

# Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Initial circle position
circle_x = 300
circle_y = 300

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Flip frame for mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Skin color range
    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create mask
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Remove noise
    kernel = np.ones((3, 3), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.GaussianBlur(mask, (5, 5), 0)

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if contours:

        # Largest contour
        max_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(max_contour) > 500:

            # Bounding rectangle
            x, y, w, h = cv2.boundingRect(max_contour)

            # Draw rectangle around hand
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Center point
            center_x = int(x + w / 2)
            center_y = int(y + h / 2)

            # Draw center point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Move circle with hand
            circle_x = center_x
            circle_y = center_y

    # Draw controllable circle
    cv2.circle(
        frame,
        (circle_x, circle_y),
        30,
        (255, 0, 0),
        -1
    )

    # Show windows
    cv2.imshow("Gesture Control", frame)
    cv2.imshow("Mask", mask)

    # Quit key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()