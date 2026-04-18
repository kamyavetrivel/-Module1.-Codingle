import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("example3.png")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.title("RGB")
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap="gray")
plt.title("GRAY")
plt.show()

crop = image[100:300, 200:400]
plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
plt.title("CROP")
plt.show()

(h,w) = image.shape[:2]
M = cv2.getRotationMatrix2D((w//2,h//2),45,1)
rot = cv2.warpAffine(image,M,(w,h))
plt.imshow(cv2.cvtColor(rot, cv2.COLOR_BGR2RGB))
plt.title("ROTATE")
plt.show()

bright = cv2.add(image, np.ones(image.shape,dtype="uint8")*50)
plt.imshow(cv2.cvtColor(bright, cv2.COLOR_BGR2RGB))
plt.title("BRIGHT")
plt.show()
