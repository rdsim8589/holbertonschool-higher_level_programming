#!/usr/bin/python3
"""
module that takes in an URL and email, sends a POST request
to the passed URL with the email as a parameter , and displays
the body of the response (decode in utf-8)
"""
import sys
import urllib.parse
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    # urlencode converts a mapping obj to str or bits
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, method="POST")
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode(encoding='UTF-8'))
