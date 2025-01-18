#!/usr/bin/python3
"""sends a POST request to the passed URL
with the email as a parameter, and displays
the body of the response (decoded in utf-8)"""

import sys
from urllib.request import urlopen, Request
from urllib.parse import urlencode

if __name__ == "__main__":

    email = sys.argv[2]
    post_dict = {"email": email}
    url_encoded_data = urlencode(post_dict)
    post_data = url_encoded_data.encode("UTF-8")
    req = Request(sys.argv[1], data=post_data)
    with urlopen(req) as response:
        page_ = response.read().decode('utf-8')
        print(page_)
