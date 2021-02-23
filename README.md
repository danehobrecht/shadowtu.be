# ShadowTube
YouTube shadowban detection. This script does not utilize the YouTube API, or Google dependencies of any kind. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. As of now, the Tor service must be running as a background process for this script to execute successfully. 

Search analyzation features are as follows:

* Particular video links
* Complete comment history

---

Install dependencies by running:

    ``pip install -r requirements.txt`` 

Run (terminal)
    
    1. ``cd ~/shadowtube``
    2. ``sudo chmod a+x main.py``
    3. ``./main.py``

ShadowTube does not relay personal data, nor does it have the ability to. Individual verification is firmly encouraged.
