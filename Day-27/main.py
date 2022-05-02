# Day 27 - GUI in Python
#
# https://docs.python.org/3/library/tkinter.html#the-packer

# The library we will use to build a GUI will be TKinter
import tkinter

# Similar to the screen object we were creating in turtle
window = tkinter.Tk()
window.title("My First GUI Program") # give our window a title
window.minsize(width = 500, height = 300)


# Label
my_label = tkinter.Label(text = "I am a Label", font = ("Arial", 24, "bold"))

# How will that label be displayed on screen?
# The packer is a geometry-management mechanism
my_label.pack(side = "left") # place it on our window and automatically center it

my_label["text"] = "New Text" # will change the text property of our label
my_label.config(text="New Text") # does the same thing to the text property







window.mainloop() # runs a loop to keep our window on the screen and listen for user action