#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id
"""
import sys
import requests
if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except Exceptions as e:
        pass
