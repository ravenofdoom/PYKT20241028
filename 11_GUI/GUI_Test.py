import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.geometry('800x600')
app.minsize(300, 450)
app.maxsize(1000, 750)
app.title('Meine GUI')
#app.state("zoomed")

frm_Center = tk.Frame(master=app, height=300, width=200, bg="#ffdf80" )
frm_Center.pack(fill='y')

btn_1 = tk.Button(master=frm_Center, text="push")

# Layoutmanager: pack(), grid(), place()
# btn_1.pack(pady=20, fill="y", anchor='center')
# btn_1.grid(row=1, column=2)
#btn_1.place(relx=0.5, rely=0.5, width=100, height=50, anchor='center')

btn_1.pack(padx=20, pady=30, anchor='center')



app.mainloop()