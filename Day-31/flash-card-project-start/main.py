from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

####################### READ DATA FROM CSV ######################
word_data = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/data/french_words.csv")
list_of_words = []
list_of_words = word_data.to_dict('records')
current_card = {}

####################### DISPLAY WORDS FROM DATA ######################
def next_card():
    global current_card
    current_card = random.choice(list_of_words)
    card_canvas.itemconfig(title_text, text = "French")
    card_canvas.itemconfig(word_text, text = word["French"])

def flip_card():
    # Change image of card
    card_canvas.itemconfig(card_image, image = back_card_image)
    # Change text
    card_canvas.itemconfig(title_text, fill = "white", text = "English")
    card_canvas.itemconfig(word_text, fill = "white", text = current_card["English"])


window = Tk()
window.title("Flash Card App")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
window.after(3000, func = flip_card)


# Card image (front)
front_card_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/card_front.png")
back_card_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/card_back.png")
wrong_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/wrong.png")
right_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-31/flash-card-project-start/images/right.png")

# Create Canvas for flash card image
card_canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR, highlightthickness= 0)

# Insert card_image to canvas using create image
card_image = card_canvas.create_image(400, 265, image = front_card_image)

# Insert text on our card canvas
title_text = card_canvas.create_text(400, 150, text = "French", fill = "black", font = ("Ariel", 40, "italic"))
word_text = card_canvas.create_text(400, 263, text = "trouve", fill = "black", font = ("Ariel", 60, "bold"))

card_canvas.grid(column = 0, row = 0, columnspan=2)


# Create button for wrong image
wrong_button = Button(image = wrong_image, command = next_card, highlightthickness = 0)
wrong_button.grid(column = 0, row = 1)

# Create button for wrong image
right_button = Button(image = right_image, command = next_card, highlightthickness = 0)
right_button.grid(column = 1, row = 1)


window.mainloop()
