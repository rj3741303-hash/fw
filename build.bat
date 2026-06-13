@echo off
REM ===== ساخت EXE روی ویندوز (اگر پایتون نصب باشد) =====
REM 1) پایتون را از python.org نصب کن و گزینه Add to PATH را بزن
REM 2) این فایل را دابل‌کلیک کن

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller
pyinstaller --onefile --name fw fw.py

echo.
echo ============================================
echo فایل خروجی در پوشه dist\fw.exe ساخته شد
echo ============================================
pause
