import subprocess

from controllers.base_controller import BaseController
from database.sql_data_store import SqlDataStore
from enums.windows_shell_commands import WindowsShellCommand
from utils.helpers import colored_input


class WindowsSettings(BaseController):
    def __init__(self, cmd_name: str, db: SqlDataStore, cmd_color: str):
        super().__init__(cmd_name, db, cmd_color)
        self.command_dict = {
            "light": self.turn_on_light_mode,
            "dark": self.turn_on_dark_mode,
            "apps_light": self.turn_on_apps_light_mode,
            "apps_dark": self.turn_on_apps_dark_mode,
            "music": self.open_grove_music,
            "edge": self.open_edge,
            "store": self.open_windows_store,
            "settings": self.open_windows_settings,
            "calendar": self.open_windows_calendar,
            "mail": self.open_windows_mail,
            "photos": self.open_windows_photos,
            "camera": self.open_windows_camera,
            "maps": self.open_windows_maps,
            "google": self.search_on_google,
            "bing": self.ask_bing,
            "youtube": self.search_on_youtube,
            "prayer": self.get_muslim_prayer_times,
            "clear": self.clear_screen,
            "help": self.help,
        }

    def turn_on_light_mode(self):
        subprocess.run(WindowsShellCommand.LIGHT.value, shell=True)
        print("Light mode turned on")

    def turn_on_dark_mode(self):
        subprocess.run(WindowsShellCommand.DARK.value, shell=True)
        print("Dark mode turned on")

    def turn_on_apps_light_mode(self):
        subprocess.run(WindowsShellCommand.APPS_LIGHT.value, shell=True)
        print("Apps light mode turned on")

    def turn_on_apps_dark_mode(self):
        subprocess.run(WindowsShellCommand.APPS_DARK.value, shell=True)
        print("Apps dark mode turned on")

    def open_grove_music(self):
        subprocess.run(WindowsShellCommand.GROOVE_MUSIC.value, shell=True)

    def open_edge(self):
        subprocess.run(WindowsShellCommand.EDGE.value, shell=True)

    def open_windows_store(self):
        subprocess.run(WindowsShellCommand.STORE.value, shell=True)

    def open_windows_settings(self):
        subprocess.run(WindowsShellCommand.SETTINGS.value, shell=True)

    def open_windows_calendar(self):
        subprocess.run(WindowsShellCommand.CALENDAR.value, shell=True)

    def open_windows_mail(self):
        subprocess.run(WindowsShellCommand.MAIL.value, shell=True)

    def open_windows_photos(self):
        subprocess.run(WindowsShellCommand.PHOTOS.value, shell=True)

    def open_windows_camera(self):
        subprocess.run(WindowsShellCommand.CAMERA.value, shell=True)

    def open_windows_maps(self):
        subprocess.run(WindowsShellCommand.MAPS.value, shell=True)

    def search_on_google(self):
        subprocess.run(WindowsShellCommand.GOOGLE.value + self._search(), shell=True)

    def search_on_youtube(self):
        subprocess.run(WindowsShellCommand.YOUTUBE.value + self._search(), shell=True)

    def ask_bing(self):
        subprocess.run(WindowsShellCommand.BING.value + self._search(), shell=True)

    def get_muslim_prayer_times(self):
        """Get muslim prayer times from Google search"""
        subprocess.run(WindowsShellCommand.PRAYER.value, shell=True)

    def _search(self):
        return colored_input("Enter search query: ").replace(" ", "+")
