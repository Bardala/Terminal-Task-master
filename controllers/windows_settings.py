import subprocess

from controllers.base_controller import BaseController
from database.sql_data_store import SqlDataStore


class WindowsSettings(BaseController):

    def __init__(self, cmd_name: str, db: SqlDataStore, cmd_color: str):
        super().__init__(cmd_name, db, cmd_color)
        self.command_dict = {
            "light": self.turn_on_light_mode,
            "dark": self.turn_on_dark_mode,
            "apps_light": self.turn_on_apps_light_mode,
            "apps_dark": self.turn_on_apps_dark_mode,
            "clear": self.clear_screen,
            "help": self.help,
        }

    def turn_on_light_mode(self):
        subprocess.run(
            "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f",
            shell=True,
        )
        print("Light mode turned on")

    def turn_on_dark_mode(self):
        subprocess.run(
            "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f",
            shell=True,
        )
        print("Dark mode turned on")

    def turn_on_apps_light_mode(self):
        subprocess.run(
            "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 1 /f",
            shell=True,
        )
        print("Apps light mode turned on")

    def turn_on_apps_dark_mode(self):
        subprocess.run(
            "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v SystemUsesLightTheme /t REG_DWORD /d 0 /f",
            shell=True,
        )
        print("Apps dark mode turned on")
