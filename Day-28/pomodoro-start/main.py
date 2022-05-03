from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50)

# Create Canvas widget so we can layer components on one another
canvas = Canvas(width = 200, height = 224) # canvas roughly the size of our tomato image

# .create_image() only takes a PhotoImage type for the image we want to display
tomato_img = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-28/pomodoro-start/tomato.png")
canvas.create_image(103, 115, image = tomato_img) # x = 103, y = 115 to put the image in the center of the canvas
canvas.pack()







window.mainloop()
