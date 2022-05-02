from tkinter import *


window = Tk()
window.title("Layout Challenge")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20) # padding around 


my_label = Label(text = "New Text", font = ("Arial", 24, "bold"))
my_label.grid(column = 0, row = 0)
my_label.config(padx = 20, pady = 20) # padding around the label only

my_button_1 = Button(text = "Button One")
my_button_1.grid(column = 1, row = 1)

my_button_2 = Button(text = "Button Two")
my_button_2.grid(column = 2, row = 0)

my_entry = Entry(width = 10)
my_entry.insert(END, string = "Text Input")
my_entry.grid(column = 3, row = 2)



window.mainloop()