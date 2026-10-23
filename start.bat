@echo off
title Smart Attendance AI System
cd /d "%~dp0"

echo ======================================================================
echo    SMART ATTENDANCE AI SYSTEM - Deep Vision Face Recognition
echo ======================================================================
echo  Starting server at http://127.0.0.1:8000 ...
echo.

where python >nul 2>&1
if %errorlevel%==0 (
    python run.py
) else (
    py run.py
)

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Could not start the server. 
    echo Please check the error message above.
    pause
)
