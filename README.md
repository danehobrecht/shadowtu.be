# ShadowTube

Website is in development. For now, this program is strictly bash.

Analyzation features are as follows:

Video links
    Specific comments (or complete history)

Installation
Bash
GNU/Linux, MacOS

    Download "shadowtube-bash" and open in terminal:

    cd /path/to/shadowtube-bash

    Install dependencies:

    pip3 install -r requirements.txt

    Make the script an executable:

    sudo chmod a+x main.py

    Run:

    ./main.py

Flask
GNU/Linux, MacOS

    Download "shadowtube-flask.zip" and extract the folder, and open in terminal

    cd /path/to/shadowtube-flask

    Install dependencies:

    pip3 install -r requirements.txt

    Establish the flask app:

    export FLASK_APP=app.py

    Run:

    flask run

Windows support coming soon.
Bash prerequisites

    Tor Browser | https://www.torproject.org/
        Required to be running during script execution.
    Comment History HTML | https://www.youtube.com/feed/history/comment_history
        "Google - My Activity.html" must be locally available to the script to use the comment feature.
