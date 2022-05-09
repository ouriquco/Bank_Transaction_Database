from tkinter import *
from  tkinter import ttk
import sqlite3
import os


# see if Bank.db exist, create it if not
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


# create the window to display stuff
window = Tk()
window.title("Bank management")
window.geometry("600x300")

# function to close the window
def close():
    window.destroy()

# method to clear the query output box
def clear():
    ## failed code
    ## query_table.delete(*query_table.get_children())
    ## for item in query_table.get_children():
    ##     query_table.delete(item)
    for widget in result.winfo_children():
        widget.destroy()

# fucntion to query stuff
def querystuff():
    try:
        query_entered = inputbox.get()
        cursor.execute(query_entered)
        connection.commit()
        #result.delete(1.0, END)
        des = [tuple[0] for tuple in cursor.description]
        results = cursor.fetchall()

        # code idea gotten from https://pythonguides.com/python-tkinter-table-tutorial/ 
        ## table_frame = result
        ## table_frame.pack()
        ## result.place(x=10, y=120)
        query_table = ttk.Treeview(result)
        query_table.pack()
    
        # output any query into output box
        query_table['columns'] = des
        query_table.column("#0", width=0,  stretch=NO)
        width = 20
        height = 150

        # add a change width for every item in des 
        for head in des:
            query_table.column(head,anchor=CENTER, width=100)
            width += 100

        # put columns name at the top
        query_table.heading("#0",text="",anchor=CENTER)
        for head in des:
            query_table.heading(head,text=head,anchor=CENTER)
    
        # insert query into the table
        for x in range(len(results)):
            query_table.insert(parent='',index='end', iid=x, text='', values=results[x])
            height += 50

        # change the window size so it fit the query
        window.geometry(f'{width}x{height}')

        ## old code
        ##cursor.execute(query_entered)
        ##des = [tuple[0] for tuple in cursor.description]
        ##output = cursor.fetchall()
        ##result.insert(END, des)
        ##result.insert(END, '\n')
        ##for out in output:
        ##    result.insert(END, out)
        ##    result.insert(END, '\n')
    except:
        notquery = Label(result, text="not a query").pack()
    
    
# button to close the window
closebtn = Button(window, text = 'close', command=exit)
closebtn.place(x=10, y=10)

# text to prompt query input
prompt = Label(window, text="enter something:")
prompt.place(x=10, y=40)

# button to clear the query output box
clearbtn = Button(window, text = 'clear query', command=clear)
clearbtn.place(x=150, y=10)

# place to enter query input
inputbox = Entry(window, width=50)
inputbox.place(x=10, y=70)

# submit button to start query
submit = Button(window, text = 'submit', command = querystuff)
submit.place(x=500, y=68)

# text tellng where the results will be
resultlocation = Label(window, text="results here:")
resultlocation.place(x=10, y=100)

# frame to display the query
result = Frame(window, width=150, height=20)
result.place(x=10, y=120)

# run function
window.mainloop()
