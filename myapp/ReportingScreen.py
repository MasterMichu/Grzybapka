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
                button=Button(text=mushroom,size_hint=(0.33,0.33))
                self.added_widgets.append(button)
                self.add_widget(button)
        
    