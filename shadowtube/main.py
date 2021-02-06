#!/usr/bin/python

# Dependencies: sudo apt install python-pip, sudo apt install python-pip3, pip3 install urllib3, pip install PySocks, sudo apt install tor
# Example test url: https://youtu.be/Y6ljFaKRTrI
# Tor browser must be running for this script to execute successfully.

import urllib
import urllib3
import re
import socks
import socket
import requests
import time
from stem.control import Controller
from stem import Signal

def get_tor_session():
    # initialize a requests Session
    session = requests.Session()
    # setting the proxy of both http & https to the localhost:9050 
    # this requires a running Tor service in your machine and listening on port 9050 (by default)
    session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
    return session

def renew_connection():
    with Controller.from_port(port = 9151) as c:
        c.authenticate()
        # send NEWNYM signal to establish a new clean connection through the Tor network
        c.signal(Signal.NEWNYM)

s = get_tor_session()
ip = s.get("http://icanhazip.com").text
print("\nCurrent IP: " + ip)

videosAccessible = 0
attemptedRoutes = 0

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
		videosAccessible -= 1
		if videosAccessible < 0:
			videosAccessible = 0
		attemptedRoutes += 1

def execute():
	userInput()
	getTitle()
	for x in range(0, 10, 1):
		searchTitle()
		print("Rotating IP...")
		time.sleep(9)
		renew_connection()
		s = get_tor_session()
		ip = s.get("http://icanhazip.com").text
		print("\nIP used: " + ip)
	print("Videos publicly accessible: " + str(videosAccessible) + "/" + str(attemptedRoutes) + "attempted routes.")

execute()
