import sqlite3
from datetime import datetime
con = sqlite3.connect ("localDB.db")
curr= con.cursor()
curr.execute("CREATE TABLE MUSHROOMS(id integer primary key autoincrement,author,type,local,public,precision,date,x,y)")
curr.execute("CREATE TABLE EDIBLE(id integer primary key autoincrement,type)")
with open("localDB.csv") as f:
    text=f.read()
    result_text=""
    splitedlines=text.splitlines()
    i=0
    for line in splitedlines:
        words=line.split(",")
        modified_lane=""
        for word in words:
            try: 
                modified_word=datetime.strpdate(word,'%d/%m/%Y')
            except:
                try:
                    modified_word=float(word)
                except:
                    modified_word='"'+word+'"'
            modified_word=str(modified_word)
            modified_lane=modified_lane+modified_word+","
        
        result=str(i)+","+str(modified_lane[:-1])
        result_text=result_text+result
        i=i+1
        executable_string=f"INSERT INTO mushrooms VALUES( {result})"
        curr.execute(executable_string)
        con.commit()
        print(result)


    
    
    EdiblesList=["podgrzybek","zajaczek","prawdziwek","maslak","goryczak","szmaciak","purchawica olbrzymia"]
    i=0
    lines_to_add=""
    for shroomie in EdiblesList:
        lines_to_add=str(i)+','+'"'+shroomie+'"'
        i=i+1
        print(lines_to_add)    
        executable_string=f"INSERT INTO edible VALUES( {str(lines_to_add)})"
        curr.execute(executable_string)
        con.commit()

    


#executable_string=f"INSERT INTO mushrooms VALUES( {result_text[:-2]})"
#curr.execute(executable_string)
#con.commit()