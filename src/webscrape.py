import praw, random
import os
from dotenv import load_dotenv


def scrape_data(subreddit_name:str) -> tuple[str, str]:
    """Scrapes a random post from a subreddit and returns the title and description of the post.
    
    Parameters
    ----------
    subreddit_name : str
        Name of the subreddit to scrape from.
        
    Returns
    -------
    tuple[str, str]
        A tuple of the post's title and description"""
    
    # Get sensitive data from .env file
    load_dotenv()
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    USER_AGENT = os.getenv("USER_AGENT")
    
    # Instantiate praw
    reddit = praw.Reddit(
        client_id = CLIENT_ID,
        client_secret = CLIENT_SECRET,
        user_agent = USER_AGENT
    )

    # Get subreddit
    subreddit = reddit.subreddit(subreddit_name)

    # Get a bunch of posts and convert them into a list
    posts = subreddit.new(limit=100)
    posts = list(posts)

    # Get random number
    random_number = random.randint(0, 100)

    # Store post's title and description in variables
    post_title = posts[random_number].title
    post_description = posts[random_number].selftext
    
    
    return post_title, post_description