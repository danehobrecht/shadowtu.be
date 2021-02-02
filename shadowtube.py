#!/usr/bin/python
# Dependencies: urllib3

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

## Formats link into YouTube title search

title = "https://www.youtube.com/results?search_query=" + "+".join( title.split() )
print(title)
