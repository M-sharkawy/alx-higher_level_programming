#!/usr/bin/python3
"""script that takes in a letter
and sends a POST request to url with
the letter as a parameter"""

import requests
import sys

if __name__ == "__main__":

    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={"q": q})

    try:
        json_value = response.json()
        if json_value:
            print(f"[{json_value.get("id")}] {json_value.get("name")}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
