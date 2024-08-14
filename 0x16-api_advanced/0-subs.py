#!/usr/bin/python3
"""
Module to query the Reddit API for the number of subscribers
for a given subreddit using PRAW.
"""

import praw

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API using PRAW to return the number of subscribers
    for a given subreddit. Returns 0 if the subreddit is invalid.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: Number of subscribers or 0 if the subreddit is invalid.
    """
    reddit = praw.Reddit(
        client_id='LSNpbK15FsQpfsf_a_bgTA',
        client_secret='vu-CHv2VGwI1XhIvThrlbcrgNcXseg',
        user_agent='alxse script by u/ctbrjg1067'
    )

    try:
        sub = reddit.subreddit(subreddit)
        return sub.subscribers
    except Exception:
        return 0
