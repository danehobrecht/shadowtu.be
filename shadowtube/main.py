#!/usr/bin/python
# Dependencies: python-pip, python-pip3, urllib, urllib3
# Example test url: https://youtu.be/Y6ljFaKRTrI

import urllib
import urllib3
import re

accessible = 0
nonAccessible = 0

def userInput():
	global urlInput
	urlInput = raw_input("Enter YouTube URL: ")
	try:
    		urllib.urlopen(urlInput)
	except IOError:
    		print "Invalid URL."
		userInput()

def getTitle():
	global http
	global title
	print("Fetching title...")
	http = urllib3.PoolManager()
	fetchUrlInput = http.request('GET', urlInput)
	a = fetchUrlInput.data
	start = '{"title":{"runs":[{"text":"'
	end = '"}]},"viewCount"'
	title = a[a.find(start)+len(start):a.rfind(end)]

def searchTitle():
	global accessible
	global nonAccessible
	print("Searching for title...")
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!")
		accessible += 1
	else:
		print("Not found!")
		nonAccessible += 1

userInput()
getTitle()

for x in range(0, 3, 1):
	searchTitle()

print("Videos publicly accessible: " + str(accessible) + "/" + "?")

# Calling external script: subprocess.call("./py.py", shell = False)
