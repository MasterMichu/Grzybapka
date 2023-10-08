from kivymd.app import MDApp
from MushroomMapview import MushroomMapview
from kivy.uix.screenmanager import ScreenManager,Screen
from FilterChoice import FilterChoice
<<<<<<< HEAD
from Configure import Configure
from RecordMushrooms import RecordMushrooms
from gpshelper import GpsHelper
from kivy.clock import Clock
from Permissions_request import Request_permissions_function
import sqlite3


=======
import sqlite3

>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
class FilterChoice(Screen):
    pass


class Configure(Screen):
    pass


<<<<<<< HEAD
=======
class RecordMushrooms(Screen):
    pass
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c


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
<<<<<<< HEAD
    ALLPERMS_GRANTED=False
    FirstLoop=True
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #while True:
            #self.ALLPERMS_GRANTED=Request_permissions_function()
            #if self.ALLPERMS_GRANTED:
            #    break
            #Clock.schedule_once(self.callback,5000)


    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()
        GpsHelper().run()

    def build(self):
        sm = ScreenManager()
        #while True:
        #    self.ALLPERMS_GRANTED=Request_permissions_function()
        #    Clock.schedule_once(self.callback,5)
        #    if self.ALLPERMS_GRANTED:
        #        break
        sm.add_widget(Mainwindow(name='main'),id="main")
=======
    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Mainwindow(name='main'))
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
        sm.add_widget(FilterChoice(name='filter'))
        sm.add_widget(Configure(name='configure'))
        sm.add_widget(RecordMushrooms(name='record'))
        sm.add_widget(Publish(name='publish'))
        return sm
        
    pass
mainappinstance=MainApp()
<<<<<<< HEAD

mainappinstance.run()
#print(mainappinstance.root.current)
=======
mainappinstance.run()
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
