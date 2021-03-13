#!/venv/bin/python3

from flask import Flask, request, flash, redirect, url_for, render_template
from markupsafe import Markup
from werkzeug.utils import secure_filename

import main
import os

app = Flask(__name__)

UPLOAD_FOLDER = '~/shadowtube-flask'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
	return render_template('html.html')

@app.route('/', methods=['POST'])
def video():
	urlInput = request.form['shareUrl']
	vOutput = main.videoExecute(urlInput)
	return render_template('html.html', vOutput=vOutput)
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
	if request.method == 'POST':
		f = request.files['file']
		filename = "Google_-_My_Activity.html"
		f.save(secure_filename(f.filename))
	cOutput = main.commentsExecute()
	return render_template('html.html', cOutput=cOutput)
