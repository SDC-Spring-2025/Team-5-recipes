from pymongo import MongoClient
import os
import praw



def get_reddit_posts():
    posts = []
    reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="test",
)
    
    for submission in reddit.subreddit("recipes").hot(limit=10):
        comments = []
        if "MOD PSA" in submission.title:
            continue
        submission.comments.replace_more(limit=None)
        for comment in submission.comments.list():
            comments.append(comment.body)
        row = {
            "title": submission.title,
            "comments": comments
            }         
        posts.append(row)

    return posts

print(get_reddit_posts())



def parse_posts():
    return 

def store_in_db():
    client = MongoClient(os.getenv("DATABASE_URL"))

    

'''
all 1000 posts in a list [] 
{'title': samgaetang, 'body': 'ingredients and methods'}
'''




