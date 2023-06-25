from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test")
root.geometry("500x200+400+200")

root.update_idletasks()

label = Label(text="G69dwine")
label.pack()

obj1 = Canvas()
obj1.pack()
root.mainloop()