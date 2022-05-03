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
window.config(padx = 100, pady = 50, bg = YELLOW)

# Create Canvas widget so we can layer components on one another
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0) # canvas roughly the size of our tomato image

# .create_image() only takes a PhotoImage type for the image we want to display
tomato_img = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = tomato_img) # x = 103, y = 112 to put the image in the center of the canvas
canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold")) # place text on top of our tomato image
canvas.grid(column = 1, row = 1)

# Labels
header_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 50, "normal"))
header_label.grid(column = 1, row = 0)

checkmark_label = Label(text = "✓", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 25, "normal"))
checkmark_label.grid(column = 1, row = 3)

# Buttons
start_button = Button(text = "Start", highlightcolor=YELLOW, highlightthickness=0)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", highlightcolor=YELLOW, highlightthickness=0)
reset_button.grid(column = 2, row = 2)







window.mainloop()
