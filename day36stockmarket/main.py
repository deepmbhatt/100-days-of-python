import requests

from twilio.rest import Client

account_sid = 'YOUR ACCOUNT SID'
auth_token = 'Your AUTH TOKEN'
client = Client(account_sid, auth_token)


stock = "Reliance.BSE"
company_name = "Reliance Industries Limited Ltd"
stock_api = "YOUR STOCK API"
news_api = "YOUR NEWS API"
stock_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock}&outputsize=compact&apikey={stock_api}"
response = requests.get(stock_url)
response.raise_for_status()
stock_data = response.json()

news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q": company_name,
    "apiKey": news_api
}




stock_data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()]
yesterday_data = stock_data_list[0]
yesterday_closing = float(yesterday_data["4. close"])
day_before_yesterday_data = stock_data_list[1]
day_before_yesterday_closing = float(day_before_yesterday_data["4. close"])
difference = float(yesterday_closing) - float(day_before_yesterday_closing)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
    
difference_percentage = round((difference / yesterday_closing) * 100)
print(difference_percentage)

if abs(difference_percentage) >= 1:
    news_response = requests.get(news_url, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"{stock}: {up_down}{difference_percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    for article in formatted_articles:
        message = client.messages.create(
        from_='+16183427045',
        body=article,
        to='+919574434446'
        )



