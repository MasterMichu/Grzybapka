from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.app import App
import sqlite3


class MushroomsCheckboxesList(BoxLayout):
<<<<<<< HEAD
    #print("initiated")
=======
    print("initiated")
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
    checkboxlist=[]
    addedboxes=[]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
<<<<<<< HEAD
        #print(kwargs)
=======
        print(kwargs)
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
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
<<<<<<< HEAD
        #print(edible)
=======
        print(edible)
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
        result=[]
        for i in edible:
            result.append({"active":False,"text":i[1]})
        self.checkboxlist=result
    def save_state_of_checkbox(self,*args):
<<<<<<< HEAD
        #print("func called")
        #print(self.addedboxes)
        sqlfilter=""
        for box in self.addedboxes:
            #print(box.text+','+str(box.active))
=======
        print("func called")
        print(self.addedboxes)
        sqlfilter=""
        for box in self.addedboxes:
            print(box.text+','+str(box.active))
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
            if box.active==True:
                if sqlfilter=="":
                    sqlfilter=f" AND (type='{box.text}')"
                else:
                    sqlfilter=sqlfilter[:-1]+f" OR type='{box.text}')"
        app = App.get_running_app()
        app.filterconfig=sqlfilter
<<<<<<< HEAD
        #print(sqlfilter)
=======
        print(sqlfilter)
>>>>>>> 7e3c65269aa46c4798af674dc7edbeb64d20d49c
        return self.save_state_of_checkbox
        

        
    