import cv2
0
def capture():
    cam = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        cv2.imshow('Camera',frame)

        if(cv2.waitKey(3)==ord('s')):
            break
    cap.release()
    cv2.destroyAllWindows()


# segmentaçao
def bodyDetection():
    bodyCascade = cv2.CascadeClassifier('haarcascades/haarcascade_smile.xml')

    cam = cv2.VideoCapture(1)

    while (True):
        ret, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        body = bodyCascade.detectMultiScale(gray, 1.5, 5)
        for (x, y, w, h) in body:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Video 0', frame)

        if cv2.waitKey(2) == ord('s'):
            break

    cam.release()
    cv2.destroyAllWindows()
