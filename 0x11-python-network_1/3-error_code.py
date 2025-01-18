#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            body = response.read()
            print(body.decode('UTF-8'))
    except HTTPError as error:
        print('Error code:', error.code)
