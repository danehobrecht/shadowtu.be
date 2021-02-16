# ShadowTube
YouTube shadowban detection. This script does not utilize the YouTube API, or Google dependencies of any kind. In theory, it should not be able to be blacklisted, as scraping is done with constantly rotating IPs. As of now, the Tor service must be running as a background process for this script to execute successfully. 

Featured searches are as follows:

* Particular video links
* Complete comment history

---

Install dependencies by running:

    pip install -r requirements.txt

ShadowTube does not process, read, or store the contents of comments inputted and script verification is encouraged.
