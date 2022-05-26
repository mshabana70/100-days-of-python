import requests
import os
import datetime

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY") # replace with custom api key
STOCK_URL = "https://www.alphavantage.co/query"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outsize": "compact",
    "datatype": "json",
    "apikey": STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)

# Raise exception for invalid error codes
stock_response.raise_for_status()

# get json data
stock_data = stock_response.json()

# Get today's & yesterday's date in "YYYY-MM-DD" format
yesterday_date = str(datetime.datetime.now() - datetime.timedelta(days=1)).split(" ")[0]
day_before_date = str(datetime.datetime.now() - datetime.timedelta(days=2)).split(" ")[0]

# Get stock_data for today
yesterday_stock = stock_data["Time Series (Daily)"][yesterday_date]
day_before_stock = stock_data["Time Series (Daily)"][day_before_date]

# Calculate percentage change between yesterday's close price to the day before

percent_change = abs(float(day_before_stock["4. close"]) - float(yesterday_stock["4. close"])) / float(day_before_stock["4. close"])
print(percent_change)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

