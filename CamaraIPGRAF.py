from tkinter import *
from PIL import Image, ImageTk  # pip install Pillow
import cv2  # pip install opencv-contrib-python
import sys


def onClossing():
    main.quit()
    cap.release()
    print("Cámara desconectada")
    main.destroy()


def callback():
    #cap.open(url)
    ret, frame = cap.read()

    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((640, 480))
        tkimage = ImageTk.PhotoImage(img)
        label.configure(image=tkimage)
        label.image = tkimage
        main.after(1, callback)

    else:
        onClossing()


def conectar():
    global obj, mens
    host = '192.168.1.127'
    port = 554
    # Se importa el módulo
    import socket

    # Creación de un objeto socket (lado cliente)
    obj = socket.socket()

    # Conexión con el servidor. Parametros: IP (puede ser del tipo 192.168.1.1 o localhost), Puerto
    obj.connect((host, port))
    print("Conectado al servidor")

    while True:
        mens = input("Mensaje desde Cliente a Servidor >> ")
        # Imprimimos la palabra Adios para cuando se cierre la conexion
        print("Envio exitoso")
        obj.send(mens)


def cerrar():
    # Imprimimos la palabra Adios para cuando se cierre la conexion
    print("Conexión cerrada")
    # Cerramos la instancia del objeto servidor
    obj.close()


url = "rtsp://admin:Robotec.123@192.168.1.127:554/sub"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Cámara inicializada")
else:
    sys.exit("Cámara desconectada")

main = Tk()
main.title("LPR Recognization")
main.geometry("900x480")
main.protocol("WM_DELETE_WINDOW", onClossing)

label = Label(main)
label.grid(row=0)
Boton1 = Button(main, text="connect", command=conectar)
Boton1.place(x=685, y=20, width=60, height=30)

main.after(1, callback)
main.mainloop()
