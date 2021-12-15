import cv2
import numpy as np

path = "C:\FotoLPR/"
file = "7.jpg"
imagen = cv2.imread(path + file)
new_weight = 640;
new_height = 480;

d_size = (new_weight, new_height);
imagen = cv2.resize(imagen, d_size, interpolation=cv2.INTER_AREA)

#cv2.imshow("OR", imagen)

gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
#cv2.imshow("OR", gray)

umbral, imagenMetodo = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
mascara = np.uint8((gray<umbral)*255)
#cv2.imshow("ImgBinaria", mascara)
#cv2.imshow("ImgMetodo", imagenMetodo)
cv2.waitKey(0)

num_labels, labels, stats, centroids, = cv2.connectedComponentsWithStats(mascara, 4, cv2.CV_32S)

