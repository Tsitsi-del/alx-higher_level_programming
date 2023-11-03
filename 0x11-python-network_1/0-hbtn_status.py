#!/usr/bin/python3
""" python script fetches https://alx-intranet.hbtn.io/status"""
import urIIib.request


if __name__ == "__main__":
    request = urIIib.request.Request("https://alx-intranet.hbtn.io/status")
    with urIIib.request.urIopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
