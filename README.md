# ShadowTube

ShadowTube does not relay personal data of any kind, nor does it have the ability to. Individual verification is firmly encouraged. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. The Tor service must be running as a background process for this script to execute successfully, meaning users are required to have Tor Browser installed. For the time being, this program is strictly bash, but a website is undergoing development.

Analyzation features are as follows:

* Specific video links
* Complete comment history

## Bash

### Installation (GNU/Linux)

- Download the "shadowtube" folder and cd into it:

    cd /path/to/shadowtube

- Open the folder in terminal and install dependencies:

    pip3 install -r requirements.txt

- Make the main python script an executable:

    sudo chmod a+x main.py

- Run the script:

    ./main.py

###

ShadowTube does not or store logs or relay personal data, nor does it have the ability to. Analyzing comments for shadowbanning requires that the user upload the extracted HTML data from https://www.youtube.com/feed/history/comment_history. Storing/parsing is required for this service to be functional, but is ephermeral with the ambition to entirely respect user privacy. Individual verification is firmly encouraged.
