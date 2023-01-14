from tkinter import *
from tkterminal import Terminal

root = Tk()

list = [

    "Windows xp",
    "Windows vista",
    "Windows 7",
    "Windows 8",
    "Windows 8.1 Single Language",
    "Windows 10",
    "Windows 11"

]

list2 = [

    "",
    "",
    "",
    "",
    "BB6NG-PQ82V-VRDPW-8XVD2-V8P66",
    "",
    ""
]
listbox = Listbox(root, width=100)

for i in list:
    listbox.insert("end",i)

listbox.grid(row=0, column=0)

terminal = Terminal(bg="black", fg="green", font="font-source-sans-pro", width=100)
terminal.shell = True
terminal.grid(row=1, column=0)

def select_item():
    for i in listbox.curselection():

        terminal.run_command("slmgr.vbs /ipk {}".format(list2[i]))
        terminal.run_command("slmgr.vbs /skms kms.lotro.cc")
        terminal.run_command("slmgr.vbs /ato")

button = Button(text="select", command=select_item)
button.grid(row=2, column=0)

root.mainloop()
