import time
import tweepy
import random
import praw
import urllib.request
import os



def Mainbot():
    reddit = praw.Reddit(client_id='SECRET',
                          client_secret='SECRET',
                          user_agent='RedditFetchBot by FlyingThunder')

    def Tweet(postinfo):
        auth = tweepy.OAuthHandler("SECRET", "SECRET")
        auth.set_access_token("SECRET",
                              "SECRET")
        api = tweepy.API(auth)
        api.update_with_media("local-filename.jpg", postinfo)
        os.remove("local-filename.jpg")


    post = reddit.subreddit('okbrudimongo').random()
    urllib.request.urlretrieve(post.url, "local-filename.jpg")
    Tweet(postinfo=post.title+"(https://www.reddit.com" + post.permalink+")")

while True:
    Mainbot()
    time.sleep(600)