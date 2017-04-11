#!/usr/bin/python3
"""
module to take in the URl and email,
sends a POST request
passes the URL as a parameter
finally displays the header
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    print(r.text)
