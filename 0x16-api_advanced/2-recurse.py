#!/usr/bin/python3
""" Document"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """ Document"""
    headers={"User-Agent": "MyPythonScript/1.0 (Ubuntu 20.04; Python 3.4.3)"}
    params={"after": after}
    request = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers=headers,
        params=params
    )

    if request.status_code == 200:
        for get_data in request.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = request.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    return None