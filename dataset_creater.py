#import packages

import cv2
import numpy as np
import sqlite3

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0);

def insertorupdate(Id, Name, age):
    conn = sqlite3.connect("sqlite.db")
    cmd="SELECT * FROM STUDENTS WHERE ID=" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExists = 0
    for row in cursor:
        isRecordExists = 1
    if(isRecordExists ==1):
        conn.execute("UPDATE STUDENTS SET Name=? WHERE ID=?", parameters=(Name, Id,))
        conn.execute("UPDATE STUDENTS SET age=? WHERE ID=?", parameters=(age, Id,))
    else:
        conn.execute("INSERT INTO STUDENTS (Id, Name, age) VALUES (?, ?, ?)", parameters=(Id, Name, age))
    conn.commit()
    conn.close()

Id=input('Enter User Id')
Name=input('Enter User Name')
age=input('Enter User Age')
insertorupdate(Id, Name, age)

sampleNum=0;                     #assume there is no samples in dataset
while(True):
    ret,img=cam.read();          #open camera
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)     #image convert into BGRGRAY COLOR
    faces=faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1;      #if face is detected increments
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)                       #delay time
    cv2.imshow("Face",img)
    cv2.waitKey(1);
    if (sampleNum>20):
        break;

cam.release()
cv2.destroyAllWindows()
