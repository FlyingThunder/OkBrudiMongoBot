import time
import tweepy
import datetime
import praw
import urllib.request
import os
import json


def Mainbot():
    reddit = praw.Reddit(client_id='X',
                          client_secret='X',
                          user_agent='X')

    def Tweet(postinfo):
        auth = tweepy.OAuthHandler("X", "X")
        auth.set_access_token("X",
                              "X")
        api = tweepy.API(auth)
        try:
            api.update_with_media("local-filename.jpg", postinfo)
        except:
            Mainbot()
        os.remove("local-filename.jpg")

    post = reddit.subreddit('okbrudimongo').random()
    x = post.id

    with open('data.json', 'r') as e:
        eread = e.read()
        if x not in eread:
            with open('data.json', 'a') as f:
                json.dump(x, f)
                f.close()
        else:
            e.close()
            Mainbot()

    print(post.url + " " + post.title)
    urllib.request.urlretrieve(post.url, "local-filename.jpg")
    Tweet(postinfo=post.title+" (https://www.reddit.com" + post.permalink+")")

def loop():
    time.sleep(600)
    print("still running")
    print(datetime.datetime.now())

while True:
    Mainbot()
    loop()
    loop()
    loop()
    loop()
    loop()
    loop()
