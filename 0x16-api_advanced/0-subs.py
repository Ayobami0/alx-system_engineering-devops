#!/usr/bin/python3
"""
Module for Task:0

How many subs?
"""

import requests


def number_of_subscribers(subreddit):
    """Counts the number of subscribers in a subreddit."""
    resp = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit\
/537.36(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        },
        allow_redirects=False,
    )

    body = resp.json()

    if body.get("kind") != "t5":
        return 0

    return body["data"]["subscribers"]
