import tweepy
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

# this api object allows us to make the requests
api = tweepy.API(auth)
print("API CLIENT", type(api))

if __name__ == "__main__":
    
    user = api.get_user('NateDow33')
    print("User type: ", type(user))

    pprint(user._json)
    print(user.id)
    print(user.screen_name)
    print(user.followers_count)

    tweets = api.user_timeline("NateDow33", tweet_mode="extended", count=150)
    print(type(tweets))

    for tweet in tweets:
        print("------------------------")
        print(tweet.id, tweet.full_text)


