import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

placa = []
# captura = cv2.VideoCapture(0)
captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
leido, image_test = captura.read()

if leido == True:
    path = "C:\FotoLPR/"
    file = "7.jpg"

    new_weight = 640;
    new_height = 480;
    d_size = (new_weight, new_height)

    # imagen de camara ip
    # AD_IP = os.environ['ADDRESS_IP']
    cv2.imwrite("C:\Fotos/Foto.png", image_test)

    # imagen test leida desde directorio
    image_test = cv2.imread(path + file)
    image_test = cv2.resize(image_test, d_size, interpolation=cv2.INTER_AREA)

    #gray = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
    #gray = cv2.blur(gray, (3, 3))
    #gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    #canny = cv2.Canny(gray, 160, 160)
    #canny = cv2.dilate(canny, None, iterations=1)

    lab = cv2.cvtColor(image_test, cv2.COLOR_BGR2Lab)
    BGR = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    gray = cv2.cvtColor(BGR, cv2. COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 160, 160)
    canny = cv2.dilate(canny, None, iterations=1)
    Lmax = 255
    Amax = 251
    Bmax = 255
    #Lmax = int(input("Digite valor Lmax "))
    #Amax = int(input("Digite valor Amax "))
    #Bmax = int(input("Digite valor Bmax "))
    imgq = cv2.inRange(lab, (150, 90, 0), (Lmax, Amax, Bmax), lab)
    #cv2.imshow("RangeLab", imgq)

    cn, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cn:
        #cv2.drawContours(image_test, [c], 0, (0, 255, 0), 2)
        #cv2.imshow("image", image_test)
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.06 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len(approx) == 4 and area > 13000:
            print('area= ', area)
            print('w= ', w)
            print('h= ', h)
            aspect_ratio = float(w) / h
            print('AS= ', aspect_ratio)

            if aspect_ratio > 1.5:
                cv2.drawContours(image_test, [c], 0, (0, 255, 0), 3)
                placa = gray[y:y + h, x:x + w]
                cv2.imshow('Placa', placa)
                imgP = cv2.imwrite("C:\FotoLPR\Placa.jpg", placa)
                if imgP != 0:
                    print("Archivo enviado al lugar")
                else:
                    print("no se capturado nada")
                text = pytesseract.image_to_string(placa, config='--psm 11')
                print('text', text)
cv2.imshow('ImageLPR', image_test)
#cv2.imshow('Lab', canny)
#cv2.imshow('ImageIP', imageIP)
#cv2.moveWindow("ImageLPR", 700, 60)
#cv2.moveWindow("Lab", 10, 60)
cv2.waitKey(0)
cv2.destroyAllWindows()