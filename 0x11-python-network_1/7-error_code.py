#!/usr/bin/python3
"""script that sends a request to the URL
and displays the body of the response."""

import requests
import sys
from requests.exceptions import HTTPError

if __name__ == "__main__":

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except HTTPError as err:
        print("Error code:", response.status_code)
    
