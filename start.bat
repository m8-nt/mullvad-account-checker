@echo off
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo "failed to install requirements"
    exit /b %errorlevel%
)
python main.py