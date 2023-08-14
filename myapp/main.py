from kivymd.app import MDApp
from MushroomMapview import MushroomMapview
import sqlite3


class MainApp(MDApp):
    connection=None
    cur=None
    def on_start(self):
        self.connection=sqlite3.connect("localDB.db")
        self.cur=self.connection.cursor()
        
    pass
mainappinstance=MainApp()
mainappinstance.run()