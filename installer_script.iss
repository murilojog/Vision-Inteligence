[Setup]
AppName=Vision Intelligence – Murilo
AppVersion=1.0
DefaultDirName={pf}\Vision Intelligence – Murilo
DefaultGroupName=Vision Intelligence – Murilo
OutputBaseFilename=Vision_Intelligence_Murilo_Setup
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\\Vision Intelligence - Murilo.exe"; DestDir: "{app}"; Flags: ignoreversion
; Include bundled Tesseract
Source: "tesseract\\*"; DestDir: "{app}\\tesseract"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\Vision Intelligence – Murilo"; Filename: "{app}\Vision Intelligence - Murilo.exe"
Name: "{group}\Desinstalar Vision Intelligence – Murilo"; Filename: "{uninstallexe}"