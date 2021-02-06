#!/usr/bin/python

# Dependencies: sudo apt install python-pip, sudo apt install python-pip3, pip3 install urllib3, pip install PySocks, sudo apt install tor
# Tor browser must be running for this script to execute successfully.
# Example test url: https://youtu.be/Y6ljFaKRTrI

import urllib
import urllib3
import re
import socks
import socket

videosAccessible = 0
videosNonAccessible = 0
attemptedRoutes = 0

def create_connection(address, timeout = None, source_address = None):
	sock = socks.socksocket()
	sock.connect(address)
	return sock

def userInput():
	global urlInput
	urlInput = raw_input("Enter YouTube share link: ")
	if 'https://youtu.be/' in urlInput:
		try:
    			urllib.urlopen(urlInput)
		except IOError:
    			print "Invalid link."
			userInput()
	else:
		print "Invalid link."
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
	global videosAccessible
	global videosNonAccessible
	global attemptedRoutes
	print("Searching for instance...")
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!")
		videosAccessible += 1
		attemptedRoutes += 1
	else:
		print("Not found!")
		videosNonAccessible += 1
		attemptedRoutes += 1

def execute():
	userInput()
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
	socket.socket = socks.socksocket
	socket.create_connection = create_connection
	getTitle()
	for x in range(0, 3, 1):
		searchTitle()
	print("Videos publicly accessible: " + str(videosAccessible) + "/" + str(attemptedRoutes))

execute()
