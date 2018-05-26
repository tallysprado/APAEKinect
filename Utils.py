import cv2
0
def capture():
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()

        cv2.imshow('Camera',frame)

        if(cv2.waitKey(3)==ord('s')):
            break
    cap.release()
    cv2.destroyAllWindows()