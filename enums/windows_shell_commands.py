from enum import Enum


class WindowsShellCommand(Enum):
    LIGHT = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f"
    DARK = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f"
    APPS_LIGHT = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f"
    APPS_DARK = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f"
    GROOVE_MUSIC = "start mswindowsmusic:"
    EDGE = "start microsoft-edge:"
    STORE = "start ms-windows-store:"
    SETTINGS = "start ms-settings:"
    CALENDAR = "start outlookcal:"
    MAIL = "start outlookmail:"
    PHOTOS = "start ms-windows.photos:"
    CAMERA = "start ms-windows.camera:"
    MAPS = "start bingmaps:"
    GOOGLE = "start microsoft-edge:https://www.google.com/search?q="
    BING = "start microsoft-edge:https://www.bing.com/search?q="
    YOUTUBE = "start microsoft-edge:https://www.youtube.com/results?search_query="
    PRAYER = "start microsoft-edge:https://www.google.com/search?q=prayer+times"
