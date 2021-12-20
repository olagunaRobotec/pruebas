import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

path = "C:\FotoLPR/"
#file = "4.jpg"
file1 = "Recorte.jpg"
placa = []

#img = cv2.imread(path + file)
captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
ret, imageIP = captura.read()
new_weight = 640;
new_height = 480;
dsize = (new_weight, new_height);

#img1 = cv2.resize(image, dsize, interpolation=cv2.INTER_AREA)
crop_img = imageIP[209:459, 62:226]
cv2.imwrite(path + file1, crop_img)
leido =1

while True:
    ret, imageIP = captura.read()
    imageIP = cv2.resize(imageIP, dsize, interpolation=cv2.INTER_AREA)
    cv2.imshow('CamaraIP', imageIP)

    #crop_img = cv2.imread(path + file)
    #crop_img = cv2.resize(crop_img, dsize, interpolation=cv2.INTER_AREA)

    new_weightC = 320;
    new_heightC = 240;
    dsizeC = (new_weightC, new_heightC);
    crop_img = cv2.resize(crop_img, dsizeC, interpolation=cv2.INTER_AREA)
    cv2.imshow('Crop', crop_img)
    k = cv2.waitKey(1)

    if k == 113:
        # print("XI", xI)
        # print("YI", yI)
        # print("XF", xF)
        # print("YF", yF)
        cv2.destroyWindow("CamaraIP")
        break

if leido == 1:
    crop_imgG = cv2.imread(path + file1)
    gray = cv2.cvtColor(crop_imgG, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3, 3))
    #gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray, 160, 160)
    canny = cv2.dilate(canny, None, iterations=1)

    cn, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cn:
        cv2.drawContours(crop_imgG, [c], 0, (0, 255, 0), 2)
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        #epsilon = 0.01 * cv2.arcLength(c, True)
        #approx = cv2.approxPolyDP(c, epsilon, True)

        if area > 1000:
            print('area= ', area)
            print('w= ', w)
            print('h= ', h)
            aspect_ratio = float(w) / h
            print('AS= ', aspect_ratio)

            #if aspect_ratio > 1:
            cv2.drawContours(crop_img, [c], 0, (0, 255, 0), 3)
                #placa = gray[y:y + h, x:x + w]
                #cv2.imshow('Placa', placa)
                #imgP = cv2.imwrite("C:\FotoLPR\Placa.jpg", placa)

                #if imgP != 0:
                #   print("Archivo enviado al lugar")
                #else:
                #    print("no se capturado nada")
                #text = pytesseract.image_to_string(placa, config='--psm 11')
                    #print('text', text)
            cv2.imshow('recorte', crop_img)
            cv2.waitKey(0)
cv2.destroyAllWindows()