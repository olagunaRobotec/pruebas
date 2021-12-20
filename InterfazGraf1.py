import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
from tkinter import *

main = Tk()
main.title("LPR Recognization")
main.geometry("720x480")

path = "C:\FotoLPR/"
file = "7.jpg"
#file = "Recorte.jpg"

imgP = cv2.imread(path + file)
#captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
#ret, imageIP = captura.read()

def Camara():
while True:
    imgP = cv2.imread(path + file)
    new_weight = 640;
    new_height = 480;
    d_size = (new_weight, new_height)
    imgP = cv2.resize(imgP, d_size, interpolation=cv2.INTER_AREA)
    lab = cv2.cvtColor(imgP, cv2.COLOR_BGR2Lab)
    #Amax = 201
    #Bmax = 250
    Lmax = int(input("Digite valor Lmax "))
    Amax = int(input("Digite valor Amax "))
    Bmax = int(input("Digite valor Bmax "))
    imgq = cv2.inRange(lab, (0, 0, 0), (Lmax, Amax, Bmax, lab))
    cv2.imshow("CAmara", imgq)
    cv2.waitKey(0)
    k = cv2.waitKey(0)
    if k == 113:
        cv2.destroyWindow("CAmara")
    break

frame1 = Frame(main, bg="white")
frame1.pack(expand=True, fill='both')
Boton1 = Button(frame1, text="Recognize LPR", command=Camara)
Boton1.place(relx=.35, rely=.05, relwidth=.25, relheight=.1)
# Spinbox = Spinbox(frame1, values =("reprobado", "ochenta", "noventa", "cien")).place(x=100, y=100)
vertical = Scale(frame1, from_=0, to=200).place(x=100, y=100)
print(vertical)
# BotonSa = Button(frame1, text="Salir", command=)
# BotonSa.place(relx=.35, rely=.60, relwidth=.25, relheight=.1)
main.mainloop()
