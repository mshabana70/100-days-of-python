# Day 27 Project - Miles to KM converter with GUI
#
# Create a miles to kilometer converter with a tkinter GUI

from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 150)
window.config(padx = 50, pady = 30)


def miles_to_km(miles):
    return round(int(miles) * 1.61, 2)

def update_label():
    # Get user input of miles
    miles = mile_entry.get()

    # reconfigure label text to equal the return value of miles_to_km
    calculated_label.config(text = miles_to_km(miles))

# Entry for miles
mile_entry = Entry(width = 10)
mile_entry.grid(column = 1, row = 0)

# "Miles" label
my_label_1 = Label(text = "Miles", font = ("Arial", 12, "normal"))
my_label_1.grid(column = 2, row = 0)

# "Is equal to" label
my_label_2 = Label(text = "is equal to", font = ("Arial", 12, "normal"))
my_label_2.grid(column = 0, row = 1)

# Converted miles to km label
calculated_label = Label(text = "0", font = ("Arial", 12, "normal"))
calculated_label.grid(column = 1, row = 1)
calculated_label.config(padx = 0, pady = 10)

# "Km" label
my_label_3 = Label(text = "Km", font = ("Arial", 12, "normal"))
my_label_3.grid(column = 2, row = 1)

# Button to trigger update_label function
calculated_button = Button(text = "Calculate", command = update_label)
calculated_button.grid(column = 1, row = 3)


window.mainloop()