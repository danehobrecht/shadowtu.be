#!/venv/bin/python3

from __future__ import print_function

from lxml.cssselect import CSSSelector
from stem.control import Controller
from stem import Signal

import lxml.html
import argparse
import requests
import urllib3
import urllib
import socket
import socks
import time
import json
import re
import io
import os

videoAttempts = 0
videosAccessible = 0

commentAttempts = 0
commentsAccessible = 0

YOUTUBE_VIDEO_URL = 'https://www.youtube.com/watch?v={youtubeId}'
YOUTUBE_COMMENTS_AJAX_URL = 'https://www.youtube.com/comment_service_ajax'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

# Tor

def getTorSession():
    session = requests.Session()
    session.proxies = {"http": "socks5://localhost:9150", "https": "socks5://localhost:9150"}
    return session

def renewConnection():
	time.sleep(9)
	with Controller.from_port(port = 9151) as c:
		c.authenticate()
		c.signal(Signal.NEWNYM)

# Videos - test url: https://youtu.be/Y6ljFaKRTrI

def videoExecute(shareUrl):
	global videosAccessible, videoAttempts
	if "https://youtu.be/" or "https://www.youtube.com/watch?v=" in str(shareUrl):
		try:
			checkTor = getTorSession().get("http://icanhazip.com").text
		except IOError:
			return """Tor service is down serverside. Please try again later."""
	else:
		return """Invalid input. """
	print("\nFetching title... ", end = "")
	http = urllib3.PoolManager()
	fsud = str(http.request('GET', shareUrl).data).replace("\n", "").replace("'", "").replace('"', '').replace("[", "").replace("]", "").replace("\\", "")
	titleFind = str(re.findall(',title:{simpleText:(.*?)},description:{simpleText:', fsud))
	title = titleFind.split("'")[1]
	print('done: "' + title + '".\n')
	for x in range(0, 5, 1):
		print("Current IP: " + getTorSession().get("http://icanhazip.com").text)
		print("Searching for instance... ", end = "")
		searchTitle = "https://www.youtube.com/results?search_query=" + "+".join(title.split())
		fetchQuery = str(http.request('GET', searchTitle).data)
		if fetchQuery.find(title) >= 0:
			print("found.")
			videosAccessible += 1
			videoAttempts += 1
		else:
			print("not found.")
			videosAccessible -= 1
			videoAttempts += 1
		if videosAccessible < 0:
			videosAccessible = 0
		print("\nRotating...")
		renewConnection()
	if videosAccessible == 0:
		conclusion = """likely shadowbanned (or non-existent)."""
	elif videosAccessible <= videoAttempts / 2:
		conclusion = """potentially shadowbanned."""
	elif videosAccessible == videoAttempts:
		conclusion = """unlikely shadowbanned."""
	return str(videosAccessible) + """/""" + str(videoAttempts) + """ public instances found - """ + conclusion

# Comments - https://www.youtube.com/feed/history/comment_history

def commentsExecute():
	global commentsAccessible, commentAttempts
	commentCharCount = 0
	index = 1
	if "jej" == "jej": # if file is uploaded as "Google - My Activity.html"
		try:
			checkTor = getTorSession().get("http://icanhazip.com").text
			commentsExecute()
		except IOError:
			return """The Tor service is down serverside. Please try again later."""
	else:
		return """Invalid file. """
	print("\nParsing comment history... ", end = "")
	with io.open("Google - My Activity.html", 'r', encoding = 'utf-8') as commentHistoryHtml:
		chh = commentHistoryHtml.read().replace("\n", "").replace("'", "").replace('"', '').replace("[", "").replace("]", "")
		comments = str(re.findall('.png,null,(.*?),null,null,,,', chh))
		commentIds = str(re.findall('data-token=(.*?) data-date', chh))
		links = str(re.findall('  <a href=(.*?)&', chh))
		print(" done.\n")
		#parentLinks = str(re.findall('Commented on  <a href=(.*?)&', f))
		#replyLinks = str(re.findall('comment on  <a href=(.*?)&', f))
		#print("\nVideos supposedly featuring parent comment(s): " + str(parentLinks) + "\n")
		#print("\nVideos supposedly featuring reply comment(s): " + str(replyLinks) + "\n")
		numOfLinks = links.count("'") / 2
	for i in range(int(numOfLinks)):
		link = links.split("'")[index]
		comment = comments.split("'")[index]
		commentId = commentIds.split("'")[index]
		index += 2
		fetchComments(link.replace("https://www.youtube.com/watch?v=", ""))
		for i in comment:
			commentCharCount += 1
		if commentCharCount >= 80:
			print('Text: "' + comment[0:80] + '..."')
		else:
			print('Text: "' + comment + '"')
		print('Searching for comment... ', end = "")
		with open('json.json', 'r') as json:
    			b = json.read()
		if b.find(commentId) >= 0:
			print("found.")
			commentsAccessible += 1
			commentAttempts += 1
		else:
			print("not found.")
			commentsAccessible -= 1
			if commentsAccessible < 0:
				commentsAccessible = 0
				commentAttempts += 1
		print("\nRotating...")
		renewConnection()
	return str(commentsAccessible) + """/""" + str(commentAttempts) + """ public comments found."""

def fetchComments(youtubeId):
	print("Current IP: " + getTorSession().get("http://icanhazip.com").text)
	parser = argparse.ArgumentParser()
	try:
		args = parser.parse_args()
		output = 'json.json'
		limit = 1000
		if not youtubeId or not output:
			parser.print_usage()
			raise ValueError('faulty video I.D.')
		if os.sep in output:
			if not os.path.exists(outdir):
				os.makedirs(outdir)
		print("Downloading comments from https://youtu.be/" + youtubeId + "... ", end = "")
		count = 0
		with io.open(output, 'w', encoding = 'utf8') as fp:
			for comment in download_comments(youtubeId):
				comment_json = json.dumps(comment, ensure_ascii=False)
				print(comment_json.decode('utf-8') if isinstance(comment_json, bytes) else comment_json, file=fp)
				count += 1
				if limit and count >= limit:
					break
		print('done.')
	except Exception as e:
		print('Error:', str(e))	
		exit()

def find_value(html, key, num_chars=2, separator='"'):
    pos_begin = html.find(key) + len(key) + num_chars
    pos_end = html.find(separator, pos_begin)
    return html[pos_begin: pos_end]

def ajax_request(session, url, params=None, data=None, headers=None, retries=5, sleep=20):
    for _ in range(retries):
        response = session.post(url, params=params, data=data, headers=headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code in [403, 413]:
            return {}
        else:
            time.sleep(sleep)

def download_comments(youtubeId, sleep=.1):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT

    response = session.get(YOUTUBE_VIDEO_URL.format(youtubeId=youtubeId))
    html = response.text
    session_token = find_value(html, 'XSRF_TOKEN', 3)
    session_token = session_token.encode('ascii').decode('unicode-escape')

    data = json.loads(find_value(html, 'var ytInitialData = ', 0, '};') + '}')
    for renderer in search_dict(data, 'itemSectionRenderer'):
        ncd = next(search_dict(renderer, 'nextContinuationData'), None)
        if ncd:
            break

    if not ncd:
        return

    continuations = [(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comments')]
    while continuations:
        continuation, itct, action = continuations.pop()
        response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL,
                                params={action: 1,
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

        if action == 'action_get_comments':
            section = next(search_dict(response, 'itemSectionContinuation'), {})
            for continuation in section.get('continuations', []):
                ncd = continuation['nextContinuationData']
                continuations.append((ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comments'))
            for item in section.get('contents', []):
                continuations.extend([(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comment_replies')
                                      for ncd in search_dict(item, 'nextContinuationData')])

        elif action == 'action_get_comment_replies':
            continuations.extend([(ncd['continuation'], ncd['clickTrackingParams'], 'action_get_comment_replies')
                                  for ncd in search_dict(response, 'nextContinuationData')])

        for comment in search_dict(response, 'commentRenderer'):
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
