from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.app import App
import sqlite3

class ReportingScreen(StackLayout):
    added_widgets=[]
    try:
        app = App.get_running_app()
        #print(app.root.current)
    except:
        pass
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def refresh(self):
        #print("refreshed")
        app = App.get_running_app()
        #print(app.reportconfig)
        if app.reportconfig==[]:
            app.root.current="configure"
        else:
            for added in self.added_widgets:
                self.remove_widget(added)
            self.added_widgets=[]
            for mushroom in app.reportconfig:
                button=Button(text=mushroom,size_hint=(0.33,0.33),on_release=self.GetCoordinates)
                self.added_widgets.append(button)
                self.add_widget(button)
    
    def GetCoordinates(self,*args,**kwargs):
        for screen in App.get_running_app().root.screens:
            if screen.name=="main":
                gps_blinker=screen.ids.mapview.ids.blinker
                mapa=screen.ids.mapview
        mushroomName=args[0].text
        print(kwargs)
        current_lat=gps_blinker.lat
        current_lon=gps_blinker.lon
        #mushroomName=kwargs["mushroomName"]
        print("current_lat=",current_lat,"current_lon=",current_lon,"mushroom=",mushroomName)
        pass
    def SerializeDataForDB(self,dataDict):
        pass
    def RecordInDB(self):
        pass

    
        
    