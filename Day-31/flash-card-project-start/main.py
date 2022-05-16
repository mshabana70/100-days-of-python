from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)



# Card image (front)
front_card_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/card_front.png")
wrong_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/wrong.png")
right_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/right.png")

# Create Canvas for flash card image
card_canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness= 0)

# Insert card_image to canvas using create image
card_canvas.create_image(400, 265, image = front_card_image)

# Insert text on our card canvas
untranslated_text = card_canvas.create_text(400, 150, text = "French", fill = "black", font = ("Ariel", 40, "italic"))
translated_text = card_canvas.create_text(400, 263, text = "trouve", fill = "black", font = ("Ariel", 60, "bold"))

card_canvas.grid(column = 0, row = 0, columnspan=2)


# Create button for wrong image
wrong_button = Button(image = wrong_image, highlightcolor = BACKGROUND_COLOR, highlightthickness = 0)
wrong_button.grid(column = 0, row = 1)

# Create button for wrong image
right_button = Button(image = right_image, highlightcolor = BACKGROUND_COLOR, highlightthickness = 0)
right_button.grid(column = 1, row = 1)



window.mainloop()
