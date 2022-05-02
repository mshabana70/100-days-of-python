# Day 27 - GUI in Python
#
# https://docs.python.org/3/library/tkinter.html#the-packer

# The library we will use to build a GUI will be TKinter
from tkinter import *

# Similar to the screen object we were creating in turtle
window = Tk()
window.title("My First GUI Program") # give our window a title
window.minsize(width = 500, height = 300)


# Label
my_label = Label(text = "I am a Label", font = ("Arial", 24, "bold"))

# How will that label be displayed on screen?
# The packer is a geometry-management mechanism
#my_label.pack(side = "left") # place it on our window and automatically center it
#my_label.pack()

# We can use place() to be more precise with our layout of objects on screen
my_label["text"] = "New Text" # will change the text property of our label
my_label.config(text="New Text") # does the same thing to the text property
#my_label.place(x = 100, y = 0)
my_label.grid(column = 0, row = 0) # best to start with something you want in the top left

# Button

# Event listener for button
def button_clicked():
    #print("I got clicked!")
    # Challenge: Change label text when button is clicked
    #my_label.config(text = "Button got clicked!")
    text_input = input.get()
    my_label.config(text = text_input)

button = Button(text = "Click Me", command = button_clicked)
#button.pack()
button.grid(column = 1, row = 1)

# Entry

# Text input entry object in tkinter
input = Entry(width = 10)
#input.pack()
input.grid(column = 2, row = 2) # note: you cant mix up grid and pack



window.mainloop() # runs a loop to keep our window on the screen and listen for user action