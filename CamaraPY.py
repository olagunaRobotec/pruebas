import cv2

xI, yI, xF, yF = 0, 0, 0, 0
interruptor = False

def dibujar(event, x, y, flags, param):
    global xI, yI, xF, yF, interruptor
    if event == cv2.EVENT_LBUTTONDOWN:
        xI, yI = x, y
        interruptor = False

    if event == cv2.EVENT_LBUTTONUP:
        xF, yF = x, y
        interruptor = True

#captura = cv2.VideoCapture(0)
captura = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.127:554/sub")
path = "C:\FotoLPR/"
#file = "5.jpg"
file1 = "12321.png"

#image_test = cv2.imread(path + file)
leido, imageCAP = captura.read()
cv2.namedWindow('display')
cv2.setMouseCallback('display', dibujar)

while True:
    #image_test = cv2.imread(path + file)
    ret, imageIP = captura.read()
    new_weight = 640;
    new_height = 480;
    d_size = (new_weight, new_height)
    imageIP = cv2.resize(imageIP, d_size, interpolation=cv2.INTER_AREA)

    if interruptor:
        cv2.rectangle(imageIP, (xI, yI), (xF, yF), (0, 255, 0), 3)
        crop_img = imageIP[xI:xF, yI:yF]
        #cv2.imwrite(path + file1, crop_img)
        cv2.imshow('display', crop_img)

    #image_test = cv2.resize(image_test, d_size, interpolation=cv2.INTER_AREA)
    if leido == True:
        imagenW = cv2.imwrite("C:\Fotos/Foto.png", imageCAP)
        imagenR = cv2.imread("C:\Fotos/Foto.png")

    gray = cv2.cvtColor(imagenR, cv2.COLOR_BGR2GRAY)
    gray = cv2.blur(gray, (3, 3))
    # gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(gray, 160, 160)
    canny = cv2.dilate(canny, None, iterations=1)

    cv2.imshow('ImageIP', imageIP)
    cv2.imshow('gray', gray)
    cv2.moveWindow("ImageIP", 10, 60)
    cv2.moveWindow("gray", 700, 60)
    #cv2.imshow('ImageOr', Lab)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
captura.release()
cv2.destroyAllWindows()