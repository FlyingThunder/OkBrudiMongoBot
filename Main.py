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


    sub = reddit.subreddit('okbrudimongo').new(limit=1000)
    random_post_number = random.randint(0,1000)


    for i,post in enumerate(sub):
        if i==random_post_number:
            urllib.request.urlretrieve(post.url, "local-filename.jpg")
            Tweet(postinfo=post.title+"(https://www.reddit.com" + post.permalink+")")

while True:
    Mainbot()
    time.sleep(3600)