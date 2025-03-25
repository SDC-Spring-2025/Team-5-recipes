from pymongo import MongoClient
import os
import praw



def get_reddit_posts():
    reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="test",
)
    
    for submission in reddit.subreddit("recipes").hot(limit=10):
        print(submission.title)

get_reddit_posts()


def store_in_db():
    client = MongoClient(os.getenv("DATABASE_URL"))

    

'''
all 1000 posts in a list [] 
{'title': samgaetang, 'url': 'link', 'body': 'ingredients and methods'}
'''




