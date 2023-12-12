import cv2
import numpy as np

main_image = "D:/Emre/SRET/ImageProcessing-PythonExamples/Examples/ReadingAndWritingImages/brain.jpg"

def saltPepperNoise(image):
   row, col, ch = image.shape
   s_vs_p = 0.5
   amount = 0.04
   noisy = np.copy(image)

   num_salt = int (np.ceil(amount*image.size*s_vs_p))
   corrds = [np.random.randint(0, i-1, num_salt) for i in image.shape]
   noisy[corrds] = 1

   num_pep = int(np.ceil(amount*image.size*s_vs_p))
   corrds = [np.random.randint(0, i-1, num_pep) for i in image.shape]
   noisy[corrds] = 0

   return noisy

img = cv2.imread(main_image)
img = img/255
noise_img = saltPepperNoise(img)
cv2.imshow("Salt Pepper Noise", noise_img)
cv2.waitKey(0)