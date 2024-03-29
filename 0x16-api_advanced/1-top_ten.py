#!/usr/bin/python3
"""
1-top_ten
"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/ctbrjg1067)'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            print("No posts found.")
            return

        for i, post in enumerate(posts[:10], 1):
            title = post['data']['title']
            print(f"{i}. {title}")
    elif response.status_code == 404:
        print(None)
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
