from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def new_password():
    # Clear password entry first
    password_entry.delete(0, END)

    # Generate new random password
    password = password_generator()
    
    # Copy new password to user clipboard
    pyperclip.copy(password)

    # Insert new password to our password entry object
    password_entry.insert(0, password)

def password_generator():
    # Values in lists
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C",
    "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
    "T", "U", "V", "W", "X", "Y", "Z" ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # Create lists of letters, numbers and symbols using list comprehension
    password_letters = [random.choice(letters) for _ in range(0, nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(0, nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(0, nr_numbers)]
    
    # Combine 3 lists of random chars to one big list
    password_list = password_letters + password_numbers + password_symbols

    # Shuffle list using random.shuffle()
    random.shuffle(password_list)
    password = ""
    password = password.join(password_list)

    return password

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        # Load in JSON
        with open("Day-30/password-manager-start/data.json", "r") as data_file:
            json_data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title = "error", message = "There is no JSON data file found.")
    else:
        # Get website value
        website_value = website_entry.get()

        # Check if website is in JSON data dictionary
        if website_value in json_data:

            # If website exists, return email and password
            email_value = json_data[website_value]["email"]
            password_value = json_data[website_value]["password"]

            # Check if user is satified with password and email
            is_correct = messagebox.askyesno(title = "Website Info", message = f"These are the details entered: \n\nEmail: {email_value} \nPassword: {password_value}\n\nIs this the correct values?")

            # If use is not satified, allow to overwrite existing email and password
            if not is_correct:
                # Run save() function
                save()
        else:
            # Else, return warning message
            messagebox.showwarning(title = "Warning", message = "Website does not exist in JSON.")

        

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    """This function saves our values from the entry objects to an external file."""

    # Get entry values and store them into variables
    website_value = website_entry.get()
    email_value = email_entry.get()
    password_value = password_entry.get()
    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value,
        }
    }


    # Check if any entries are empty
    if len(website_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showwarning(title = "Warning", message = "Please dont leave any fields empty!")
    else:
        # Message box to check if they want to save the entered info
        is_ok = messagebox.askokcancel(title = website_value, message = f"These are the details entered: \n\n\tEmail: {email_value} \n\tPassword: {password_value} \n\nIs this ok to save?")

        # If user is ok with entered values, run logic
        if is_ok:
            
            # Exception handling for FileNotFoundError:
            try:
                # Write values to an external file
                with open("Day-30/password-manager-start/data.json", "r") as file:
                    # open() is in read permissions:

                    # Load data from JSON
                    data = json.load(file)
                    #print(data) # This is of type 'dictionary'
            except FileNotFoundError:
                print("File was not found, creating JSON now...")
                with open("Day-30/password-manager-start/data.json", "a") as file:
                    # Write to JSON using dump()
                    json.dump(new_data, file, indent = 4)
            else:
                # Update our JSON file with more data
                data.update(new_data)

                with open("Day-30/password-manager-start/data.json", "w") as file:
                    # open() is in write permissions:

                    # Write the updated data back to JSON using dump()
                    json.dump(data, file, indent = 4)
            finally:
                # No matter what, run this block of code

                # Clear existing values from entry objects (keep existing email entry)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


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
website_entry = Entry(width = 21)
website_entry.grid(column = 1, row = 1)
website_entry.focus() # focus cursor on this entry on launch of app

email_entry = Entry(width = 40)
email_entry.grid(column = 1, row = 2, columnspan = 2)
# END => the very last index of the entry label
email_entry.insert(0, "mshabana5656@gmail.com") # we want our email entry to have our most common email already inputted for convenience

password_entry = Entry(width = 21)
password_entry.grid(column = 1, row = 3)

# Buttons
search_button = Button(text = "Search", width = 13, command = find_password)
search_button.grid(column = 2, row = 1)

generate_button = Button(text = "Generate Password", command = new_password)
generate_button.grid(column = 2, row = 3)

add_button = Button(text = "Add", width = 40, command = save)
add_button.grid(column = 1, row = 4, columnspan = 2)


window.mainloop()