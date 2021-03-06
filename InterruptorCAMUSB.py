import cv2

xI, yI, xF, yF = 0, 0, 0, 0
interruptor = False


def dibujar(event, x, y, flags, param):
    global xI, yI, xF, yF, interruptor, imageIP, path, file1
    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        interruptor = False

    if event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        interruptor = True
        recorte = imageIP[yI:yF, xI:xF, :]
        cv2.imwrite(path + file1, recorte)
        cv2.imshow("RecorteIP", recorte)

path = "C:\FotoLPR/"
#file = "4.jpg"
file1 = "Recorte.jpg"

captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, imageIP = captura.read()

new_weight = 640;
new_height = 480;
dsize = (new_weight, new_height)

cv2.namedWindow('display')
cv2.setMouseCallback('display', dibujar)

while True:
    ret, imageIP = captura.read()

    if interruptor:
        cv2.rectangle(imageIP, (xI, yI), (xF, yF), (0, 255, 0), 3)
    cv2.imshow('display', imageIP)

    k = cv2.waitKey(1) & 0xff
    if k == 113:
        print("XI", xI)
        print("YI", yI)
        print("XF", xF)
        print("YF", yF)
        break
cv2.destroyAllWindows()