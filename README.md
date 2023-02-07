# Python-Stock-Trading-News-Notifier

Hello! This is a python program that is used for notifying Stock Trading News via SMS. I've referenced this from Angela's 100 Days of Python Udemy Course. There are a few things that you will need to do in order to make this API work.
an Example of a Stock Trading News Section is right here. Let's take Tesla for example:
![tesla example](https://user-images.githubusercontent.com/68105213/217297825-5d37d11b-dc6e-405c-89ca-8a8254833cd6.png)
What we want is a reproduction of this, but on an SMS.


![image](https://user-images.githubusercontent.com/68105213/217299272-d8e876e8-eed7-40a3-9794-786335c17ed3.png)




The idea here is that we want to compare the closing prices of a certain company's stock (In this case, it is Tesla) to the day before yesterday (y3) and yesterday (y2).
If there is a difference in closing stock price, then depending on the situation, a news article will pop up in your SMS messanger (or in any phone number you specify it to).




You will need to import a few libraries like so:


![image](https://user-images.githubusercontent.com/68105213/217293776-77330ef0-c08c-4b53-98ac-dcec72e1a386.png)


The request library is used for getting data and information from external APIs, and also establish connections with.

You will also need to install the twilio rest library to connect python/your environment. 
The links for all the APIs:

Twilio:
https://www.twilio.com

Alphavantage:
https://www.alphavantage.co

News API:
https://newsapi.org







