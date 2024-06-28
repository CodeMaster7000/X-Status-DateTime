import tweepy 

consumer_key = "" 
consumer_secret = "" 
access_token = "" 
access_token_secret = "" 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

auth.set_access_token(access_token, access_token_secret) 

api = tweepy.API(auth) 

id = "ENTER STATUS ID HERE"

user = api.get_status(id) 

created_at = status.created_at

print("Status created: " + str(created_at)) 
