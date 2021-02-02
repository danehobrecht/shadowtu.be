#!/usr/bin/python

import urllib3
import re

## Fetches and stores the inputted youtube URL's title
url = raw_input("Enter YouTube URL: ")
http = urllib3.PoolManager()
fetch = http.request('GET', url)
s = fetch.data
start = '{"title":{"runs":[{"text":"'
end = '"}]},"viewCount"'
title = s[s.find(start)+len(start):s.rfind(end)]
print(title)
