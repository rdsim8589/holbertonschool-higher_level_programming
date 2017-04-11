#!/usr/bin/python3
"""
module that fetches https://intranet.hbtn.io/status

Using the requests package
"""
import requests
if __name__ == "__main__":
    r = requests.get("https://intranet.hbtn.io/status")
    print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {:s}""".format(type(r.content),
                                 r.content,
                                 r.text))
