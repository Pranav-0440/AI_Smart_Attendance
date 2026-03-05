import csv
import os
from datetime import datetime

ATTENDANCE_FILE = "attendance/attendance.csv"

# runtime memory to avoid duplicate marking in same session
marked_today = set()


def mark_attendance(name):

    os.makedirs("attendance", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    # Avoid duplicate marking in same runtime
    if name in marked_today:
        return "already"

    # Create CSV file if it doesn't exist
    if not os.path.exists(ATTENDANCE_FILE):

        with open(ATTENDANCE_FILE, "w", newline="") as f:

            writer = csv.writer(f)
            writer.writerow(["Name", "Roll", "Date", "Day", "Time"])

    # Extract name and roll
    try:
        name_part, roll_part = name.split("_")
    except:
        name_part = name
        roll_part = "Unknown"

    # Check if attendance already exists today
    with open(ATTENDANCE_FILE, "r") as f:

        reader = csv.reader(f)

        for row in reader:

            if len(row) < 3:
                continue

            if row[0] == name_part and row[2] == today:
                marked_today.add(name)
                return "already"

    # Mark attendance
    now = datetime.now()

    date = now.strftime("%Y-%m-%d")
    day = now.strftime("%A")
    time = now.strftime("%H:%M:%S")

    with open(ATTENDANCE_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            name_part,
            roll_part,
            date,
            day,
            time
        ])

    marked_today.add(name)

    return "marked"