import customtkinter as ctk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('crud.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT, 
    age INTEGER
)''')
conn.commit()

root = ctk.CTk()
root.geometry("400x300")

def clear_entries():
    entryi.delete(0, ctk.END)
    entryn.delete(0, ctk.END)
    entrya.delete(0, ctk.END)

def search_user():
    id=entryi.get()
    clear_entries()
    if id:
        c.execute("SELECT * FROM users WHERE id=?",(id))
        user=c.fetchone()
        if user:
            entryi.insert(0, id)  # Re-insert the ID
            entryn.insert(0, user[1])
            entrya.insert(0, user[2])
        else:
            messagebox.showinfo("Not Found", "User not found")
    else:
        messagebox.showwarning("Input Error", "Please enter an ID")

def insert_user():
    name=entryn.get()
    age=entrya.get()
    if name and age:
        c.execute("INSERT INTO users (name,age) VALUES (?,?)",(name,age))
        conn.commit()
        messagebox.showinfo("Success",f"User inserted successfully")
        clear_entries()
    else:
        messagebox.showwarning("Input Error","Please enter all fields")

def update_user():
    id=entryi.get()
    name=entryn.get()
    age=entrya.get()
    if name and age:
        c.execute("UPDATE users SET name=?,age=? WHERE id=?",(name,age,id))
        conn.commit()
        messagebox.showinfo("Success",f"User updated successfully")
        clear_entries()
    else:
        messagebox.showwarning("Input Error","Please enter all fields")

def delete_user():
    id=entryi.get()
    if id:
        c.execute("DELETE FROM users WHERE id=?",(id))
        conn.commit()
        messagebox.showinfo("Success",f"User deleted successfully")
        clear_entries()
    else:
        messagebox.showwarning("Input Error","Please enter an ID")

label=ctk.CTkLabel(root,text="ID")
label.grid(row=0,column=0,padx=10,pady=10)
entryi=ctk.CTkEntry(root)
entryi.grid(row=0,column=1,padx=10,pady=10)

labeln=ctk.CTkLabel(root,text="Name")
labeln.grid(row=1,column=0,padx=10,pady=10)
entryn=ctk.CTkEntry(root)
entryn.grid(row=1,column=1,padx=10,pady=10)

labela=ctk.CTkLabel(root,text="Age")
labela.grid(row=2,column=0,padx=10,pady=10)
entrya=ctk.CTkEntry(root)
entrya.grid(row=2,column=1,padx=10,pady=10)

searchb=ctk.CTkButton(root,text="Search",command=search_user)
searchb.grid(row=3,column=0,padx=10,pady=10)

insertb=ctk.CTkButton(root,text="Insert",command=insert_user)
insertb.grid(row=3,column=1,padx=10,pady=10)

updateb=ctk.CTkButton(root,text="Update",command=update_user)
updateb.grid(row=4,column=0,padx=10,pady=10)

deleteb=ctk.CTkButton(root,text="Delete",command=delete_user)
deleteb.grid(row=4,column=1,padx=10,pady=10)

clearb=ctk.CTkButton(root,text="Clear",command=clear_entries)
clearb.grid(row=5,column=0,padx=10,pady=10)
root.mainloop()