#!/usr/bin/python

import urllib3
import re

# User Input

def userInput():
	global urlInput
	urlInput = raw_input("Enter YouTube URL: ")	

# Formatting

def getTitle():
	print("Fetching title...")
	global http
	global title
	http = urllib3.PoolManager()
	fetchUrlInput = http.request('GET', urlInput)
	a = fetchUrlInput.data
	start = '{"title":{"runs":[{"text":"'
	end = '"}]},"viewCount"'
	title = a[a.find(start)+len(start):a.rfind(end)]

# Searching

def searchTitle():
	global accessible
	accessible = 0;
	print("Searching for title...")
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!")
		accessible = accessible + 1 
	else:
		print("Not found!")
	print("Videos publicly accessible: " + str(accessible) + "/" + "?")

# Executing

userInput()
getTitle()
searchTitle()
