import streamlit as st
import cv2
import os
import pandas as pd
from face_utils import train_model
from attendance_utils import mark_attendance

st.title("AI Smart Attendance System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Register Student", "Start Attendance", "Dashboard"]
)

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# ---------------- REGISTER STUDENT ----------------

if menu == "Register Student":

    st.header("Register New Student")

    name = st.text_input("Student Name")
    roll = st.text_input("Roll Number")
    branch = st.text_input("Branch")

    if st.button("Capture Face"):

        if name == "" or roll == "":
            st.warning("Enter Name and Roll Number")
        else:

            cam = cv2.VideoCapture(0)

            folder = f"dataset/{name}_{roll}"
            os.makedirs(folder, exist_ok=True)

            frame_window = st.image([])

            captured = False

            while not captured:

                ret, frame = cam.read()

                if not ret:
                    st.error("Camera not detected")
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:

                    face = gray[y:y+h, x:x+w]
                    face = cv2.resize(face, (200, 200))

                    img_path = f"{folder}/0.jpg"
                    cv2.imwrite(img_path, face)

                    captured = True

                    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                frame_window.image(frame, channels="BGR")

            cam.release()

            st.success(f"{name} registered successfully!")

# ---------------- ATTENDANCE ----------------

if menu == "Start Attendance":

    st.header("Face Recognition Attendance")

    if st.button("Start Camera"):

        recognizer, label_map = train_model()

        cam = cv2.VideoCapture(0)

        frame_window = st.image([])

        while True:

            ret, frame = cam.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:

                face_img = gray[y:y+h, x:x+w]
                face_img = cv2.resize(face_img, (200, 200))

                label, confidence = recognizer.predict(face_img)

                name = "Unknown"

                if confidence < 80:

                    name = label_map[label]

                    status = mark_attendance(name)

                    student_name = name.split("_")[0]

                    if status == "marked":
                        st.success(f"{student_name} marked attendance today")

                    elif status == "already":
                        st.warning(f"{student_name} Already Marked attendance")

                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

                cv2.putText(
                    frame,
                    f"{name} {int(confidence)}",
                    (x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    2
                )

            frame_window.image(frame, channels="BGR")

# ---------------- DASHBOARD ----------------

if menu == "Dashboard":

    st.header("Attendance Dashboard")
    
    try:

        df = pd.read_csv("attendance/attendance.csv")

        st.dataframe(df)

        st.subheader("Attendance Count")

        st.bar_chart(df["Name"].value_counts())

    except:
        st.warning("No Attendance Data Available")