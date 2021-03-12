# ShadowTube

ShadowTube does not relay personal data of any kind, nor does it have the ability to. Any data given by the user through consent is ephemeral. Individual verification is firmly encouraged. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. The Tor service must be running as a background process for this script to execute successfully, meaning users are required to have Tor Browser installed. For the time being, this program is strictly bash, but a website is undergoing development.

Analyzation features are as follows:

* Specific video links
* Complete comment history

#### Installation (GNU/Linux)

- Download "shadowtube-bash" and open the folder in terminal:

    `cd /path/to/shadowtube-bash`

- Install dependencies:

    `pip3 install -r requirements.txt`

- Make the script an executable:

    `sudo chmod a+x main.py`

- Run:

    `./main.py`
    
#### More information    

Comment history must be locally available to the script to use the comment analyzation feature. This can be retrieved by logging in to the respective Google account and exporting the HTML data from https://www.youtube.com/feed/history/comment_history. In most cases, pressing "CTRL+S", or, "COMMAND+S" on the tab is the most straightforward way to do this. If this isn't the case, look into exporting HTML data from a particular webpage on the respective browser/operating system.
