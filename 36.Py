import cv2

image= cv2.imread('Example.png')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image, (224,224))
cv2.imshow('processedimage',resized_image)
key= cv2.waitKey(0) 
if key==ord('s'):
    cv2.imwrite('greyscale_reized_image.jpg',resized_image)
    print("Image saved as greyscale_reized_image.jpg")
else:
    print("image not saved")

cv2.destroyAllWindows()
print(f"Processed image Dimmensions:{resized_image.shape}") 


