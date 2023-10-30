import cv2
import numpy as np

absolutePath = "D:/Emre/SRET/ImageProcessing-PythonExamples/Examples/ReadingAndWritingImages/brain.jpg"

image1 = cv2.imread(absolutePath)

# cv2.imshow("Brain", image1)

print(f"Image size: {image1.size}")
print(f"Image dtype: {image1.dtype}")
print(f"Image shape: {image1.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()