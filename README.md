# ShadowTube

ShadowTube does not relay personal data of any kind, nor does it have the ability to. Individual verification is firmly encouraged. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. The Tor service must be running as a background process for this script to execute successfully, meaning users are required to have Tor Browser installed. For the time being, this program is strictly bash, but a website is undergoing development.

Analyzation features are as follows:

* Specific video links
* Complete comment history

### Installation (GNU/Linux)

- Download "shadowtube-bash" and open the folder in terminal:

    `cd /path/to/shadowtube`

- Install dependencies:

    `pip3 install -r requirements.txt`

- Make the main python script an executable:

    `sudo chmod a+x main.py`

- Run the script:

    `./main.py`
    
Comment history must be locally available as "Google - My Activity.html". This can be retrieved by logging in to the respective Google account and exporting this page: 
https://www.youtube.com/feed/history/comment_history. 
In most cases, pressing "CTRL+S", or, "COMMAND+S" on the page is the most straightforward way to do this. If this isn't the case, look into exporting HTML data from webpage on the respective browser/operating system.

###

ShadowTube does not or store logs or relay personal data, nor does it have the ability to. Analyzing comments for shadowbanning requires that the user upload the extracted HTML data from their Google account comment history. Storing/parsing is required for this service to be functional, but is ephermeral with the ambition to entirely respect user privacy. Individual verification is firmly encouraged.
