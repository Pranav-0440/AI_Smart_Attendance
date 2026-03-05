import cv2
import json
import os
import streamlit as st

students=[]

DATA_PATH="data/students.json"

face_cascade=cv2.CascadeClassifier(
    cv2.data.haarcascades+"haarcascade_frontalface_default.xml"
)

def capture_face(name,roll):

    cam=cv2.VideoCapture(0)

    folder=f"dataset/{name}_{roll}"
    os.makedirs(folder,exist_ok=True)

    while True:

        ret,frame=cam.read()

        if not ret:
            break

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        faces=face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            face=gray[y:y+h,x:x+w]
            face=cv2.resize(face,(200,200))

            img_path=f"{folder}/0.jpg"

            cv2.imwrite(img_path,face)

            cam.release()
            cv2.destroyAllWindows()

            return True

        cv2.imshow("Capture Face",frame)

        if cv2.waitKey(1)==ord("q"):
            break

    cam.release()
    cv2.destroyAllWindows()

    return False


def register_page():

    st.header("Student Registration")

    name=st.text_input("Name")
    roll=st.text_input("Roll Number")
    branch=st.text_input("Branch")

    if st.button("Capture Face"):

        success=capture_face(name,roll)

        if success:

            student={
                "name":name,
                "roll":roll,
                "branch":branch
            }

            students.append(student)

            st.success("Face Captured Successfully")

    if st.button("Final Submit"):

        os.makedirs("data",exist_ok=True)

        with open(DATA_PATH,"w") as f:

            json.dump(students,f)

        st.success("All Students Saved")