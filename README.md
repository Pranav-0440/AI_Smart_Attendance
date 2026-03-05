# 🤖 AI Smart Attendance System

An **AI-powered Smart Attendance System** that uses **Face Recognition** to automatically detect students and mark their attendance.
This system eliminates manual attendance, reduces proxy attendance, and provides a real-time dashboard to monitor records.

---

## 🚀 Features

* 👤 **Student Registration**

  * Register students with **Name, Roll Number, and Branch**
  * Capture face images using webcam

* 🎯 **Face Recognition Attendance**

  * Detect faces in real-time
  * Match with stored dataset
  * Automatically mark attendance

* 📅 **Duplicate Prevention**

  * If a student tries to mark attendance again on the same day
  * System shows **"Attendance Already Marked"**

* 📊 **Dashboard**

  * Displays attendance records
  * Visualizes attendance counts

* 💾 **CSV-based Storage**

  * Attendance stored in `attendance.csv`

---

## 🧠 Technologies Used

* **Python**
* **OpenCV**
* **Streamlit**
* **NumPy**
* **Pandas**

---

## 📂 Project Structure

```
AI_Smart_Attendance
│
├── app.py                  # Main Streamlit application
├── face_utils.py           # Face recognition training module
├── attendance_utils.py     # Attendance management
│
├── dataset/                # Student face datasets
│   ├── pranav_36/
│   └── vishal_13/
│
├── attendance/
│   └── attendance.csv      # Attendance records
│
├── data/
│   └── students.json       # Student information
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Pranav-0440/AI_Smart_Attendance.git
cd AI_Smart_Attendance
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

Activate environment

**Windows**

```bash
.venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 📸 System Workflow

### 1️⃣ Register Student

* Enter **Name**
* Enter **Roll Number**
* Enter **Branch**
* Capture face images

Images are stored in:

```
dataset/name_roll/
```

---

### 2️⃣ Start Attendance

* System trains face recognition model
* Detects student faces
* Matches dataset
* Marks attendance

Example console output:

```
Pranav marked attendance today
```

If repeated:

```
Pranav already marked attendance
```

---

### 3️⃣ View Dashboard

Displays:

* Attendance table
* Attendance count chart

---

## 📄 Attendance File Format

```
Name,Roll,Date,Day,Time
Pranav,36,2026-03-05,Thursday,12:31:32
Vishal,13,2026-03-05,Thursday,12:33:10
```

---

## 🎯 Future Improvements

* 🔐 Anti-spoofing detection
* 👁 Eye blink detection
* 🧠 Deep learning face recognition
* 🗄 Database integration (SQLite / PostgreSQL)
* 📱 Mobile compatible UI
* 📊 Advanced analytics dashboard

---

## 👨‍💻 Author

**Pranav Ghorpade**

Electronics & Telecommunication Engineering
AI | Computer Vision | Software Development

GitHub:
https://github.com/Pranav-0440

---