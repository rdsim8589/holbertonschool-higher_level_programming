#!/usr/bin/python3
"""
hbtn_status module

Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body reponse:\n"
              "\t- type: {}\n"
              "\t- content: {}\n"
              "\t- utf8 content: {:s}".format(type(html),
                                       html,
                                       html.decode('UTF-8')))
