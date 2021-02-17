from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES
text=StringVar
root = Tk()
root.geometry("500x500")
language = list(LANGUAGES.values())
f1 = Frame(root,bg="White")
f1.grid()
a=StringVar()
a.set("  ")
b=StringVar()
b.set(" ")
L1=Label(f1,text="TRANSLATOR")
L1.grid(row=1,column=0)
L2=Label(f1,text="INPUT TEXT")
L2.grid(row=2,column=0)
s1=Entry(f1,textvariable=a)
s1.grid(row=2,column=1,ipadx=100)
L3=Label(f1,text="OUTPUT TEXT")
L3.grid(row=5,column=0)
s2=Entry(f1,textvariable=b)
s2.grid(row=5,column=1,ipadx=100)
select_language= ttk.Combobox(f1, value=language,width=27)
select_language.grid(column=0,row=3)
select_language.set("select")
def translate():
    translator = Translator()
    translated=translator.translate(s1.get(), dest=select_language.get())
    b.set(translated.text)
    s2.update()
b1 = Button(f1, text="TRANSLATE",command=translate)
b1.grid(row=4, column=0)
root.mainloop()