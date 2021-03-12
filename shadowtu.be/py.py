#!/venv/bin/python3

from flask import Flask, request, flash, redirect, url_for, render_template
from markupsafe import Markup
from werkzeug.utils import secure_filename

import main
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/var/www/uploads'
ALLOWED_EXTENSIONS = {'html'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
	return render_template('html.html')

@app.route('/', methods=['POST'])
def video():
	urlInput = request.form['shareUrl']
	output = main.videoExecute(urlInput)
	return render_template('html.html', output=output)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
