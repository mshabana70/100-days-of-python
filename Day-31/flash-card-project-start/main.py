from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

# Create Canvas for flash card image
card_canvas = Canvas(width = 800, height = 526)

# Card image (front)
front_card_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/card_front.png")

# Insert card_image to canvas using create image
card_canvas.create_image(400, 250, image = front_card_image)


window.mainloop()
