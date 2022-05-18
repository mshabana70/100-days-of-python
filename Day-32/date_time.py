# Testing the datetime module
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() # returns an int
print(day_of_week)

date_of_birth = dt.datetime(year = 1998, month = 7, day = 14, hour = 6)
print(date_of_birth)