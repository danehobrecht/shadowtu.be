#!/usr/bin/python
# Dependencies: urllib3, PySocks, python-socks, tor
# Test url: https://youtu.be/Y6ljFaKRTrI
# Tor Browser must be running in the background to access the tor service

import urllib3
import re
import socks
import socket

def createConnection(address, timeout = None, source_address = None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)

# patch the socket module
socket.socket = socks.socksocket
socket.createConnection = createConnection

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
