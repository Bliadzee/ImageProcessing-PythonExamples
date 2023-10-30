import numpy as np 
import cv2
import matplotlib.pyplot as plt

row = 256
col = 256

img = np.zeros((row,col))
img[100:105, :] = 0.5
img[:, 100:105] = 1

plt.figure(figsize=(10,4))
plt.imshow(img)
plt.show()