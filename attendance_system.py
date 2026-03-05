import cv2
import os
from attendance_utils import mark_attendance

def start_attendance(recognizer,label_map):

    face_cascade=cv2.CascadeClassifier(
        cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
    )

    cam=cv2.VideoCapture(0)

    while True:

        ret,frame=cam.read()

        if not ret:
            break

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces=face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            face=gray[y:y+h,x:x+w]
            face=cv2.resize(face,(200,200))

            label,confidence=recognizer.predict(face)

            name="Unknown"

            if confidence<80:

                name=label_map[label]

                status=mark_attendance(name)

                if status=="marked":
                    print(f"{name.split('_')[0]} marked attendance today")

                elif status=="already":
                    print(f"{name.split('_')[0]} Already Marked attendance")

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.putText(frame,name,(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,(0,255,0),2)

        cv2.imshow("Attendance Camera",frame)

        if cv2.waitKey(1)==ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()