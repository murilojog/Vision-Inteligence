@echo off
pip install -r requirements.txt
rmdir /s /q build dist VisionIntelligence.spec
pyinstaller --onefile --windowed --name "Vision Intelligence - Murilo" main.py
REM Sign executable if certificate present
if exist cert.pfx (
  signtool sign /f cert.pfx /p yourpassword /tr http://timestamp.digicert.com /td sha256 /fd sha256 dist\Vision Intelligence - Murilo.exe
)
REM Copy Tesseract files
xcopy /e /i tesseract dist\Vision Intelligence - Murilo\tesseract
REM Build installer via Inno Setup
if exist "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" (
    "C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer_script.iss
) else (
    echo Inno Setup não encontrado.
)
pause