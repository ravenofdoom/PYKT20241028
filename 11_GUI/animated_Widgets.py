"""
Quelle: https://www.youtube.com/watch?v=vVRrOi5LGSo
"""

import tkinter as tk

modTheater=0
menue_x=-0.3
blinker=0

def showMenue():
    global menue_x
    if menue_x < 0.01:
        menue_x += 0.01
        frm_Menue.place(relx=menue_x, rely=0.02, relwidth=0.2, relheight=0.86)
        mainW.after(10, showMenue)


def hideMenue():
    frm_indicator.place_forget()
    global menue_x
    menue_x -= 0.01
    frm_Menue.place(relx=menue_x, rely=0.02, relwidth=0.2, relheight=0.86)
    if menue_x > -0.3:
        mainW.after(10, hideMenue)

mainW = tk.Tk()

mainW.geometry("800x600")
mainW.configure(bg="#80dfff")

# create widgets
btn_Menue=tk.Button(mainW, text="Menü einblenden", bg="#0066ff", command=showMenue, activebackground="#6666ff")
frm_Menue=tk.Frame(mainW, background="#6666ff" )

btn_hideMenue=tk.Button(frm_Menue, text="Menü ausblenden", bg="#0066ff", command=hideMenue, activebackground="#6600cc")
frm_indicator=tk.Frame(frm_Menue, background="#6600cc")


# place widgets
btn_Menue.place(relx=0.01, rely=0.9, relwidth=0.2, relheight=0.075)
frm_Menue.place(relx=menue_x, rely=0.02, relwidth=0.2, relheight=0.86)

btn_hideMenue.place(relx=0.2, rely=0.71, relheight=0.2, relwidth=0.75)


mainW.mainloop()