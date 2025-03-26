from pymongo import MongoClient
from pymongo.errors import PyMongoError
import os
import praw

def get_reddit_posts():
    posts = []
    filtered_posts = []
    reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="test",
    )
    
    for submission in reddit.subreddit("recipes").new(limit=1000):
        comments = []
        if "MOD PSA" in submission.title:
            continue
        submission.comments.replace_more(limit=0)
        for comment in submission.comments:
            comments.append(comment.body)
        row = {
            "title": submission.title,
            "comments": comments
            }         
        posts.append(row)

    print(f"size of posts list: {len(posts)}" )

    for post in posts:
        filtered_comments = [comment for comment in post["comments"] if "ingredients" in comment.lower()]
        
        if filtered_comments:
            post["comments"] = filtered_comments
            filtered_posts.append(post) 

    print(f"size of filtered posts list: {len(filtered_posts)}" )

    return filtered_posts

def store_in_db():
    try:
        client = MongoClient(os.getenv("DATABASE_URL"))
        db = client["recipes_db"]
        collection = db["recipes"]
        posts = get_reddit_posts()
        collection.insert_many(posts)
    except PyMongoError:
        print("Database error occured {e}")

store_in_db()



