#!/usr/bin/python3
""" Contains number_of_subscribers function"""


def number_of_subscribers(subreddit):
    """
    Retures the number of subscribers for a given subreddit
    - If not a valid subreddit, return 0.
    """

    import requests

    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json')

    if r.status_code == 200:
        return r.json().get("data").get("subscribers")
    else:
        return 0
