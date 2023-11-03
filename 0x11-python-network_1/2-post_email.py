#!/usr/bin/python3
""" Sends a Post to a given URL with a given email"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}
    dat = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(url, dat)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
