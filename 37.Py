import cv2
import matplotlib.pyplot as plt
image= cv2.imread("Example2.png")
image_RGB= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
plt.imshow(image_RGB)
plt.title("RGB IMAGE")
plt.show()
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_image,cmap="gray")
plt.title("GRAY IMAGE")
plt.show()

cropped_image = image[100:300, 200:400]
cropped_rgb= cv2.cvtColor(cropped_image,cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("CROPPED IMAGE")
plt.show()





