from tkinter import *
import sqlite3
import os

if os.path.exists('Bank.db') == False:
    # https://www.adamsmith.haus/python/answers/how-to-execute-an-external-sql-file-using-sqlite3-in-python
    connection = sqlite3.connect("Bank.db")
    cursor = connection.cursor()
    sql_file = open("DB_Code.sql")
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)


# create windows
testwindow = Tk()
testwindow.title("Bank management")
testwindow.geometry("600x300")

# functions
def close():
    testwindow.destroy()

def querystuff():
    query_entered = inputbox.get()
    result.delete(0.0, END)

    try:
        cursor.execute(query_entered)
        des = [tuple[0] for tuple in cursor.description]
        output = cursor.fetchall()
        result.insert(END, des)
        result.insert(END, '\n')
        for out in output:
            result.insert(END, out)
            result.insert(END, '\n')
    except:
        result.insert(END, 'not a query')
    
    
# stuff on window
closebtn = Button(testwindow, text = 'close', command=exit)
closebtn.place(x=10, y=10)

prompt = Label(testwindow, text="enter something:")
prompt.place(x=10, y=40)

inputbox = Entry(testwindow, width=50)
inputbox.place(x=10, y=70)

submit = Button(testwindow, text = 'submit', command = querystuff)
submit.place(x=315, y=68)

resultlocation = Label(testwindow, text="results here:")
resultlocation.place(x=10, y=100)

result = Text(testwindow, width=50, height=20)
result.place(x=10, y=120)

# run function
testwindow.mainloop()