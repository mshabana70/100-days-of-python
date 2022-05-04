from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 40, pady = 20)


# import image as a PhotoImage object 
password_image = PhotoImage(file = "/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-29/password-manager-start/logo.png")

# Create a canvas with width = 200, height = 200
canvas = Canvas(width = 200, height = 200)
canvas.create_image(100, 100, image = password_image)
canvas.grid(column = 1, row = 0)

# Labels
website_label = Label(text = "Website:")
website_label.grid(column = 0, row  = 1)

email_label = Label(text = "Email/Username:")
email_label.grid(column = 0, row  = 2)

password_label = Label(text = "Password:")
password_label.grid(column = 0, row = 3)


# Entries
website_entry = Entry(width = 40)
website_entry.grid(column = 1, row = 1, columnspan = 2)
website_entry.focus() # focus cursor on this entry on launch of app

email_entry = Entry(width = 40)
email_entry.grid(column = 1, row = 2, columnspan = 2)

# END => the very last index of the entry label
email_entry.insert(0, "mshabana5656@gmail.com") # we want our email entry to have our most common email already inputted for convenience

password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

# Buttons
generate_button = Button(text = "Generate Password")
generate_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width = 40)
add_button.grid(column = 1, row = 4, columnspan = 2)





window.mainloop()