#!/usr/bin/python3
"""
Script that takes Github credenials,
displays Id using Github API
"""
import sys
import requests
if __name__ == "__main__":
    try:
        user = sys.argv[1]
        password = sys.argv[2]
        r = requests.get("https://api.github.com/user", auth=(user, password))
        print(r.json().get('id'))
    except IndexError:
        print("give username and password")
