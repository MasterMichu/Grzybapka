from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from ReportingScreen import ReportingScreen
from kivy.app import App
import sqlite3


class RecordMushrooms(Screen):
    def on_enter(self, *args):
        #print(dir(self.ids))
        #print(self.ids)
        self.ids.screentoupdate.refresh()
        #repo_screen=self.ReportingScreen

        return super().on_enter(*args)
    
    pass
