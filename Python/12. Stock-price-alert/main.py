import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEYS = os.environ.get("STOCK_API_KEYS")
NEW_API_KEYS = os.environ.get("NEW_API_KEYS")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameter = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEYS,
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_down = None
if difference < 0:
    up_down = "🔻"
else:
    up_down = "🔺"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if abs(diff_percent) > 1:
    new_parameter = {
        "q": COMPANY_NAME,
        "apiKey": NEW_API_KEYS,
    }
    news_response = requests.get(url=NEW_ENDPOINT, params=new_parameter)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{STOCK}: {up_down}{difference}%\nHeadline: {article['title']} \nBrief: {article['description']}" for article in three_articles]

    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+160832403232861',
            body=f"{article}",
            to='+917131128697'
        )

        print(message.status)
