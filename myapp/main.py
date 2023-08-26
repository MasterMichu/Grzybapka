from kivymd.app import MDApp
from MushroomMapview import MushroomMapview
from kivy.uix.screenmanager import ScreenManager,Screen
from FilterChoice import FilterChoice
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
    filterconfig=None
    reportconfig=None
    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainwindow(name='main'))
        sm.add_widget(FilterChoice(name='filter'))
        sm.add_widget(Configure(name='configure'))
        sm.add_widget(RecordMushrooms(name='record'))
        sm.add_widget(Publish(name='publish'))
        return sm
        
    pass
mainappinstance=MainApp()
mainappinstance.run()