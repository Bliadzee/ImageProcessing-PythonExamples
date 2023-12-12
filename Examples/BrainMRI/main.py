import cv2
import numpy as np

img = cv2.imread("D:/Emre/SRET/ImageProcessing-PythonExamples/Examples/BrainMRI/BrainMRI.jpg")

median = cv2.medianBlur(img, 5)

compare = np.concatenate((img, median), axis=1)

cv2.imshow('image', compare)
cv2.waitKey(0)
cv2.destroyAllWindows()
