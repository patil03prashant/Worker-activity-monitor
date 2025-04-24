@echo off
:: Activate the conda environment and run the Python script

:: Initialize Conda
CALL "C:\Users\adas.bangalore\AppData\Local\miniconda3\condabin\conda.bat" activate mediapipe_env

:: Change to script directory
cd /d D:\assi

:: Run the Python script
python worker_activity_system.py

:: Keep the window open if there's an error
PAUSE
