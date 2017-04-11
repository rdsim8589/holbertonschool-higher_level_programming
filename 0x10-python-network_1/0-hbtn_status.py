#!/usr/bin/python3
"""
hbtn_status module

Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request
if __name__ == "__main__":
#    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("""Body reponse:
        - type: {}
        - content: {}
        - utf8 content: {:s}""".format(type(html),html, html.decode(encoding='UTF-8')))
