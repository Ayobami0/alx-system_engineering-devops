#!/usr/bin/python3
"""
Module for Task:1

Top Ten
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a subreddit."""
    resp = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=9".format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit\
/537.36(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        },
        allow_redirects=False,
    )
    body = resp.json()
    if body.get('error') == 404:
        print(None)
        return

    for post in body["data"]["children"]:
        print(post['data']['title'])
