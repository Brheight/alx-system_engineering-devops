#!/usr/bin/python3
"""
Takes GitHub credentials (username and personal access token) as arguments,
uses Basic Authentication with the personal access token as the password
to access the GitHub API and displays the user id.
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print(None)
