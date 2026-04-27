import cv2
import numpy as np

def apply_filter(image, r, g, b):
    img = image.copy()
    img[:,:,2] = cv2.add(img[:,:,2], r)
    img[:,:,1] = cv2.add(img[:,:,1], g)
    img[:,:,0] = cv2.add(img[:,:,0], b)
    return img

image = cv2.imread("Example3.png")

if image is None:
    print("Error image not found")
    exit()

r = 0
g = 0
b = 0

print("R increase red")
print("T decrease red")
print("G increase green")
print("H decrease green")
print("B increase blue")
print("N decrease blue")
print("S save image")
print("Q quit")

while True:
    output = apply_filter(image, r, g, b)
    cv2.imshow("Image", output)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('r'):
        r += 20
    elif key == ord('t'):
        r -= 20
    elif key == ord('g'):
        g += 20
    elif key == ord('h'):
        g -= 20
    elif key == ord('b'):
        b += 20
    elif key == ord('n'):
        b -= 20
    elif key == ord('s'):
        cv2.imwrite("saved_image.png", output)
        print("Image saved")
    elif key == ord('q'):
        break
    else:
        print("Invalid key")

cv2.destroyAllWindows()
