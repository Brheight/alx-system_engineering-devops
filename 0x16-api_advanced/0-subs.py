#!/usr/bin/python3
"""
0-subs
"""

import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/ctbrjg1067)'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return 0
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return 0
