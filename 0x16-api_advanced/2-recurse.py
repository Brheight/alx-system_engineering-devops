#!/usr/bin/python3
"""
2-recurse
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list containing the titles of all hot articles
    for a given subreddit. If no results are found for the given subreddit, returns None.
    """
    if not hot_list:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    else:
        url = f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}'

    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/ctbrjg1067)'}  # Replace with your Reddit username

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if not posts:
            return hot_list

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
        return None
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")

