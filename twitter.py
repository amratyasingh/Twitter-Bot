import tweepy
import time
import keys as kk

auth = tweepy.OAuthHandler(kk.API_key,kk.API_key_secret)
auth.set_access_token(kk.Access_token,kk.Access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = input("Enter the hashtag or username for which you want to like tweets : ")
no_of_tweets = int(input("Enter the no of tweets you want to like : "))

for tweet in tweepy.Cursor(api.search, search).items(no_of_tweets):
    try:
        tweet.favorite()
        print('Tweet Liked')
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break