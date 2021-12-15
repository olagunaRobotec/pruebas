import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

from tkinter import *

main = Tk()
main.title("LPR Recognization")
main.geometry("720x480")


def Camara():
    placa = []
    # captura = cv2.VideoCapture(0)
    captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
    leido, imageIP = captura.read()

    if leido == True:
        path = "C:\FotoLPR/"
        file = "7.jpg"

    # imagen de camara ip
    cv2.imwrite("C:\Fotos\Foto.png", imageIP)

    # imagen test leida desde directorio

    image_test = cv2.imread(path + file)
    new_weight = 640;
    new_height = 480;

    d_size = (new_weight, new_height);
    imageIP = cv2.resize(imageIP, d_size, interpolation=cv2.INTER_AREA)
    image_test = cv2.resize(image_test, d_size, interpolation=cv2.INTER_AREA)

    gray = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3, 3))
    #gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray, 160, 160)
    canny = cv2.dilate(canny, None, iterations=1)

    cn, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cn:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.06 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len (approx) == 4 and area > 9000:
            print('area= ', area)
            print('w= ', w)
            print('h= ', h)
            aspect_ratio = float(w) / h
            print('AS= ', aspect_ratio)

            if aspect_ratio > 2:
                cv2.drawContours(image_test, [c], 0, (0, 255, 0), 3)
                placa = gray[y:y + h, x:x + w]
                cv2.imshow('Placa', placa)
                text = pytesseract.image_to_string(placa, config='--psm 11')
                print('text', text)
    cv2.imshow('ImageLPR', image_test)
    cv2.imshow('ImageIP', imageIP)
    cv2.moveWindow("ImageLPR", 700, 60)
    cv2.moveWindow("ImageIP", 10, 60)
    cv2.waitKey(0)

frame1 = Frame(main, bg="white")
frame1.pack(expand=True, fill='both')
Boton1 = Button(frame1, text="Recognize LPR", command=Camara)
Boton1.place(relx=.35, rely=.05, relwidth=.25, relheight=.1)
#BotonSa = Button(frame1, text="Salir", command=)
#BotonSa.place(relx=.35, rely=.60, relwidth=.25, relheight=.1)
main.mainloop()