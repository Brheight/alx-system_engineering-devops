#!/usr/bin/python3
"""
Takes a URL and an email as arguments, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')

    with request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
