#!/usr/bin/python3
"""
Python script that takes in a URL, sends request to the URL
and displays the body of the response
"""
import sys
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        print(response.read().decode(encoding='UTF-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
