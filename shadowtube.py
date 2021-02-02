#!/usr/bin/python
# Dependencies: urllib3

import urllib3
import re

## Fetches and stores the inputted youtube URL's title

url = raw_input("Enter YouTube URL: ")
http = urllib3.PoolManager()
fetch = http.request('GET', url)
a = fetch.data
start = '{"title":{"runs":[{"text":"'
end = '"}]},"viewCount"'
title = a[a.find(start)+len(start):a.rfind(end)]
#print(title)

## Formats video link's title into YouTube search link

query = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
print(query)

#3 Fetches data from query link
#fetchQuery = http.request('GET', query)
#b = fetchQuery.data
#searchTitle = b[b.find(start)+len(start):b.rfind(end)]
#print(searchTitle)
