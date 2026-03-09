@echo off
title Interview STAR Tool
echo.
echo ========================================
echo   INTERVIEW STAR TOOL
echo ========================================
echo.
echo Checking dependencies...
C:\Users\rrares\Desktop\Python\venv\Scripts\pip.exe install --quiet streamlit pandas openpyxl google-genai
echo.
echo Starting application...
echo.
C:\Users\rrares\Desktop\Python\venv\Scripts\python.exe -m streamlit run app.py
pause
