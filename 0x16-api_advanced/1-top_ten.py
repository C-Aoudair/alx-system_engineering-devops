#!/usr/bin/python3
""" Document"""

import requests


def top_ten(subreddit):
    """ Document"""

    request = requests.get(
        f"https://www.reddit.com/r/{subreddit}/hot.json",
        headers={"User-Agent": "MyPythonScript/1.0 (Ubuntu 20.04; Python 3.4.3)"},
        params={"limit": 10},
    )

    if request.status_code == 200:
        for resulte in request.json().get("data").get("children"):
            post = resulte.get("data")
            title = post.get("title")
            print(title)
    else:
        print(None)