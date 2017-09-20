# Dependencies
import tweepy
import time
import json

# Twitter API Keys
consumer_key = "NDia3lgb7QR258CMpk5hWh1Ff"
consumer_secret = "5gXd49SjH3fihwoBLNCp6KYybCwOQSPvnWBnOwTRiu7jiIrInO"
access_token = "907734478159826946-0xIx20UVDhVxdEtWuyzvMX9az0rg2V5"
access_token_secret = "sNW0efMBw7QsqcFCJVbH0r5iZ7ucd1ovcP7QHhoAO1CRC"



# Quotes to Tweet
quote_list = [
    "There is nothing permanent except change. - Heraclitus",
    "You cannot shake hands with a clenched fist. - Indira Gandhi",
    "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
    "Learning never exhausts the mind. - Leonardo da Vinci",
    "There is no charm equal to tenderness of heart. - Jane Austen"]


# Create function for tweeting
def QuoteItUp(quote_num):
   
    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
counter = 0

while(counter < len(quote_list)):
    QuoteItUp(counter)
    time.sleep(60)
