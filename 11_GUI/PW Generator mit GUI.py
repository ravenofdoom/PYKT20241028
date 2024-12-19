import tkinter as tk
import random

def pwCreatorSimple(pwLength:int)->str:
    import string
    pwPool=string.hexdigits + string.punctuation
    return "".join(random.sample(pwPool, pwLength))

def pwCreatorPro1(lows:int, caps:int, nums:int, specs:int=0)->str:
    import string
    lowLetters=random.sample(string.ascii_lowercase, lows)
    capLetters=random.sample(string.ascii_uppercase, caps)
    numbers=random.sample(string.digits, nums)
    specChar=random.sample(string.punctuation, specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    random.shuffle(pw)
    return "".join(pw)

root=tk.Tk()

radioVar=tk.StringVar(value="simple")  # Set default value to "simple"
chooseGen=False  # SimpleGen when False

root.title('Passwortgenerator')
root.geometry('400x400')

def chooseSimple():
        global chooseGen
        chooseGen=False
        print("Simple generator selected")
        lblLows.place_forget()
        lblCaps.place_forget()
        lblNums.place_forget()
        lblSpecs.place_forget()
        inLows.place_forget()
        inCaps.place_forget()
        inNums.place_forget()
        inSpecs.place_forget()
        lblGenSimple.place(relx=0.15, rely=0.3)
        inGenSimple.place(relx=0.45, rely=0.3)

def choosePro():
        global chooseGen
        chooseGen=True
        print("Pro generator selected")
        lblGenSimple.place_forget()
        inGenSimple.place_forget()
        lblLows.place(relx=0.1, rely=0.15)
        inLows.place(relx=0.6, rely=0.15)
        lblCaps.place(relx=0.1, rely=0.25)
        inCaps.place(relx=0.6, rely=0.25)
        lblNums.place(relx=0.1, rely=0.35)
        inNums.place(relx=0.6, rely=0.35)
        lblSpecs.place(relx=0.1, rely=0.45)
        inSpecs.place(relx=0.6, rely=0.45)

def chooseAction():  
    if chooseGen:
        lblPassword.configure(text=pwCreatorPro1(int(inLows.get()) if inLows.get() else 0, 
                                                 int(inCaps.get()) if inCaps.get() else 0,
                                                 int(inNums.get()) if inNums.get() else 0, 
                                                 int(inSpecs.get()) if inSpecs.get() else 0))  
    if not chooseGen and inGenSimple.get()!="":
        lblPassword.configure(text=pwCreatorSimple(int(inGenSimple.get())))

def copyClipboard():
     lblPassword.clipboard_clear()
     lblPassword.clipboard_append(lblPassword.cget('text'))

radGenSimple=tk.Radiobutton(root, text="Einfacher Generator", variable=radioVar, value="simple", command=chooseSimple)
radGenSimple.place(relx=0.1, rely=0.05)

radGenPro=tk.Radiobutton(root, text="Parametrierter Generator", variable=radioVar, value="pro", command=choosePro)
radGenPro.place(relx=0.5, rely=0.05)

lblGenSimple=tk.Label(root, bg='RED', text='Anzahl Zeichen:', font=('Helvetica', 10))
inGenSimple =tk.Entry(root)

lblLows=tk.Label(root, bg='RED', text='Anzahl Kleinbuchstaben:', font=('Helvetica', 10))
inLows =tk.Entry(root)

lblCaps=tk.Label(root, bg='RED', text='Anzahl Großbuchstaben:', font=('Helvetica', 10))
inCaps =tk.Entry(root)

lblNums=tk.Label(root, bg='RED', text='Anzahl Zahlen:', font=('Helvetica', 10))
inNums =tk.Entry(root)

lblSpecs=tk.Label(root, bg='RED', text='Anzahl Sondereichen:', font=('Helvetica', 10))
inSpecs =tk.Entry(root)

btnGen=tk.Button(root, text="Generieren", command=chooseAction)
btnGen.place(relx=0.05, rely=0.6, relwidth=0.4)

btnGenCopy=tk.Button(root, text="Copy to Clipboard", command=copyClipboard)
btnGenCopy.place(relx=0.55, rely=0.6, relwidth=0.4)

lblPassword=tk.Label(root, bg='RED', text="Passwort",font=('Helvetica', 25))
lblPassword.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.2)

# Call chooseSimple to set the initial state
chooseSimple()

root.mainloop()