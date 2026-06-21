; Inno Setup Script for Pact PDF Application
; Generates a clean, branded, multi-step installer (.exe) for Windows

#define MyAppName "Pact"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "Ebenezer Essel"
#define MyAppExeName "Pact.exe"

[Setup]
AppId={{5E5868E9-23CE-45FC-93C9-1065114D3C5C}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={localappdata}\{#MyAppName}
DisableDirPage=no
DefaultGroupName={#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=dist
OutputBaseFilename=PactInstaller
Compression=lzma
SolidCompression=yes
WizardStyle=modern

; Branding and Wizard Aesthetics
SetupIconFile=assets\Pact.ico
WizardImageFile=assets\wizard_image.bmp
WizardSmallImageFile=assets\wizard_small_image.bmp
LicenseFile=LICENSE.txt
DisableWelcomePage=no

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "dist\Pact.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\.env"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent
