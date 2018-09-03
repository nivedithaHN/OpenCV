
# coding: utf-8

# In[95]:


#Choose RGB image - Plot R, G & B separately
import matplotlib.pyplot as plt
import cv2


# In[96]:


#Read the image
img = cv2.imread("img5.jpg")
#Image type 
type(img)


# In[97]:


#Shape of image array
img.shape
#3 stands for color channel.
#There is a difference in pixel ordering in OpenCV & Matplotlib 
#Matplotlib: RGB
#OpenCV: BGR


# In[98]:


#Print image in new window by specifying it's name externally
cv2.imshow("Image",img)
#Image displays for 5 secs and then destroys the window  
cv2.waitKey(5000)
cv2.destroyAllWindows()
#Image displays till you press '0'
#cv2.waitKey(0)


# In[99]:


#Display part of the image
img_part = img[170:,100:200]
cv2.imshow("Part of image",img_part)
cv2.waitKey(5000)
cv2.destroyAllWindows()


# In[100]:


#Print the image into b,r and g components
b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

#Alternative spliting -> split() is costly in terms of time.
#b,g,r = cv2.split(img)

#Display each cmponent
cv2.imshow("B Component",b)
cv2.imshow("G Component",g)
cv2.imshow("R Component",r)

cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[101]:


#Display original image by merging b,g and r
new_img = cv2.merge([b,g,r])
cv2.imshow("Original image formed by merging bgr", new_img)
cv2.waitKey(10000)
cv2.destroyAllWindows()


# In[102]:


#For Better visualization
plt.subplot(221),plt.imshow(img, 'gray'),plt.title('Original Image')
plt.subplot(222),plt.imshow(b, 'gray'),plt.title('B Component')
plt.subplot(223),plt.imshow(g, 'gray'),plt.title('G Component')
plt.subplot(224),plt.imshow(r, 'gray'),plt.title('R Component')
plt.show()

