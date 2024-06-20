#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Fetches and prints the titles of the top ten hot posts from a given
    subreddit on Reddit.

    Parameters:
    - subreddit (str): The name of the subreddit to fetch posts from.

    Returns:
    None
    """
    headers = {'User-Agent': 'my-app/0.0.1'}

    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print(None)
    except Exception as e:
        print(None)
