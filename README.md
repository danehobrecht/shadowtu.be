# ShadowTube

Analyzation features are as follows:

- Video links
- Specific comments (or complete history)
    
### Flask installation
#### GNU/Linux, MacOS

1. Download the zip, extract the folder, and open in terminal

    `cd /path/to/shadowtube-flask`
    
2. Install dependencies:

    `pip3 install -r requirements.txt`

3. Establish the flask app:

    `export FLASK_APP=app.py`
    
4. Run:

    `flask run`

**Windows support coming soon.**

## Prerequisites

- Tor Browser | https://www.torproject.org/
    - Required to be running during script execution.
- Comment History HTML | https://www.youtube.com/feed/history/comment_history
    - "Google - My Activity.html" must be locally available to the script to use the comment feature.

## Sidenotes

- Video premieres currently not supported.
