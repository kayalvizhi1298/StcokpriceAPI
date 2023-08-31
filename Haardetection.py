import numpy as np
import cv2
import pandas as pd
from google.colab.patches import cv_imshow
face_cascade = cv2.CascadeClassifier('C:\Users\Admin\Downloads\haarcascade_frontalface_alt.xml')
# eye_cascade = cv2.CascadeClassifier('/content/haarcascade_eye.xml')

image = cv2.imread('/content/drive/MyDrive/Images/images.jfif')
# print(image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,1.3,2)
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)
  
cv_imshow(image)