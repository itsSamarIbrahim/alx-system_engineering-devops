#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not)
"""
import requests
from collections import Counter
import re


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Counts the occurrences of words from a given word list in the titles of hot
    posts on a specified subreddit.

    This function makes a request to Reddit's API to fetch hot posts from a
    specified subreddit, then iterates through the titles of these posts,
    counting the occurrences of words that match those in the provided
    word list.
    It supports pagination via the 'after' parameter to continue fetching posts
    beyond the initial limit.

    Parameters:
    - subreddit (str): The name of the subreddit to fetch posts from.
    - word_list (list[str]): A list of words to count occurrences of in the
                             post titles.
    - after (str): A cursor string to paginate through posts. Defaults to None,
                   indicating the start of the thread.
    - word_count (Counter): An existing Counter object to accumulate word
                            counts.
                            Defaults to None, creating a new Counter.

    Returns:
    - None: Prints the sorted word counts to stdout and does not return a value
    """
    if word_count is None:
        word_count = Counter()
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
                title = post['data']['title'].lower()
                words = re.findall(r'\b\w+\b', title)
                for word in words:
                    if word in word_list:
                        word_count[word] += 1
            after = data['data']['after']
            if after:
                return count_words(subreddit, word_list, after, word_count)
            else:
                sorted_word_count =
                (sorted(word_count.items(),
                        key=lambda item: (-item[1], item[0])))
                for word, count in sorted_word_count:
                    print(f'{word}: {count}')
                return
        else:
            return
    except Exception as e:
        return
