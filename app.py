#!/venv/bin/python3

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from markupsafe import Markup

import main
import os

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z'

@app.route('/', methods=['GET', 'POST'])
def videos():
	if request.method == 'POST':
		user_input = request.form['shareUrl']
		return render_template('videos.html', output=main.videoExecute(user_input))
	return render_template('videos.html')

@app.route('/comments', methods = ['GET', 'POST'])
def comments():
	if request.method == 'POST':
		f = request.files['file']
		filename = "Google_-_My_Activity.html"
		f.save(secure_filename(f.filename))
		return render_template('comments.html', output=main.commentsExecute())
	return render_template('comments.html')

@app.route('/why')
def why():
	return render_template('why.html')
