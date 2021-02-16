#!/usr/bin/python

# Dependencies: sudo apt install python-pip, sudo apt install python-pip3, pip3 install urllib3, pip install PySocks, sudo apt install tor
# Example test url: https://youtu.be/Y6ljFaKRTrI
# Tor Browser must be running for this script to execute successfully.

import urllib, urllib2, urllib3, socks, socket, re, requests, time, io
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

def menuInput():
	choice = raw_input("Choose one of the listed options: ")	
	if choice == "1":
		try:
			shareUrlInput()
		except IOError:
			print("\nInvalid input.")
			menuInput()		
	elif choice == "2":
		try:
			getComments()
		except IOError:
			print("\nInvalid input.")
			menuInput()
	else: 
		print("\nInvalid input.\n")
		menuInput()

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
		s = getTorSession()
		ip = s.get("http://icanhazip.com").text
		print("IP being tested: " + ip)
		searchTitle()
		print("Rotating IP...\n")
		time.sleep(9)
		renewConnection()
	print(str(videosAccessible) + "/" + str(attemptedRoutes) + " public instances found.\n")

def getComments():
	#https://www.youtube.com/feed/history/comment_history
	with io.open("Google - My Activity.html", 'r', encoding='utf-8') as commentHistoryHtml:
		strCommentHistoryHtml = commentHistoryHtml.read()
		f = strCommentHistoryHtml.replace("\n", "").replace("'", "").replace('"', '').replace('[', '').replace(']', '')
		print(f) 
		#start = '["YouTube",null,"https://www.gstatic.com/images/branding/product/2x/youtube_24dp.png"],null,["'
		#end = '"],null,null,[],[],null,null,null,null,null,[],[]'
		comments = re.findall(r'.png,null,(.*?),null,null,,,', f)
		#comments = f[f.find(start)+len(start):f.rfind(end)]
		print(comments)

print("\nShadowTube\n\n1. Videos\n2. Comments\n")
menuInput()
