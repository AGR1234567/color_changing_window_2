from tkinter import*
from tkinter.filedialog import*

window=Tk()

list1 = ['red', 'blue', 'green', 'yellow']

def add():
    b=e1.get().strip()
    if b:
        l1.insert(END, b)
        e1.delete(0, END)

def delete():
    b=l1.curselection()
    if a:
        l1.delete(a)

def change_color(event):
    a=l1.curselection()
    if a:
        c=l1.get(a[0])
        window.config(background=c)

e1=Entry(window)
e1.pack(pady=5)
s1=Scrollbar(window, orient='vertical')
l1=Listbox(window, width=70, yscrollcommand=s1.set)
l1.pack(side=BOTTOM)
l1.bind('<<ListboxSelect>>', change_color)
b1=Button(window, text='Change color', width=10, command=change_color)
b1.pack(side=LEFT, padx=5, pady=5)
b2=Button(window, text='Add', width=10, command=add)
b2.pack(side=LEFT, padx=5, pady=5)
b3=Button(window, text='Delete', width=10, command=delete)
b3.pack(side=LEFT, padx=5, pady=5)
for i in list1:
    l1.insert(END, i)


window.mainloop()