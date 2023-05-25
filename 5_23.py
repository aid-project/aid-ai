import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from PIL import Image
import cv2

arr = cv2.imread("backgroundON.jpg",0)
print(arr.shape)

#plt.imshow(im)
#plt.show()

#arr[arr != 255] = 0
unique_elements, counts = np.unique(arr, return_counts=True)

for element, count in zip(unique_elements, counts):
    print(f"Element: {element}, Count: {count}")
    pass

plt.imshow(arr, cmap=plt.cm.gray)
plt.show()