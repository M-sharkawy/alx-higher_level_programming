#!/usr/bin/python3
"""script that takes in a URL, sends a request
to the URL and displays the value of the X-Request-Id"""

from urllib.request import urlopen
import sys

with urlopen(sys.argv[1]) as response:
    header = response.getheader("X-Request-Id")
    print(header)
