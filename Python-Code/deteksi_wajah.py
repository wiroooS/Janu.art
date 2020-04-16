import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0) # inisialisasi webcam laptop

detector = dlib.get_frontal_face_detector() # mengambil library wajah pada dlib

while True:
   
    ret, frame = cap.read() #membuat frame untuk output camera
    
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BG2BGR) 
    
        faces = detector(gray)
        for face in faces:
            x = face.left()
            y = face.top()
            x1 = face.right()
            y1 = face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 3)
                    
        cv2.imshow('Frame', frame) #menampilkan output camera
        
    # untuk mengakhiri tekan "q"    
    if cv2.waitKey(25) & 0xFF == ord('q'): 
        break
    
cap.release()
cv2.destroyAllWindows()
