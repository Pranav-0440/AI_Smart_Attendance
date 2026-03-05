import cv2
import os
import numpy as np

DATASET_PATH = "dataset"


def train_model():

    faces = []
    labels = []
    label_map = {}

    label_id = 0

    if not os.path.exists(DATASET_PATH):
        raise Exception("Dataset folder not found!")

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    for person in os.listdir(DATASET_PATH):

        person_path = os.path.join(DATASET_PATH, person)

        # Skip non-directories
        if not os.path.isdir(person_path):
            continue

        label_map[label_id] = person

        for img in os.listdir(person_path):

            img_path = os.path.join(person_path, img)

            # Skip hidden or non-image files
            if not img.lower().endswith((".png", ".jpg", ".jpeg")):
                continue

            image = cv2.imread(img_path)

            if image is None:
                continue

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            detected_faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in detected_faces:

                face = gray[y:y+h, x:x+w]
                face = cv2.resize(face, (200, 200))

                faces.append(face)
                labels.append(label_id)

        label_id += 1

    if len(faces) == 0:
        raise Exception("No faces found in dataset. Please register students first.")

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    recognizer.train(faces, np.array(labels))

    print("Model trained successfully on", len(faces), "images")

    return recognizer, label_map