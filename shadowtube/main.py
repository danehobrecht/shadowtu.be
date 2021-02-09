#!/usr/bin/python

# Dependencies: sudo apt install python-pip, sudo apt install python-pip3, pip3 install urllib3, pip install PySocks, sudo apt install tor
# Example test url: https://youtu.be/Y6ljFaKRTrI
# Tor Browser must be running for this script to execute successfully.

import urllib, urllib2, urllib3, re, socks, socket, requests, time
from stem.control import Controller
from stem import Signal

videosAccessible = 0
attemptedRoutes = 0

# Videos

def get_tor_session():
    session = requests.Session()
    session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
    return session

def renew_connection():
    with Controller.from_port(port = 9151) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

def userInput():
	print("\nChoose search type:\n\n1. Videos\n2. ?\n")
	choice = raw_input()	
	if choice == "1":
		try:
			shareUrlInput()
		except IOError:
			print("\nInvalid input.")
			userInput()		
	elif choice == "2":
		try:
			print("\nYou must be logged in to your Google account via your local browser to continue.\n")
		except IOError:
			print("\nInvalid input.")
			userInput()
	else: 
		print("\nInvalid input.")
		userInput()

def shareUrlInput():
	global shareUrl
	shareUrl = raw_input("\nEnter YouTube share link: ")
	if 'https://youtu.be/' in shareUrl:
		try:
			videosExecute()
		except IOError:
    			print("Invalid link. (is Tor running?)")
			shareUrlInput()
	else:
		print("\nInvalid link.")
		shareUrlInput()

def getTitle():
	global http
	global title
	print("\nFetching title...")
	http = urllib3.PoolManager()
	fetchShareUrl = http.request('GET', shareUrl)
	a = fetchShareUrl.data
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

def videosExecute():
	getTitle()
	for x in range(0, 3, 1):
		s = get_tor_session()
		ip = s.get("http://icanhazip.com").text
		print("IP being tested: " + ip)
		searchTitle()
		print("Rotating IP...\n")
		time.sleep(9)
		renew_connection()
	print(str(videosAccessible) + "/" + str(attemptedRoutes) + " public instances found.")

userInput()
