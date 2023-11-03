#!/usr/bin/python3
"""Script to display X-Request Id header variable of a request"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
