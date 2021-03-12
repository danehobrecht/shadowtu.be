#!/venv/bin/python3

from flask import Flask, request, render_template
from markupsafe import Markup

import main

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('html.html')

@app.route('/', methods=['POST'])
def runAndOutput():
	urlInput = request.form['shareUrl']
	output = main.videoExecute(urlInput)
	return render_template('html.html', output=output)
