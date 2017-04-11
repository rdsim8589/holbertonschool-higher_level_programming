#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id
"""
import urllib.request
import sys
if __name__ == "__main__":
    try:
        # urllib.request.urlopen(<url>) returns a HTTPResponse Object
        with urllib.request.urlopen(sys.argv[1]) as request:
            # info returns a dictionary of the HTTP header
            print(request.info()['X-Request-Id'])
    except Exception as e:
        pass
