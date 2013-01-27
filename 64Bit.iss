; -- 64Bit.iss --
; Demonstrates installation of a program built for the x64 (a.k.a. AMD64)
; architecture.
; To successfully run this installation and the program it installs,
; you must have the "x64" edition of Windows XP or Windows Server 2003.

; SEE THE DOCUMENTATION FOR DETAILS ON CREATING .ISS SCRIPT FILES!

[Setup]
AppName=R'n'Games
AppVersion=1.0
DefaultDirName={pf}\RnGames
DefaultGroupName=RnGames
UninstallDisplayIcon={app}\R'n'Games.exe
Compression=lzma2
SolidCompression=yes
OutputDir=".\"
; "ArchitecturesAllowed=x64" specifies that Setup cannot run on
; anything but x64.
ArchitecturesAllowed=x64
; "ArchitecturesInstallIn64BitMode=x64" requests that the install be
; done in "64-bit mode" on x64, meaning it should use the native
; 64-bit Program Files directory and the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "build\exe.win-amd64-2.7\*" ; DestDir: "{app}" ; Flags : recursesubdirs
Source: "README_fr.txt"; DestDir: "{app}"; Flags: isreadme


[Icons]
Name: "{group}\R'n'Games"; Filename: "{app}\R'n'Games.exe"
Name: "{group}\Uninstall R'n'Games"; Filename: "{uninstallexe}"
