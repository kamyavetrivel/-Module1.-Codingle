import cv2
import matplotlib.pyplot as plt

image_path = 'example3.png'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _ = image_rgb.shape

arrow_start = (20, 50)
arrow_end = (width - 20, 50)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

mid_x = width // 2
label_position = (mid_x - 80, 40)

cv2.putText(
    image_rgb,
    f'Width: {width}px',
    label_position,
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (255, 255, 0),
    2,
    cv2.LINE_AA
)

cv2.circle(image_rgb, arrow_start, 5, (0, 255, 0), -1)
cv2.circle(image_rgb, arrow_end, 5, (0, 255, 0), -1)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title('Image with Width Annotation')
plt.axis('off')
plt.show()
