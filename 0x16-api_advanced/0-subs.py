#!/usr/bin/python3
""" Contains number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    Retures the number of subscribers for a given subreddit
    - If not a valid subreddit, return 0.
    """
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    r = requests.get("https://www.reddit.com/r/{}/about.json".format(subreddit),
                     headers=headers,
                     allow_redirects=False)

    if r.status_code == 404:
        return 0
    return r.json().get("data").get("subscribers")
