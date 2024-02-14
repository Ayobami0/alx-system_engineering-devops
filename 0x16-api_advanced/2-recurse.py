#!/usr/bin/python3
"""
Module for Task:2

Recurse it!
"""


import requests


def append_recurse(src, dest, count=0):
    """Recussively append an item from a source to a destination."""
    if len(src) < 1:
        return
    if count == len(src) - 1:
        return
    dest.append(src[count]["data"]["title"])
    append_recurse(src, dest, count + 1)


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API.

    Returns a list containing the titles of all
    hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
        subreddit,
        after,
    )

    resp = requests.get(
        url,
        allow_redirects=False,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit\
/537.36(KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
        },
    )
    body = resp.json()
    if body.get("error") == 404:
        return None

    append_recurse(body["data"]["children"], hot_list)

    after = body["data"]["after"]

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
