# ShadowTube

Current analyzation features are as follows:

- Video links
- Complete comment history
    
### Host ShadowTube instance
#### GNU/Linux, MacOS

1. Download the zip and create a virtual environment named "venv" in the extracted directory:

	`python3 -m venv /path/to/shadowtube/venv`

2. Navigate to directory:

	`cd /path/to/shadowtube`

3. Install dependencies:

    `pip3 install -r requirements.txt`

4. Establish the flask app:

    `export FLASK_APP=app.py`
    
5. Run:

    `flask run`

#### Windows

1. Download the zip and create a virtual environment (venv) in the extracted directory:

	`python3 -m venv c:path\to\shadowtube\venv`

2. Activate virtual environment:

	`venv\Scripts\activate.bat`

3. Install dependencies:

	`pip3 install -r requirements.txt`

4. Establish the flask app:

	`set FLASK_APP=app.py`

5. Run:

	`python3 -m flask run`
	
## Prerequisites

- Python 3 - pip3 must be available | https://www.python.org/downloads/
- Tor Browser - Required to be running during script execution | https://www.torproject.org/
- virtualenv - Required for creating sandboxed environments | https://pypi.org/project/virtualenv/
- Comment History HTML - "Google - My Activity.html" must be locally available to the script | https://www.youtube.com/feed/history/comment_history

## Known compatability issues (subject to change)

- Video premieres
- Geometric unicode characters in titles
- Discussion posts
