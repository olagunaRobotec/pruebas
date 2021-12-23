import cv2
import os
import imutils

interruptor = False

personName = 'Oscar'
dataPath = 'C:/cara/FotoCARA'  # Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName

if not os.path.exists(personPath):
    print('Carpeta creada: ', personPath)
    os.makedirs(personPath)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')
faceClassif = cv2.CascadeClassifier('C:\OpenCV454\sources\data\haarcascades_cuda\haarcascade_frontalface_default.xml')
count = 0

while True:
    try:
        ret, frame = cap.read()
        if ret == False: break
        frame = imutils.resize(frame, width=640)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        FrameLive = frame.copy()
        FrameLive = imutils.resize(FrameLive, width=640)
        cv2.imshow('frame', FrameLive)
        cv2.waitKey(1)
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            count = count + 1
            if count == 5:
                cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)

    except:
        break
        cap.release()
        cv2.destroyAllWindows()
        print("ERROR")