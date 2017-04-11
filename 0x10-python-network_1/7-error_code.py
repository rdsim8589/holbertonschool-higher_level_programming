#!/usr/bin/python3
"""
modules that contains a script to take in a URL send a request.
It than displays the body response
"""
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    status_code = r.status_code
    if (status_code < 400):
        print(r.text)
    else:
        print("Error code: {:d}".format(status_code))
