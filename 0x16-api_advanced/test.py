import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    #headers = {'User-Agent': 'Your-User-Agent-Here'}  # Add a valid user agent
    headers = {'User-Agent': 'MyRedditApp/1.0 (by /u/ctbrjg1067)'}  

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers_count = data['data']['subscribers']
        print(subscribers_count)
        return subscribers_count
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return 0
number_of_subscribers("science")
