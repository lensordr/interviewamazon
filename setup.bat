@echo off
title Setup - Interview STAR Tool
echo.
echo ========================================
echo   INSTALLING DEPENDENCIES...
echo ========================================
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo ========================================
echo   SETUP COMPLETE!
echo ========================================
echo.
pause
