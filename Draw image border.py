
# coding: utf-8

# In[1]:


import cv2 
import numpy as np
import matplotlib.pyplot as plt


# In[19]:


#Set border color
border_color = [225,22,225]


# In[20]:


# Read image
img1 = cv2.imread("img.jpg")
# Image shape
img1.shape


# In[21]:


#Display image
cv2.imshow("Image",img1)
cv2.waitKey(0)


# In[25]:


newImg = cv2.copyMakeBorder(img1,10,10,10,10, cv2.BORDER_CONSTANT, value = border_color)

plt.title("Image with border")
imgplot = plt.imshow(newImg, None)
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)

