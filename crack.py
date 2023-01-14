from tkinter import *
from tkterminal import Terminal
import os

root = Tk()

list = [

    "Windows xp",
    "Windows vista",
    "Windows 7",
    "Windows 8",
    "Windows 8.1",
    "Windows 10",
    "Windows 11"

]
listbox = Listbox(root, width=100)

for i in list:
    listbox.insert("end",i)

listbox.grid(row=0, column=0)

terminal = Terminal(bg="black", fg="green", width=100)
terminal.grid(row=1, column=0)

def select_item():
    for i in listbox.curselection():

        if i == 0:
            pass

        if i == 1:
            pass

        if i == 2:
            pass

        if i == 3:
            pass

        if i == 4:
            os.system("slmgr.vbs /ipk BB6NG-PQ82V-VRDPW-8XVD2-V8P66")
            os.system("slmgr.vbs /skms kms.lotro.cc")
            os.system("slmgr.vbs /ato")

button = Button(text="select", command = select_item)
button.grid(row=2, column=0)

root.mainloop()
