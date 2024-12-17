import tkinter as tk
from tkinter import ttk
import sqlite3

""" db_path="Pfad zur Datenbank"
db_conn=sqlite3.connect(db_path)
db_namen=db_conn.cursor()
db_namen.execute('select Kontakte.Vorname, Kontakte.Nachname from Kontakte;')
data_namen=db_namen.fetchall() """

# create window

mainwindow = tk.Tk()
mainwindow.geometry('800x600')
mainwindow.minsize(300, 450)
mainwindow.maxsize(1000, 750)
mainwindow.title('Meine GUI')

# create widgets

l_upperfrm=tk.Frame(master=mainwindow, height=300, width=200, bg="#ffdf80")
l_lowerfrm=tk.Frame(master=mainwindow, height=300, width=200, bg="#ffc6b3")
r_frm=tk.Frame(master=mainwindow, height=600, width=600, bg="#cce6ff")
contact_listbox=tk.Listbox(l_upperfrm, font=("Arial, 15"))
btn_new=tk.Button(master=l_upperfrm, text='Neuer Kontakt')
chbx_work=tk.Checkbutton(master=l_lowerfrm, text='Beruflich', bg="#ffc6b3")
ckbx_home=tk.Checkbutton(master=l_lowerfrm, text='Privat', bg="#ffc6b3")
chbx_love=tk.Checkbutton(master=l_lowerfrm, text='Intim', bg="#ffc6b3")

# create layout

l_upperfrm.place(relx=0, rely=0, relwidth=0.35, relheight=0.8)
l_lowerfrm.place(relx=0, rely=0.8, relwidth=0.35, relheight=0.2)
r_frm.place(relx=0.35, rely=0, relwidth=0.65, relheight=1)
contact_listbox.place(relx=0.02, rely=0.02, relwidth=0.95, relheight=0.85)
btn_new.place(relx=0.02, rely=0.89)
chbx_work.pack(pady=5, anchor='w')
ckbx_home.pack(pady=5, anchor='w')
chbx_love.pack(pady=5, anchor='w')

# create content

""" for x in data_namen:
    contact_listbox.insert("end",x) """

""" contact_listbox.pack(side='left')
btn_ok.pack(side='bottom', anchor='center' ) """

# run
mainwindow.mainloop()