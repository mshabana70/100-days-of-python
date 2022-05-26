import requests
import os
import datetime
from twilio.rest import Client

# STOCKS CONSTANTS
STOCK = "TSLA"
COMPANY_NAME = "Tesla"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY") # replace with custom api key
STOCK_URL = "https://www.alphavantage.co/query"

# NEWS CONSTANTS
NEWS_API_KEY = os.environ.get("NEWS_API_KEY") # replace with custom api key
NEWS_URL = "https://newsapi.org/v2/everything" # every article

# TWILIO CONSTANTS
TWILIO_ACCOUNT_SID = "AC6b18ea2b02ea95a18ea6b6526b1cae5f"
TWILIO_AUTH_KEY = os.environ.get("TWILIO_AUTH_KEY")

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
yesterday_price = float(yesterday_stock["4. close"])
day_before_price = float(day_before_stock["4. close"])
percent_change = round((yesterday_price - day_before_price) / yesterday_price, 2) # using round() for testing
percent_change *= 100 # convert to ones place
up_down = None
if percent_change > 0:
    up_down = "🔺"
elif percent_change < 0:
    up_down = "🔻"

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_paramters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

news_response = requests.get(url=NEWS_URL, params=news_paramters)

# Raise exception for invalid response codes
news_response.raise_for_status()

# Get top 3 news headlines regarding or company's stock
news_data = news_response.json()
top_news_stories = news_data["articles"][:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
for i in range(len(top_news_stories)):
    article_headline = top_news_stories[i]["title"]
    article_description = top_news_stories[i]["description"]
    article_url = top_news_stories[i]["url"]

    if (percent_change >= 5) or (percent_change <= -5):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_KEY)
        message = client.messages \
                    .create(
                        body=f"{STOCK}: {up_down}{percent_change}%\n\nHeadline: {article_headline}\n\nBrief: {article_description}\n\nRead More: {article_url}",
                        from_="+12058582732",
                        to="+16464278840"
                    )
    # Make sure the message was sent successfully
    print(message.status)


