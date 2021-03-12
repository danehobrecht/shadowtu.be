# ShadowTube

ShadowTube does not use Google dependencies of any kind. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. The Tor service must be running as a background process for this script to execute successfully, meaning users are required to have Tor Browser installed. For the time being, this program is strictly bash, but a website is undergoing development.

Analyzation features are as follows:

* Specific video links
* Complete comment history

### Bash
---

Install dependencies by running:

    pip3 install -r requirements.txt

Run (terminal):
    
    cd ~/shadowtube
    sudo chmod a+x main.py
    ./main.py

ShadowTube does not relay personal data, nor does it have the ability to. Individual verification is firmly encouraged.
