#!/usr/bin/python3
"""
a recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches the titles of hot posts from a given subreddit on Reddit.

    This function constructs a URL to fetch hot posts from the specified subreddit,
    then recursively calls itself to fetch subsequent pages of posts until there
    are no more posts left to fetch (i.e., the 'after' parameter is None).

    Parameters:
    - subreddit (str): The name of the subreddit to fetch hot posts from.
    - hot_list (list): A list to store the titles of fetched posts.
                                 Defaults to an empty list.
    - after (str, optional): The cursor for pagination.
                             Used to fetch subsequent pages of posts.
                             Defaults to None.

    Returns:
    - list: A list of titles of hot posts fetched from the subreddit.
             If an error occurs during fetching, None is returned.
    """
    headers = {'User-Agent': 'my-app/0.0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100'

    if after:
        url += f'&after={after}'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except Exception as e:
        return None
