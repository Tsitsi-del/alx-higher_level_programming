#!/usr/bin/python3
"""Script sends a post request to http://0.0.0.0:5000/search_user with a given letter."""
import requests
import sys


if __name__ == "__main__":
    lttr = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": lttr}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(repsonse.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
