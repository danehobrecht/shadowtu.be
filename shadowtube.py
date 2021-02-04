#!/usr/bin/python
# Dependencies: urllib3
# Test url: https://youtu.be/Y6ljFaKRTrI

import urllib3
import re

def userInput():
	global urlInput
	urlInput = raw_input("Enter YouTube URL: ")

def getTitle():
	global http
	global title
	http = urllib3.PoolManager()
	fetchUrlInput = http.request('GET', urlInput)
	a = fetchUrlInput.data
	start = '{"title":{"runs":[{"text":"'
	end = '"}]},"viewCount"'
	title = a[a.find(start)+len(start):a.rfind(end)]

def searchTitle():
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!")
	else:
		print("Not found!")

userInput()
getTitle()
searchTitle()
