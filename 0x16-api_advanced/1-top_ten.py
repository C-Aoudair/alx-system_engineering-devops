#!/usr/bin/python3
""" Document"""

import requests


def top_ten(subreddit):
    """ Document"""

    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    if request.status_code == 200:
        for get_data in request.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            print(title)
    else:
        print(None)