#!/venv/bin/python3

from flask import Flask, send_file, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

import main
import os

app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z'

UPLOAD_FOLDER = os.getcwd() + '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def video():
	global output
	if request.method == 'POST':
		user_input = request.form['url']
		output = main.video(user_input)
		return redirect(url_for('results'))
	return render_template('video.html')

@app.route('/comments', methods = ['GET', 'POST'])
def comments():
	global output
	if request.method == 'POST':
		f = request.files['file']
		filename = 'Google_-_My_Activity.html'
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
		output = main.comments()
		return redirect(url_for('results'))
	return render_template('comments.html')

@app.route('/why')
def why():
	return render_template('why.html')

@app.route('/results', methods=['GET'])
def results():
	return render_template('results.html', output=output)

@app.route('/results/download', methods=['GET'])
def download():
	return send_file("results.txt", as_attachment=True)
