import tkinter as tk
import sqlite3
import tkinter.messagebox as myMessageBox

conn=sqlite3.connect('college.sqlite3')
cursor=conn.cursor()

def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS student(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   email TEXT,
                   address TEXT)""")
    conn.commit()

create_table()

app=tk.Tk()
app.title('Student Record')
app.geometry('500x500')

nameLebel=tk.Label(app,text='Name:')
nameLebel.grid(row=0,column=0,padx=10,pady=10)
name=tk.Entry(app)
name.grid(row=0,column=1)
emailLebel=tk.Label(app,text='Email:')
emailLebel.grid(row=1,column=0,padx=10,pady=10)
email=tk.Entry(app)
email.grid(row=1,column=1)
addressLebel=tk.Label(app,text='Address:')
addressLebel.grid(row=2,column=0)
address=tk.Entry(app)
address.grid(row=2,column=1)

def insert():
    iname=name.get()
    iemail=email.get()
    iaddress=address.get()
    cursor.execute("""
                INSERT INTO student(name,email,address)
                VALUES(?,?,?)""",(iname,iemail,iaddress))
    conn.commit()
    name.delete(0,tk.END)
    email.delete(0,tk.END)
    address.delete(0,tk.END)
    myMessageBox.showinfo('Success','Record Inserted Successfully')  

button=tk.Button(app,text='Submit',command=insert)
button.grid(row=3,column=1)

app.mainloop()