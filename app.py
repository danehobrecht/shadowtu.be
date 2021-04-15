#!/venv/bin/python3

from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import main
import os

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z'

@app.route('/', methods=['GET', 'POST'])
def video():
	global output
	if request.method == 'POST':
		user_input = request.form['shareUrl']
		output = main.videoExecute(user_input)
		return redirect(url_for('vOutput'))
	return render_template('video.html')

@app.route('/video/results', methods=['GET'])
def vOutput():
	return render_template('video-results.html', output=output)

@app.route('/comments', methods = ['GET', 'POST'])
def comments():
	if request.method == 'POST':
		f = request.files['file']
		filename = 'Google_-_My_Activity.html'
		f.save(secure_filename(f.filename))
		return render_template('comments.html', output=main.commentsExecute())
	return render_template('comments.html')

@app.route('/why')
def why():
	return render_template('why.html')
