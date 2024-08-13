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
response = requests.get(stock_url) # Get the stock data
response.raise_for_status() # Raise an exception if the status code is not 200
stock_data = response.json() # Convert the data to JSON

news_url = "https://newsapi.org/v2/everything" # The news API endpoint
news_parameters = { # The news API parameters
    "q": company_name,
    "apiKey": news_api
}




stock_data_list = [value for (key, value) in stock_data["Time Series (Daily)"].items()] # Get the stock data list
yesterday_data = stock_data_list[0] # Get the data for yesterday
yesterday_closing = float(yesterday_data["4. close"]) # Get the closing price for yesterday
day_before_yesterday_data = stock_data_list[1]  # Get the data for the day before yesterday
day_before_yesterday_closing = float(day_before_yesterday_data["4. close"]) # Get the closing price for the day before yesterday
difference = float(yesterday_closing) - float(day_before_yesterday_closing) # Calculate the difference between the closing prices
up_down = None
if difference > 0: # Check if the difference is positive
    up_down = "🔺"
else: # If the difference is negative
    up_down = "🔻"
    
difference_percentage = round((difference / yesterday_closing) * 100) # Calculate the difference percentage
print(difference_percentage)

if abs(difference_percentage) >= 1: # Check if the difference percentage is greater than or equal to 1
    news_response = requests.get(news_url, params=news_parameters) # Get the news data
    news_response.raise_for_status() # Raise an exception if the status code is not 200
    articles = news_response.json()["articles"] # Get the articles
    three_articles = articles[:3]   # Get the first three articles
    formatted_articles = [f"{stock}: {up_down}{difference_percentage}%\nHeadline: {article['title']}\nBrief: {article['description']}" for article in three_articles] # Format the articles
    print(formatted_articles)
    for article in formatted_articles: # Loop through the articles
        message = client.messages.create(
        from_='FROM NUMBER',
        body=article,
        to='TO NUMBER'
        )



