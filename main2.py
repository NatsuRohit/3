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

sIdData=tk.Entry(app)

sIdData.grid(row=0,column=2)
nameLebel=tk.Label(app,text='Name:')
nameLebel.grid(row=0,column=0,padx=10,pady=10)
name=tk.Entry(app)
name.grid(row=0,column=1)
emailLebel=tk.Label(app,text='Email:')
emailLebel.grid(row=1,column=0,padx=10,pady=10)
email=tk.Entry(app)
email.grid(row=1,column=1)
addressLebel=tk.Label(app,text='Address:')
addressLebel.grid(row=2,column=0,padx=10,pady=10)
address=tk.Entry(app)
address.grid(row=2,column=1)

def insert():
    iname=name.get()
    iemail=email.get()
    iaddress=address.get()
    sid=sIdData.get()
    if sid=="":sid=0
    if int(sid)>0:
        cursor.execute("""UPDATE student SET
                       name=?,
                       email=?,
                       address=?
                       WHERE id=?""",
                       (iname,iemail,iaddress,sid))
        conn.commit()
        name.delete(0,tk.END)
        email.delete(0,tk.END)
        address.delete(0,tk.END)
        sIdData.delete(0,tk.END)
        
        show()
        my.MessageBox.showinfo("Success","Record Updated Successfully")

    else:
        cursor.execute("""
                INSERT INTO student(name,email,address)
                VALUES(?,?,?)""",(iname,iemail,iaddress))
    conn.commit()
    name.delete(0,tk.END)
    email.delete(0,tk.END)
    address.delete(0,tk.END)
    show()
    myMessageBox.showinfo('Success','Record Inserted Successfully')

button=tk.Button(app,text='Add Record',command=insert)
button.grid(row=3,column=1)

def delete(id):
    cursor.execute("DELETE FROM student WHERE id=?",(id,))
    conn.commit()

    myMessageBox.showinfo("Success","Record Deleted Successfully")
    show()

def edit(id):
    cursor.execute("SELECT * FROM student WHERE id=?",(id,))
    record=cursor.fetchone()
    sIdData.insert(0,record[0])
    name.insert(0,record[1])
    email.insert(0,record[2])
    address.insert(0,record[3])
    button.config(text="Update Record",command=lambda:insert())

    show()

def show():
    cursor.execute("SELECT * FROM student")
    records=cursor.fetchall()
    tk.Label(app,text="Name").grid(row=5,column=0)
    tk.Label(app,text="Email").grid(row=5,column=1)
    tk.Label(app,text="Address").grid(row=5,column=2)
    tk.Label(app,text="Action").grid(row=5,column=3)

    for i, record in enumerate(records):
        tk.Label(app, text=record[1]).grid(row=i+6, column=0)
        tk.Label(app, text=record[2]).grid(row=i+6, column=1)
        tk.Label(app, text=record[3]).grid(row=i+6, column=2)
        tk.Button(app, text="Edit",command=lambda id_=record[0]:edit(id_)).grid(row=i+6,column=3)
        tk.Button(app, text="Delete", command=lambda id_=record[0]: delete(id_)).grid(row=i+6, column=4)

show()

app.mainloop()