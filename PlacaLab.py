import cv2

path = "C:\FotoLPR/"
file = "Recorte.jpg"
#file = "Recorte.jpg"

imgP = cv2.imread(path + file)
#captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
#ret, imageIP = captura.read()

while True:
    imgP = cv2.imread(path + file)
    new_weight = 640;
    new_height = 480;
    d_size = (new_weight, new_height)
    imgP = cv2.resize(imgP, d_size, interpolation=cv2.INTER_AREA)
    lab = cv2.cvtColor(imgP, cv2.COLOR_BGR2Lab)
    Lmax = 255
    Amax = 160
    #Bmax = 255
    #Lmax = int(input("Digite valor Lmax "))
    #Amax = int(input("Digite valor Amax "))
    Bmax = int(input("Digite valor Bmax "))
    imgq = cv2.inRange(lab, (150, 80, 160), (Lmax, Amax, Bmax), lab)
    cv2.imshow("CAmara", imgq)
    k = cv2.waitKey(1)
    if k == 113:
        cv2.destroyWindow("CAmara")
        break
cv2.destroyAllWindows()