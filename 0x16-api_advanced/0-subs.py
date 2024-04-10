#!/usr/bin/python3
""" Contains number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """
    Retures the number of subscribers for a given subreddit
    - If not a valid subreddit, return 0.
    """
    headers = {
        "User-Agent": 'Mozilla/5.0'
    }
    r = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                     headers=headers,
                     allow_redirects=False)

    if r.status_code == 404:
        return 0
    return r.json().get("data").get("subscribers")
