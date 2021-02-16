#!/usr/bin/python

# Example test url: https://youtu.be/Y6ljFaKRTrI

from stem.control import Controller
from stem import Signal

import urllib
import urllib2
import urllib3
import socks
import socket
import re
import requests
import time
import io

videosAccessible = 0
commentsAccessible = 0
attemptedRoutesV = 0
attemptedRoutesC = 0

# Tor

def getTorSession():
    session = requests.Session()
    session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
    return session

def renewConnection():
    with Controller.from_port(port = 9151) as c:
        c.authenticate()
        c.signal(Signal.NEWNYM)

# Input

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

# Videos

def getTitle():
	global http, title
	print("\nFetching title...")
	http = urllib3.PoolManager()
	fetchShareUrl = http.request('GET', shareUrl)
	a = fetchShareUrl.data
	start = '{"title":{"runs":[{"text":"'
	end = '"}]},"viewCount"'
	title = a[a.find(start)+len(start):a.rfind(end)]
	print("Done.\n")

def searchVideo():
	global videosAccessible, attemptedRoutesV
	print("Searching for instance..."),
	formatQuery = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
	fetchQuery = http.request('GET', formatQuery)
	b = fetchQuery.data
	if b.find(title) >= 0:
		print("Found!\n")
		videosAccessible += 1
		attemptedRoutesV += 1
	else:
		print("Not found!\n")
		videosAccessible -= 1
		if videosAccessible < 0:
			videosAccessible = 0
		attemptedRoutesV += 1

def videosExecute():
	getTitle()
	for x in range(0, 3, 1):
		ip = getTorSession().get("http://icanhazip.com").text
		print("IP being tested: " + ip)
		searchVideo()
		print("Rotating IP...\n")
		time.sleep(9)
		renewConnection()
	print(str(videosAccessible) + "/" + str(attemptedRoutesV) + " public instances found.\n")


# Comments

def getComments(): #https://www.youtube.com/feed/history/comment_history
	with io.open("Google - My Activity.html", 'r', encoding='utf-8') as commentHistoryHtml:
		global links, commentIds, parentLinks, replyLinks 
		f = commentHistoryHtml.read().replace("\n", "").replace("'", "").replace('"', '').replace('[', '').replace(']', '').replace(']', '')
		commentIds = str(re.findall('data-token=(.*?) data-date', f)).replace(", u", "").replace("]", "")
		links = str(re.findall('  <a href=(.*?)&', f)).replace(", u", "").replace("]", "")
		searchComment()
		#parentLinks = str(re.findall('Commented on  <a href=(.*?)&', f))
		#replyLinks = str(re.findall('comment on  <a href=(.*?)&', f))
		#print(f)
		#comments = re.findall('.png,null,(.*?),null,null,,,', f)
		#print("\nVideos supposedly featuring parent comment(s): " + str(parentLinksFormatted))
		#print("\nVideos supposedly featuring reply comment(s): " + str(replyLinksFormatted) + "\n\n")
		#print("\nComments: " + str(commentsFormatted))
		#print("\nLinks: " + str(linksFormatted) + "\n")

def searchComment():
	global commentsAccessible, attemptedRoutesC
	print("\nSearching for comment...\n\n"),
	i = 0;
	for i in range(links.count("'") / 2):
		i += 1
		link = links.split("'")[i]
		comment = commentIds.split("'")[i]
		with open('json.json', 'r') as json:
    			b = json.read()
		#print(link + " " + comment)
		if b.find(comment) >= 0:
			print("Comment found!\n")
			commentsAccessible += 1
			attemptedRoutesC += 1
		else:
			print("Comment not found.\n")
			commentsAccessible -= 1
			if commentsAccessible < 0:
				commentsAccessible = 0
				attemptedRoutesC += 1
	

def commentsExecute():
	for x in range(0, 3, 1):
		ip = getTorSession().get("http://icanhazip.com").text
		print("IP being tested: " + ip)
		searchComment()
		print("Rotating IP...\n")
		time.sleep(9)
		renewConnection()
	print(str(commentsAccessible) + "/" + str(attemptedRoutesC) + " public comments found.\n")

# Menu

print("\nShadowTube\n\n1. Videos\n2. Comments\n")
menuInput()
