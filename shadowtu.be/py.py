#!/venv/bin/python3

from flask import Flask, request, render_template
from markupsafe import Markup

import main

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('html.html')

@app.route('/', methods=['POST'])
def video():
	urlInput = request.form['shareUrl']
	output = main.videoExecute(urlInput)
	return render_template('html.html', output=output)

@app.route('/', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        f = request.files['Google - My Activity.html']
        f.save('~/Backup/Documents/Programming/shadowtube-flask/Google - My Activity.html')
