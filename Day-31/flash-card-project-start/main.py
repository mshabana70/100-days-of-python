from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(bg = BACKGROUND_COLOR)

# Create Canvas for flash card image
card_canvas = Canvas(width = 800, height = 526)
card_canvas.config(padx = 50, pady = 50)

# Card image (front)
front_card_image = PhotoImage(file = "images/card_front.png")

# Insert card_image to canvas
card_canvas.create_image(400, 250, image = front_card_image)


window.mainloop()
