#!/usr/bin/python3
"""Script Post request to a given URL with a given email"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    val = {"email": sys.argv[2]}

    req = requests.post(url, data=val)
    print(req.text)
