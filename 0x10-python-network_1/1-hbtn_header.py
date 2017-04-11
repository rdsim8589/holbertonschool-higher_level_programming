#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id
"""
import urllib.request
from sys import argv
if __name__ == "__main__":
    try:
        # urllib.request.urlopen(<url>) returns a HTTPResponse Object
        req = urllib.request.urlopen(argv[1])
        # info returns a dictionary of the HTTP header
        print(req.info()['X-Request-Id'])
    except Exception as e:
        print(e)
