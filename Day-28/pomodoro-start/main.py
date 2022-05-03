from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60


    if (reps % 8 == 0):
        # If its the 8th rep:
        count_down(long_break_seconds)
        header_label.config(text = "Long Break!", fg = RED)
    elif (reps % 2 == 0):
        # If its the 2nd/4th/6th:
        count_down(short_break_seconds)
        header_label.config(text = "Break!", fg = PINK)
    else:
        # If its the 1st/3rd/5th/7th rep:
        count_down(work_seconds)
        header_label.config(text = "Work")
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #print(count)

    # Format our count to display like traditional time
    minutes = math.floor(count / 60)
    seconds = count % 60

    # Dynamic typing
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"

    # decrement our timer_text as we count down every second
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer() # call start timer again

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# Create Canvas widget so we can layer components on one another
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0) # canvas roughly the size of our tomato image

# .create_image() only takes a PhotoImage type for the image we want to display
tomato_img = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-28/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = tomato_img) # x = 103, y = 112 to put the image in the center of the canvas
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold")) # place text on top of our tomato image
canvas.grid(column = 1, row = 1)

# Labels
header_label = Label(text = "Timer", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 50, "normal"))
header_label.grid(column = 1, row = 0)

checkmark_label = Label(text = "✓", bg = YELLOW, fg = GREEN, font = (FONT_NAME, 25, "normal"))
checkmark_label.grid(column = 1, row = 3)

# Buttons
start_button = Button(text = "Start", command = start_timer, bg = RED)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", bg = RED)
reset_button.grid(column = 2, row = 2)


window.mainloop()
