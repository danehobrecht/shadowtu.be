#!/usr/bin/env python

# Example test url: https://youtu.be/Y6ljFaKRTrI

from __future__ import print_function
from lxml.cssselect import CSSSelector
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
import json
import os
import argparse
import lxml.html

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
	i = 0;
	for i in range(links.count("'") / 2):
		i += 1
		time.sleep(3)
		youtube_id = links.split("'")[i]
		comment = commentIds.split("'")[i]
		fetchComments(youtube_id.replace('https://www.youtube.com/watch?v=', ''))
		print("Link being analyzed: " + youtube_id)
		print("CID in question: " + comment + "\n")
		print("Searching for comment..."),
		with open('json.json', 'r') as json:
    			b = json.read()
		if b.find(comment) >= 0:
			print("Comment found!")
			commentsAccessible += 1
			attemptedRoutesC += 1
		else:
			print("Comment not found.")
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

# Downloader

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v={youtube_id}'
YOUTUBE_COMMENTS_AJAX_URL = 'https://www.youtube.com/comment_service_ajax'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

def find_value(html, key, num_chars = 2, separator = '"'):
    pos_begin = html.find(key) + len(key) + num_chars
    pos_end = html.find(separator, pos_begin)
    return html[pos_begin: pos_end]

def ajax_request(session, url, params = None, data = None, headers = None, retries = 5, sleep = 20):
    for _ in range(retries):
        response = session.post(url, params=params, data=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code in [403, 413]:
            return {}
        else:
            time.sleep(sleep)

def download_comments(youtube_id, sleep = .1):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT

    response = session.get(YOUTUBE_VIDEO_URL.format(youtube_id = youtube_id))
    html = response.text
    session_token = find_value(html, 'XSRF_TOKEN', 3)
    session_token = session_token.encode('ascii').decode('unicode-escape')

    data = json.loads(find_value(html, 'var ytInitialData = ', 0, '};') + '}')
    for renderer in search_dict(data, 'itemSectionRenderer'):
        ncd = next(search_dict(renderer, 'nextContinuationData'), None)
        if ncd:
            break
    continuations = [(ncd['continuation'], ncd['clickTrackingParams'])]

    while continuations:
        continuation, itct = continuations.pop()
        response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL,
                                params={'action_get_comments': 1,
                                        'pbj': 1,
                                        'ctoken': continuation,
                                        'continuation': continuation,
                                        'itct': itct},
                                data={'session_token': session_token},
                                headers={'X-YouTube-Client-Name': '1',
                                         'X-YouTube-Client-Version': '2.20201202.06.01'})

        if not response:
            break
        if list(search_dict(response, 'externalErrorMessage')):
            raise RuntimeError('Error returned from server: ' + next(search_dict(response, 'externalErrorMessage')))

        continuations = [(ncd['continuation'], ncd['clickTrackingParams'])
                         for ncd in search_dict(response, 'nextContinuationData')] + continuations

        for comment in search_dict(response, 'commentRenderer'): # downloads comments
            yield {'cid': comment['commentId'],'text': ''.join([c['text'] for c in comment['contentText']['runs']])}

        time.sleep(sleep)

def search_dict(partial, search_key):
    stack = [partial]
    while stack:
        current_item = stack.pop()
        if isinstance(current_item, dict):
            for key, value in current_item.items():
                if key == search_key:
                    yield value
                else:
                    stack.append(value)
        elif isinstance(current_item, list):
            for value in current_item:
                stack.append(value)


def fetchComments(youtube_id):
    parser = argparse.ArgumentParser()
    try:	
        args = parser.parse_args()
        output = 'json.json'
        limit = 100
        if not youtube_id or not output:
            parser.print_usage()
            raise ValueError('Faulty YouTube Video ID.')
        if os.sep in output:
            outdir = os.path.dirname(output)
            if not os.path.exists(outdir):
                os.makedirs(outdir)
	print('\nDownloading comments (depending on the video, this may take a while)...')
        print('Video ID: ' + youtube_id + "\n")
        count = 0
        with io.open(output, 'w', encoding = 'utf8') as fp:
            for comment in download_comments(youtube_id):
                comment_json = json.dumps(comment, ensure_ascii=False)
                print(comment_json.decode('utf-8') if isinstance(comment_json, bytes) else comment_json, file=fp)
                count += 1
                if limit and count >= limit:
                    break
        print('Done!\n')
    except Exception as e:
        print('Error:', str(e))
        exit()

# Menu

print("\nShadowTube\n\n1. Videos\n2. Comments\n")
menuInput()
