#!/venv/bin/python3

from __future__ import print_function

from lxml.cssselect import CSSSelector
from stem.control import Controller
from requests import get
from array import array
from stem import Signal

import subprocess
import lxml.html
import argparse, requests
import socket, shutil
import socks
import time, json, html
import sys
import re, io, os

x = 1
cycles = 10
for x in range(cycles):
	print(cycles)
	x += 1
	cycles += 1
