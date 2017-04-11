#!/usr/bin/python3
"""
Module that takes in a string and sends request to Star Wards API
"""
import sys
import requests
if __name__ == "__main__":
    try:
        url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
        r = requests.get(url)
        print("Number of results: {}".format(r.json()["count"]))
        for search_result in r.json().get("results"):
            print(search_result.get("name"))
    except IndexError:
        print("pass search parameter")
