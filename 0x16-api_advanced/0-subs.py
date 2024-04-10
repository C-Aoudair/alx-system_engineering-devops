#!/usr/bin/python3
""" Contains number_of_subscribers function"""


def number_of_subscribers(subreddit):
    """ Retures the number of subscribers for a given subreddit"""

    import requests

    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json')

    data = r.json()
    if data is None:
        return 0
    return data.get('data').get('subscribers')
