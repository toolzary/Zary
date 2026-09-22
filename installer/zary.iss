
#define MyAppName "Zary"
#define MyAppVersion "0.1.0"
#define MyAppPublisher "Toolzary"

[Setup]

AppId={{D80FEB1F-BE4A-4CE8-B90D-11698B0CDAB1}

AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}

DefaultDirName={autopf}\Zary
DefaultGroupName=Zary

ArchitecturesAllowed=x64compatible
ArchitecturesInstallIn64BitMode=x64compatible

LicenseFile=D:\All Toolzary\zary\LICENSE

OutputDir=D:\All Toolzary\zary\installer\Output
OutputBaseFilename=Zary-Setup

SetupIconFile=D:\All Toolzary\zary\assets\logo.ico

Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]

Name: "english"; MessagesFile: "compiler:Default.isl"


[Files]

Source: "D:\All Toolzary\zary\dist\zary.exe"; \
    DestDir: "{app}"; \
    Flags: ignoreversion

Source: "D:\All Toolzary\zary\assets\logo.ico"; \
    DestDir: "{app}"; \
    DestName: "zary.ico"; \
    Flags: ignoreversion


[Icons]

; Start Menu shortcut

Name: "{autoprograms}\Zary"; \
    Filename: "{sys}\WindowsPowerShell\v1.0\powershell.exe"; \
    Parameters: "-NoExit -ExecutionPolicy Bypass -Command ""& '{app}\zary.exe'"""; \
    WorkingDir: "{app}"; \
    IconFilename: "{app}\zary.ico"


; Desktop shortcut

Name: "{autodesktop}\Zary"; \
    Filename: "{sys}\WindowsPowerShell\v1.0\powershell.exe"; \
    Parameters: "-NoExit -ExecutionPolicy Bypass -Command ""& '{app}\zary.exe'"""; \
    WorkingDir: "{app}"; \
    IconFilename: "{app}\zary.ico"


[Registry]

; Add Zary to the system PATH

Root: HKLM; \
    Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; \
    ValueName: "Path"; \
    ValueData: "{olddata};{app}"; \
    Flags: preservestringtype
