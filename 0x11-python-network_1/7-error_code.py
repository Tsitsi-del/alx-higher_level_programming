#!/usr/bin/python3
"""Script to send a request to a given URL and display the response body"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
