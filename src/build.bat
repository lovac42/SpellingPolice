@echo off
set ZIP=C:\PROGRA~1\7-Zip\7z.exe a -tzip -y -r
set REPO=spelling_police
set NAME=Spelling Police
set PACKID=1410276506
set VERSION=0.1.0


quick_manifest.exe "%NAME%" "%PACKID%" >%REPO%\manifest.json
echo %VERSION% >%REPO%\VERSION

fsum -r -jm -md5 -d%REPO% * > checksum.md5
move checksum.md5 %REPO%\checksum.md5

cd %REPO%
%ZIP% ../%REPO%_v%VERSION%_Anki21.ankiaddon *

