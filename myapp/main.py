from kivymd.app import MDApp
from MushroomMapview import MushroomMapview
from kivy.uix.screenmanager import ScreenManager,Screen
from FilterChoice import FilterChoice
from Configure import Configure
from RecordMushrooms import RecordMushrooms
from gpshelper import GpsHelper
from kivy.clock import Clock
import sqlite3

class FilterChoice(Screen):
    pass


class Configure(Screen):
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
    def callback(self,dt):
        pass
    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()
        Clock.schedule_once(self.callback,2)
        GpsHelper().run()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainwindow(name='main'),id="main")
        sm.add_widget(FilterChoice(name='filter'))
        sm.add_widget(Configure(name='configure'))
        sm.add_widget(RecordMushrooms(name='record'))
        sm.add_widget(Publish(name='publish'))
        return sm
        
    pass
mainappinstance=MainApp()
mainappinstance.run()
#print(mainappinstance.root.current)