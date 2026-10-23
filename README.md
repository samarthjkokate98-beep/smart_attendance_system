# 🎓 Smart Attendance AI - Face Recognition Attendance System

An automated computer-vision web application that enables faculty to mark classroom attendance automatically by uploading a photo of students or capturing a live camera frame. The deep learning face recognition pipeline identifies each student present in the room and marks them as **Present** (with match confidence %) or **Absent**.

---

## 🌟 Key Features

### 👨‍🏫 Faculty Portal
- **Interactive Dashboard**: Real-time stats on total enrolled students, courses, attendance sessions conducted, and average class attendance rate.
- **Student Roster & Face Profile Enrollment**: Add students with their Roll Number, Name, Course, and upload reference face photos. The AI extracts a 128-dimensional biometric embedding.
- **Automated AI Attendance**:
  - **Group Photo Upload**: Drag-and-drop a high-res photo containing multiple students in the classroom.
  - **Live Webcam Scanning**: Capture a live snapshot from the faculty's camera/webcam.
  - **Multi-Face Detection**: Detects all faces simultaneously using OpenCV **YuNet**.
  - **Biometric Matching**: Compares each face against enrolled students using OpenCV **SFace** cosine similarity.
  - **Visual Verification Overlay**: Generates green bounding boxes for recognized students and red boxes for unknown faces.
  - **Manual Override**: Faculty can review the proposed attendance list and toggle any student between *Present* and *Absent* with one click before saving.
- **Reports & Data Export**: Historical logs of every attendance session with visual photo evidence, attendance percentages, and one-click **CSV Export**.

### 👨‍🎓 Student Portal
- **Personal Attendance Dashboard**: Real-time attendance percentage progress gauge, total classes attended, and total classes missed with standing indicators (e.g. Warning if < 75%).
- **Attendance History Log**: Detailed log of every session attended, including date, course, faculty, AI match confidence score, and cropped face snapshot taken during class.
- **Face ID Profile**: View registered reference photo and AI vector status, with the ability to upload a new front-facing reference photo anytime.



## 🔑 Demo Login Credentials

The system includes pre-seeded demo accounts with sample biometric embeddings for quick testing:

| Role | Username | Password | Notes |
| :--- | :--- | :--- | :--- |
| **Faculty** | `faculty` | `faculty123` | Full access to manage students, take attendance, view reports |
| **Student (John)** | `student_john` | `student123` | Roll No: `CS2026-001` (Face enrolled) |
| **Student (Alex)** | `student_alex` | `student123` | Roll No: `CS2026-003` (Face enrolled) |

> 💡 **Tip:** On the Sign In page, you can also click the **"Faculty Demo"** or **"Student Demo"** quick-login buttons to log in with a single click!

---

## 📸 Testing Attendance Right Away

A sample classroom image containing enrolled students is already included in `app/static/uploads/classroom_group_sample.jpg`.

1. Log in as **Faculty** (`faculty` / `faculty123`).
2. Go to **"Take Attendance"** in the top navigation.
3. Select Course: `CS101`.
4. Click **"Select Photo From Device"** and select:
   `app/static/uploads/classroom_group_sample.jpg`
5. Click **"Scan & Recognize Attendance"**.
6. The AI will instantly:
   - Detect both faces in the photo.
   - Recognize **John Doe** (Confidence: 79.2%) and **Alex Smith** (Confidence: 95.3%) and mark them **Present**!
   - Mark students who were not detected as **Absent**.
   - Show face thumbnails and bounding boxes.
7. Click **"Confirm & Save Attendance"** to record the session.

---

## 📁 Project Architecture

```
smart-attendance-system/
├── app/
│   ├── __init__.py
│   ├── main.py                # FastAPI routes and API endpoints
│   ├── database.py            # SQLite database schema, connections & helpers
│   ├── auth.py                # PBKDF2 password hashing & session management
│   ├── face_engine.py         # OpenCV YuNet & SFace multi-face recognition engine
│   ├── static/
│   │   ├── uploads/           # Uploaded classroom & session photos
│   │   │   ├── crops/         # Cropped face audit thumbnails
│   │   │   └── students/      # Reference face photos for enrolled students
│   └── templates/
│       ├── base.html          # Base layout with Tailwind CSS & navigation
│       ├── login.html         # Unified Faculty/Student login & registration
│       ├── faculty_dashboard.html # Faculty home overview & metrics
│       ├── faculty_students.html  # Student management & face photo enrollment
│       ├── faculty_take_attendance.html # Photo upload & webcam attendance scanner
│       ├── faculty_reports.html   # Attendance session logs & CSV export
│       ├── faculty_session_detail.html # Visual session inspection with photo
│       ├── student_dashboard.html # Student attendance portal
│       └── student_profile.html   # Student profile & reference face ID
├── data/
│   └── attendance.db          # SQLite database
├── models/
│   ├── download_models.py     # YuNet & SFace model downloader
│   ├── face_detection_yunet_2023mar.onnx
│   └── face_recognition_sface_2021dec.onnx
├── requirements.txt
├── run.py                     # Application startup script
└── README.md
```

---

## 🧠 Face Recognition Technology
- **Detector**: [YuNet](https://github.com/opencv/opencv_zoo/tree/master/models/face_detection_yunet) - An ultra-fast deep learning detector capable of detecting faces in real-time under varying illumination and head angles.
- **Recognizer**: [SFace](https://github.com/opencv/opencv_zoo/tree/master/models/face_recognition_sface) - Deep learning face recognition model that extracts 128-dimensional normalized embeddings and compares them using Cosine similarity.
