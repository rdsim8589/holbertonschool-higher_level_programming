#!/usr/bin/python3
"""
Module that takes in a string and sends request to Star Wards API
"""
import sys
import requests
if __name__ == "__main__":
    try:
        url = "https://swapi.co/api/people/?search={:s}".format(sys.argv[1])
        r = requests.get(url)
        total_count = r.json()["count"]
        count = 0
        print("Number of result: {}".format(total_count))
        while count != total_count:
            for search_result in r.json().get("results"):
                print(search_result.get("name"))
            r = requests.get(r.json().get("next"))
            count += 1
    except Exception as e:
        pass
