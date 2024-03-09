#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, after=None, count_dict=None):
    if count_dict is None:
        count_dict = {}

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    if after:
        params = {'after': after, 'limit': 100}
    else:
        params = {'limit': 100}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])

    for child in children:
        title = child.get('data', {}).get('title', '').lower()
        for word in word_list:
            if f' {word.lower()} ' in f' {title} ':
                count_dict[word] = count_dict.get(word, 0) + title.count(f' {word.lower()} ')

    after = data.get('after')
    if after:
        count_words(subreddit, word_list, after, count_dict)
    else:
        print_results(count_dict)

def print_results(count_dict):
    sorted_items = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_items:
        print(f'{word}: {count}')

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        count_words(subreddit, word_list)
