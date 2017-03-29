@echo off
@set pwd=%~dp0
python %pwd%\get_wallpaper.py %pwd%\background.jpg
reg add "hkcu\Control Panel\desktop" /v wallpaper /d "%pwd%\background.jpg" /f
reg add "hkcu\Control Panel\desktop" /v WallpaperStyle /d "10" /f
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
exit