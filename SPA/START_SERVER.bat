@echo off
REM ========================================
REM Start Django Development Server
REM ========================================

echo.
echo ================================
echo    Starting Django Server
echo ================================
echo.

REM Navigate to SPA directory
cd /d "%~dp0"

REM Activate virtual environment if exists
if exist ".venv\Scripts\activate.bat" (
    echo [*] Activating virtual environment...
    call .venv\Scripts\activate.bat
)

REM Run Django server
echo [*] Starting development server...
echo [*] Access at: http://127.0.0.1:8000/
echo [*] Login page: http://127.0.0.1:8000/login/
echo [*] Register page: http://127.0.0.1:8000/register/
echo.
echo Press CTRL+C to stop the server
echo.

python manage.py runserver

pause

