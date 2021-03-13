# ShadowTube

Analyzation features are as follows:

* Specific video links
* Complete comment history

#### Installation (GNU/Linux):

1. Download "shadowtube-bash" and open the folder in terminal:

    `cd /path/to/shadowtube-bash`

2. Install dependencies:

    `pip3 install -r requirements.txt`

3. Make the script an executable:

    `sudo chmod a+x main.py`

4. Run:

    `./main.py`

#### More information

- Tor Browser is required to be running during script execution (https://www.torproject.org/).
- "Google - My Activity.html" must be locally available to the script to use the comment feature. Export the HTML page from the following link: https://www.youtube.com/feed/history/comment_history
- Clearnet-accessible website is in the works.
