#Python Program for Stock Trading News API and Twillio API Usage
#For this examople I will be using tesla as the company template
from requests import ConnectionError
from twilio.rest import Client
import requests

#connection timeout seconds
connection_timeout = 30 

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

#use alpha vantage for stock api endpoint
#use news api for news api endpoint 
STOCK_ENDPOINT = "https://www.alphavantage.co.query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#import api keys for use
STOCK_API_KEY = "***(Your Own API Key)"
NEWS_API_KEY = "*****(Your Own API Key********)"

#TWILIO Application is used for SMS API for python
TWILIO_SID = "***********(Your Own Twilio SID)***********"
TWILIO_TOKEN = "********(Youw Own Twilio Token)***********"

#We can enter our url with the parameters like so. alphavantage needs time series intraday, company name, time interval, and your unique API key
url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=1min&apikey=**********"
#create a get request
response = requests.get(url)
data = response.json()["Time Series (1min)"]
data_list = [value for (key, value) in data.items()]

#y2 is yesterday, y3 is the day before yesterday
y2_data = data_list[0]
y2_cp = y2_data["4. close"]

#day before yesterday data
y3_data = data_list[1]
y3_cp = y3_data["4. close"]

#Find the positive difference of y2 closing price and y3 closing price
#Since it is a positive diff, we us abs 
difference = (float(y2_cp) - float(y3_cp))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

#Find percentage difference 
diff_percentage = (difference / float(y2_cp)) * 100
#If percentage is greater than 5, get the news article
#In this case we will use less than 5, since tesla's stock market is currently doing alright 
if diff_percentage < 5:
#implement news api using news parameters
#We get the articles list
    news_params = {
        "apiKey" : NEWS_API_KEY,
        "qInTitle" : COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params= news_params)
    articles = news_response.json()['articles']
    #Slice the list according to how many news articles you want
    tr_articles = articles[:3]
    
    #Create a list of the first 3 article's headline and description
    #We will create list comprehensions and format the articles
    
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in tr_articles]
        
    #Send each article as a separate message via Twilio
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body = article,
            #Send this from your own virtual twilio phone number
            from_= "+15739833871",
            #the testing phone number
            to   ="+************"               
        )
    