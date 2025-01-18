#!/usr/bin/python3
"""script that fetches url using requests lib"""

import requests

response = requests.get("https://alx-intranet.hbtn.io/status")

print("Body response:")
print(f"\t- type: {type(response.text)}")
print(f"\t- content: {response.text}")
response.close()
