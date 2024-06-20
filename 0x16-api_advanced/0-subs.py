#!/usr/bin/python3
"""
a function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Fetches the number of subscribers for a given subreddit on Reddit.

    Parameters:
    - subreddit (str): The name of the subreddit to fetch subscriber count for.

    Returns:
    - int: The number of subscribers for the specified subreddit.
           Returns 0 if the subreddit does not exist,
           the request fails, or the status code is not 200.
    """
    headers = {"User-Agent": "Custom", }
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(url, headers=headers)

    try:
        if response.status_code == 200:
            return response.json().get("data").get("subscribers")
        else:
            return 0
    except Exception as e:
        return 0
