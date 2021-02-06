#!/usr/bin/python

# Dependencies: sudo apt install python-pip, sudo apt install python-pip3, pip3 install urllib3, pip install PySocks, sudo apt install tor
# Example test url: https://youtu.be/Y6ljFaKRTrI
# Tor Browser must be running for this script to execute successfully.

import urllib
import urllib3
import re
import socks
import socket
import requests
import time
from stem.control import Controller
from stem import Signal

videosAccessible = 0
attemptedRoutes = 0

def getTorSession():
    session = requests.Session()
    session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
    return session

def renewConnection():
    with Controller.from_port(port = 9151) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

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
	print("Done.\n")

def searchTitle():
	global videosAccessible
	global attemptedRoutes
	print("Searching for instance..."),
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!\n")
		videosAccessible += 1
		attemptedRoutes += 1
	else:
		print("Not found!\n")
		videosAccessible -= 1
		if videosAccessible < 0:
			videosAccessible = 0
		attemptedRoutes += 1

def execute():
	userInput()
	getTitle()
	for x in range(0, 30, 1):
		s = getTorSession()
		ip = s.get("http://icanhazip.com").text
		print("IP being tested: " + ip)
		searchTitle()
		print("Rotating IP...\n")
		time.sleep(9)
		renewConnection()
	print(str(videosAccessible) + "/" + str(attemptedRoutes) + " public instances found.")

execute()
