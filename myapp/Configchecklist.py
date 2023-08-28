from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App
import sqlite3


class Configchecklist(BoxLayout):
    #print("initiated")
    checkboxlist=[]
    addedboxes=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(kwargs)
        self.load_list_of_edible_mushrooms()
        self.orientation="vertical"
        for item in self.checkboxlist:
            boxinbox=BoxLayout(cols=2)
            label=Button(text=item["text"])
            checkbox = CheckBox(height=30,active=item["active"])
            checkbox.size_hint_x=0.2
            checkbox.text = item["text"]
            self.addedboxes.append(checkbox)
            checkbox.on_release=self.save_state_of_checkbox(checkbox)
            boxinbox.add_widget(label)
            boxinbox.add_widget(checkbox)
            self.add_widget(boxinbox)

    def load_list_of_edible_mushrooms(self):
        connection=sqlite3.connect("localDB.db")
        cur=connection.cursor()
        sql_statement = "SELECT * FROM edible"
        fetching = cur.execute(sql_statement)
        edible = cur.fetchall()
        #print(edible)
        result=[]
        for i in edible:
            result.append({"active":False,"text":i[1]})
        self.checkboxlist=result
    def save_state_of_checkbox(self,*args):
        #print("func called")
        #print(self.addedboxes)
        configlist=[]
        for box in self.addedboxes:
            if box.active==True:
                configlist.append(box.text)
        app = App.get_running_app()
        app.reportconfig=configlist
        #print(configlist)
        return self.save_state_of_checkbox
    