import cv2 as cv
import numpy as np

main_image = "D:/Emre/SRET/ImageProcessing-PythonExamples/Examples/ReadingAndWritingImages/brain.jpg"

img = cv.imread(main_image)
cv.imshow("Original Image", img)

def gaussian_noise(image):
   row, col, ch = image.shape
   mean = 0
   var = 0.05
   sigma = var**0.5

   gauss = np.random.normal(mean, sigma,(row,col,ch))
   gauss = gauss.reshape(row, col, ch)
   noisy = image + gauss

   return noisy

img = cv.imread(main_image)
img = img/255
noise_img = gaussian_noise(img)
cv.imshow("Gaussian Noise", noise_img)
cv.waitKey(0)