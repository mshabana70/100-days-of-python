from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(bg = BACKGROUND_COLOR)

# Create Canvas for flash card image

# Card image (front)
front_card_image = PhotoImage(file = "images/card_front.png")


window.mainloop()
