"""
Entrypoint script to start the Smart Face Recognition Attendance System.
"""
import uvicorn
import os
import sys

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)

    print("=" * 70)
    print("   SMART ATTENDANCE AI SYSTEM - Deep Vision Face Recognition")
    print("=" * 70)
    print(" [*] Web Server: http://127.0.0.1:8000")
    print(" [*] Faculty Login: username: 'faculty'     | password: 'faculty123'")
    print(" [*] Student Login: username: 'student_john'| password: 'student123'")
    print("=" * 70)
    
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=False)
