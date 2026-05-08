def main():

cap = cv2.VideoCapture(0)

if not cap.isOpened():

print("Cannot open camera")

return

ftype = "original"

print("Keys: r=RED, g=GREEN, b=BLUE, s=SOBEL, c=CANNY, t=CARTOON, q=QUIT")

while True:

ret, frame = cap.read()

if not ret:

print("Can't receive frame.")

break

out = apply_filter(frame, ftype)

cv2.imshow("Filter", out)

key = cv2.waitKey(1) & 0xFF

if key == ord('r'):

ftype = "red_tint"

elif key == ord('g'):

ftype = "green_tint"

elif key == ord('b'):

ftype = "blue_tint"

elif key == ord('s'):

ftype = "sobel"

elif key == ord('c'):

ftype = "canny"

elif key == ord('t'):

ftype = "cartoon"

elif key == ord('q'):

break

cap.release()

cv2.destroyAllWindows()

if __name__ == "__main__":

main()
