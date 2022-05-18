# import smtplib

# my_email = "moonshabana70@gmail.com"
# password = "test123forprogram"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls() # Start transport layer security (encrypts email in transit)
#     connection.login(user=my_email, password= password)
#     connection.sendmail(
#         from_addr= my_email,
#         to_addrs= "moonshabana70@yahoo.com", 
#         msg= "Subject:Hello World!\n\nThis is the body of my email."
#     )


# Challenge # 1: create a motivation quote application
# that sends an email with a motivational quote every monday
# (test with the current day of the week)

import datetime as dt
import smtplib
import random

# Lets get a list of our quotes first
with open("/Users/mahmoudshabana/Documents/Udemy/100-days-of-python/Day-32/quotes.txt", "r") as quote_file:
    quote_list = quote_file.readlines()
    # Pick a random quote
    random_quote = random.choice(quote_list)

# Send random quote when it is monday (we will test with today)
current_date = dt.datetime.now()
day_of_week = current_date.weekday()

# Set our email and password
MY_EMAIL = "moonshabana70@gmail.com"
PASSWORD = "test123forprogram"

# 0 => monday
if (day_of_week == 2):
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password = PASSWORD)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mshabana5656@gmail.com", 
            msg=f"Subject:Weekly Motivation from Python\n\n{random_quote}."
        )
