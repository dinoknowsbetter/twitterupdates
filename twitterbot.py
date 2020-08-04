import tweepy
import time
from discord import Webhook, RequestsWebhookAdapter


#insert your twitter developer api keys here
consumer_key = 'CHANGE_ME'
consumer_secret = 'CHANGE_ME'
access_token = 'CHANGE_ME'
access_token_secret = 'CHANGE_ME'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)
oldurl = ''

api = tweepy.API(auth)

#change the webhook ID and token here
webhook = Webhook.partial(CHANGE_ME, 'CHANGE_ME', adapter=RequestsWebhookAdapter())

username = 'dinoknowsbetter'


while True:
    tweets = api.home_timeline()
    url = 'https://twitter.com/' + username + '/status/' + str(tweets[0].id)
    if url != oldurl:
        oldurl = url
        #this is a console message, you can turn it off
        print('Pushed a notification to discord for tweet: ' + url)
        #this is the message being sent to discord, tweak it to your liking
        webhook.send('DinoKnowsBest just tweeted, check it out: ' + url, username='TwitterBot')
    else:
        #this is a console message, you can turn it off
        print('Nothing new')
    time.sleep(60)
