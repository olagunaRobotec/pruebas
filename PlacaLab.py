import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
path = "C:\FotoLPR/"
file = "7.jpg"
# file = "Recorte.jpg"

imgP = cv2.imread(path + file)
# imgIP = cv2.VideoCapture("rtsp://admin:Robotec.123@192.168.1.129:554/sub")


while True:
    imgP = cv2.imread(path + file)
    #ret, imgP = imgP.read()
    new_weight = 640;
    new_height = 480;
    d_size = (new_weight, new_height)
    imgP = cv2.resize(imgP, d_size, interpolation=cv2.INTER_AREA)

    lab = cv2.cvtColor(imgP, cv2.COLOR_BGR2Lab)
    Lmax = 255
    Amax = 160
    Bmax = 255
    # Lmax = int(input("Digite valor Lmax "))
    # Amax = int(input("Digite valor Amax "))
    # Bmax = int(input("Digite valor Bmax "))
    cv2.inRange(lab, (150, 80, 160), (Lmax, Amax, Bmax), lab)
    BGR = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
    gray = cv2.cvtColor(BGR, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 160, 160)
    canny = cv2.dilate(canny, None, iterations=1)

    cn, _ = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in cn:
        area = cv2.contourArea(c)
        x, y, w, h = cv2.boundingRect(c)
        epsilon = 0.06 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)

        if len(approx) == 4 and area > 19000:
            print('area= ', area)
            print('w= ', w)
            print('h= ', h)
            aspect_ratio = float(w) / h
            print('AS= ', aspect_ratio)

            if aspect_ratio > 1.5:
                #cv2.drawContours(imgP, [c], 0, (0, 255, 0), 3)
                placa = gray[y:y + h, x:x + w]
                cv2.imshow('Placa', placa)
                imgP = cv2.imwrite("C:\FotoLPR\Placa.jpg", placa)
                if imgP != 0:
                    print("Archivo enviado al lugar")
                else:
                    print("no se capturado nada")
                text = pytesseract.image_to_string(placa, config='--psm 11')
                print('text', text)
    cv2.imshow("CAmara", imgP)
    k = cv2.waitKey(1)
    if k == 113:
        cv2.destroyWindow("CAmara")
        break
cv2.destroyAllWindows()
