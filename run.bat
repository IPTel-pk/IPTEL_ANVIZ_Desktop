@echo off

:: Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo Please create it first using: python -m venv venv
    pause
    exit /b 1
)

:: Activate the environment
call venv\Scripts\activate.bat

:: Run the application
python main.py

:: If the app crashes, keep the window open so you can read the error
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] The application exited with an error.
    pause
)