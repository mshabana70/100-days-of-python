##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import smtplib
import datetime as dt
import random


# read csv from birthdays.csv
birthdays = pd.read_csv("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-32/automated-birthday-wisher/birthdays.csv")
birthday_dict = birthdays.to_dict(orient="records")

print(birthday_dict)

# Check todays date
today_date = dt.datetime.now()
today_month = today_date.month
today_day = today_date.day



# Set credentials for email
MY_EMAIL = "moonshabana70@gmail.com"
PASSWORD = "test123forprogram"

for i in range(len(birthday_dict)):

    # Check if today matches anyones birthday month and day
    if birthday_dict[i]["month"] == today_month and birthday_dict[i]["day"] == today_day:
        to_email = birthday_dict[i]["email"]
        to_name = birthday_dict[i]["name"].capitalize()

        # Get contents of random letter
        random_num = random.randint(1, 3)
        with open(f"/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-32/automated-birthday-wisher/letter_templates/letter_{random_num}.txt", "r") as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace("[NAME]", to_name)
            print(new_letter)

        # Send new letter to birthday email
        with smtplib.SMTP("smtp.gmail.com", port= 587) as connection:
            connection.starttls()
            connection.login(user= MY_EMAIL, password= PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL, 
                to_addrs= to_email, 
                msg=f"Subject: Happy Birthday {to_name}!\n\n{new_letter}")

        