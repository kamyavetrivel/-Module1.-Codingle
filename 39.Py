import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title,image):
    plt.figure(figsize=(8,8))
    if len(image.shape)== 2:
        plt.imshow(image,cmap='grey')
    else: 
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def interactive_edge_detection(image_path):
    image= cv2.imread(image_path)
    if image is None:
        print("Error: image not found!")
        return 
    
    gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original grayscale image", gray_image)
    print("Select an option:")
    print("1. Sobel Edge Detection")
    print("2. Canny Edge detection")
    print("3. Canny Edge detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6.Exit")
    
    while True:
        choice=input("Enter your choice between (1-6):")

        if choice == "1":
            Sobel_x=cv2.Sobel(gray_image, cv2.CV_64F,1,0, ksize=3)
            Sobel_y=cv2.Sobel(gray_image, cv2.CV_64F,0,1, ksize=3)
            combined_sobel = cv2.bitwise_or(Sobel_x.astype(np.uint8),Sobel_y.astype(np.uint8))
            display_image("Sobel Edge detection",combined_sobel)
        elif choice == "2":
            print("Adjust thresholds for Canny(default:100 and 200)")
            lower_thresh = int(input("Enter lower treshold:")) 
            upper_thresh = int(input("Enter Upper threshold:"))
            edges= cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)
        elif choice == "3":
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection",np.abs(laplacian).astype(np.uint8))
        elif choice == "4":
            print("Adjust kernal size for Gaussian blur (must be odd, default:5)")
            kernal_size = int(input("Enter kernal size(odd number:)"))
            blurred = cv2.GaussianBlur(image, (kernal_size, kernal_size),0)
            display_image("Gaussian smoothed image",blurred)

        elif choice == "5":
            print("Adjust Kernal size for Median filtering(must be odd, default: 5)")
            kernal_size=int(input("Enter kernal size(odd number)"))
            median_filtered = cv2.medianBlur(image, kernal_size)
            display_image("Median Filtered Image", median_filtered)
        elif choice == "6":
            print("Existing..")
            break
        else:
            print("invalid choice. Please select a number that is between 1 and 6.")
interactive_edge_detection('Example3.png')
