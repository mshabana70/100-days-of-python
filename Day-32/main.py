import smtplib

my_email = "moonshabana70@gmail.com"
password = "test123forprogram"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() # Start transport layer security (encrypts email in transit)
    connection.login(user=my_email, password= password)
    connection.sendmail(
        from_addr= my_email,
        to_addrs= "moonshabana70@yahoo.com", 
        msg= "Subject:Hello World!\n\nThis is the body of my email."
    )
    