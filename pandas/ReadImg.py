import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('test.jpg') 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
image = np.array(image) # Convert img to numpy array
plt.imshow(image)
plt.show()