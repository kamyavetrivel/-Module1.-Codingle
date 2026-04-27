import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered = image.copy()

    if filter_type == "red_tint":
        filtered[:,:,1] = 0
        filtered[:,:,0] = 0

    elif filter_type == "blue_tint":
        filtered[:,:,1] = 0
        filtered[:,:,2] = 0

    elif filter_type == "green_tint":
        filtered[:,:,0] = 0
        filtered[:,:,2] = 0

    elif filter_type == "increase_red":
        filtered[:,:,2] = cv2.add(filtered[:,:,2],50)

    elif filter_type == "decrease_blue":
        filtered[:,:,0] = cv2.subtract(filtered[:,:,0],50)

    elif filter_type == "gaussian":
        filtered = cv2.GaussianBlur(image,(5,5),0)

    elif filter_type == "median":
        filtered = cv2.medianBlur(image,5)

    elif filter_type == "canny":
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        filtered = cv2.Canny(gray,100,200)

    return filtered


image = cv2.imread("Example3.png")

if image is None:
    print("Error image not found")
    exit()

filter_type = "original"

print("R - red tint")
print("B - blue tint")
print("G - green tint")
print("I - increase red")
print("D - decrease blue")
print("1 - gaussian")
print("2 - median")
print("3 - canny")
print("Q - quit")

while True:
    if filter_type == "original":
        output = image
    else:
        output = apply_filter(image, filter_type)

    cv2.imshow("Image", output)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('r'):
        filter_type = "red_tint"
    elif key == ord('b'):
        filter_type = "blue_tint"
    elif key == ord('g'):
        filter_type = "green_tint"
    elif key == ord('i'):
        filter_type = "increase_red"
    elif key == ord('d'):
        filter_type = "decrease_blue"
    elif key == ord('1'):
        filter_type = "gaussian"
    elif key == ord('2'):
        filter_type = "median"
    elif key == ord('3'):
        filter_type = "canny"
    elif key == ord('q'):
        break
    else:
        print("Invalid key")

cv2.destroyAllWindows()
