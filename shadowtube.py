#!/venv/bin/python3

from flask import Flask, request, flash, redirect, url_for, render_template
from markupsafe import Markup
from werkzeug.utils import secure_filename

import main
import os

app = Flask(__name__)

# Home (videos)
@app.route('/', methods=['GET', 'POST'])
def videos():
	if request.method == 'POST':
		user_input = request.form['shareUrl']
		vOutput = main.videoExecute(user_input)
		return render_template('home.html', vOutput=vOutput)
	return render_template('home.html')

# Comments
@app.route('/comments', methods = ['GET', 'POST'])
def comments():
	if request.method == 'POST':
		f = request.files['file']
		filename = "Google_-_My_Activity.html"
		f.save(secure_filename(f.filename))
		cOutput = main.commentsExecute()
		return render_template('comments.html', cOutput=cOutput)
	return render_template('comments.html')

# Why
@app.route('/why')
def why():
	return render_template('why.html')
