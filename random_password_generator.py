import random
import paperclip
from tkinter import *
from tkinter.ttk import *

def low():
    entry.delete(0,END)
    length=var1.get()
    lower="abcdefghijklmnopqrstuvwxyz"
    upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()"
    password=""

    if var.get()==1:
        for i in range(0,length):
            password=password+random.choice(lower)
        return password
    elif var.get()==0:
        for i in range(0,length):
            password=password+random.choice(upper)
        return password
    elif var.get()==3:
        for i in range(0,length):
            password=password+random.choice(digits)
        return password
    else:
        print("Invalid choice")
def generate():
    password1=low()
    entry.insert(10,password1)
def copy1():
    random_password=entry.get()
    paperclip.copy(random_password)
root=Tk()
var=IntVar()
var1=IntVar()
root.title("Random Password Generator")

rp=Label(root,text="password")
rp.grid(row=0)
entry=Entry(root)
entry.grid(row=0,column=1)

c_label=Label(root,text="length")
c_label.grid(row=1)

cb=Button(root,text="copy",command=copy1)
cb.grid(row=0,column=2)
generate_b=Button(root,text="Generate",command=generate)
generate_b.grid(row=0,column=3)

radio_low=Radiobutton(root,text="low",variable=var,value=1)
radio_low.grid(row=1,column=2,sticky='E')
radio_medium=Radiobutton(root,text="medium",variable=var,value=0)
radio_medium.grid(row=1,column=3,sticky='E')
radio_strong=Radiobutton(root,text="strong",variable=var,value=3)
radio_strong.grid(row=1,column=4,sticky='E')
combo=Combobox(root,textvariable=var1)

combo['values']=(8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,"length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.grid(column=1,row=1)

root.mainloop()
