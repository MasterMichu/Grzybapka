from kivymd.app import MDApp
from MushroomMapview import MushroomMapview
from kivy.uix.screenmanager import ScreenManager,Screen
import sqlite3

class FilterChoice(Screen):
    pass


class Configure(Screen):
    pass


class RecordMushrooms(Screen):
    pass


class Publish(Screen):
    pass

class Mainwindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass



class MainApp(MDApp):
    connection=None
    cur=None
    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()
        
    pass
mainappinstance=MainApp()
mainappinstance.run()