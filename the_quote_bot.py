#Importing required modules
import requests
import tweepy
from time import sleep
from credentials import *
from time import sleep

#Calling twitter api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Where the magic happens
n=1
sleep_time = int(input("Enter the duration between 2 tweets (in seconds) - ")) # To set a sleep time
hashtags = ("#hashtag1" "hashtag2") #use hashtags for enguagement 

while n<1000000000000000000000000000000:

    try:
        url = 'https://api.quotable.io/random' #Website for scraping quotes
        r = requests.get(url)
        quote = r.json()
        a = quote['content'] + '    -' + quote['author']
        print('Number of tweets so far - ', n)
        print ('Quote - ' , a)
        tweet = api.update_status(a + hashtags) #tweet the quote
        n = n+1
        sleep(sleep_time)

    except StopIteration:
        break
    
#Code by @icecracker_hem (github.com/icecrac34r)
