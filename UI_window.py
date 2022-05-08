from tkinter import *
import sqlite3
import os
from  tkinter import ttk

if os.path.exists('Bank.db'):
    connection = sqlite3.connect("Bank.db")
    cursor = connection.cursor()
else:
    # code idea gotten from https://www.adamsmith.haus/python/answers/how-to-execute-an-external-sql-file-using-sqlite3-in-python
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
    try:
        query_entered = inputbox.get()
        cursor.execute(query_entered)
        connection.commit()
        des = [tuple[0] for tuple in cursor.description]
        results = cursor.fetchall()

        # code idea gotten from https://pythonguides.com/python-tkinter-table-tutorial/ 
        table_frame = result
        table_frame.pack()
        table_frame.place(x=10, y=120)
        query_table = ttk.Treeview(table_frame)
        query_table.pack()
    
        # output any query into output box
        query_table['columns'] = des
        query_table.column("#0", width=0,  stretch=NO)
        width = 20
        height = 150

        # add columns to table and define width
        # for every new column make window bigger
        for head in des:
            query_table.column(head,anchor=CENTER, width=100)
            width += 100

        # change the size of the window
        testwindow.geometry(f'{width}x{height}')

        # put columns name at teh top
        query_table.heading("#0",text="",anchor=CENTER)
        for head in des:
            query_table.heading(head,text=head,anchor=CENTER)
    
        # insert query into the table
        for x in range(len(results)):
            query_table.insert(parent='',index='end', iid=x, text='', values=results[x])
            height += 50

        # change the window size so it fit the query
        testwindow.geometry(f'{width}x{height}')

        # old code
        #cursor.execute(query_entered)
        #des = [tuple[0] for tuple in cursor.description]
        #output = cursor.fetchall()
        #result.insert(END, des)
        #result.insert(END, '\n')
        #for out in output:
        #    result.insert(END, out)
        #    result.insert(END, '\n')
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
