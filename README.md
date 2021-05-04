# ShadowTube

![alt text](https://github.com/danehobrecht/shadowtu.be/blob/main/static/images/shadowtube.png)

Analyzation features:

 - Video links
 - Complete comment history (alpha)
 - "Discussion", or, "Community" posts (under development)

### Sample outputs
#### Video

```
"Me at the zoo"
https://www.youtube.com/watch?v=jNQXAC9IVRw

Accessible in the United States (199.249.230.78)
Accessible in Republic of Moldova (178.17.174.164)
Accessible in Ukraine (193.218.118.183)
Accessible in Seychelles (37.228.129.5)
Accessible in the United States (199.249.230.158)

5/5 attempts successful.
```

#### Comments

```
https://www.youtube.com/watch?v=Drx1DEXa0GM
"Super clever, really like the use of chickens. The smaller scale interpretations seem to be popular as opposed to som..."
Accessible in Germany (185.220.101.204)
Accessible in the Netherlands (104.248.88.112)
Accessible in the Netherlands (51.15.124.1)
[ ✓ ]

https://www.youtube.com/watch?v=nWfF8wj19yk
"This is good work. Feel your pain with the beatmap conversion."
Accessible in Norway (185.35.202.222)
Accessible in Switzerland (46.19.141.84)
Accessible in the United States (104.244.73.13)
[ ✓ ]

https://www.youtube.com/watch?v=e_pyT5yFuYY
"Doesn't look like failing to me. Glad you enjoyed the map."
Accessible in Finland (95.216.145.1)
Accessible in Germany (5.199.130.188)
Accessible in Canada (209.127.17.234)
[ ✓ ]

https://www.youtube.com/watch?v=LDiylRToAGE
"This video is seriously helping the beatmapping process for a personal Minecraft project of mine. Thank you."
Accessible in the Netherlands (185.191.124.150)
Accessible in Ukraine (95.214.235.160)
Accessible in Germany (185.220.101.5)
[ ✓ ]

4/4 comments accessible.
```

### Self-host
#### GNU/Linux, MacOS

1. Download the zip and create a virtual environment named "venv" in the extracted directory
```
python3 -m venv /path/to/shadowtube/venv
```
2. Navigate to directory
```
cd /path/to/shadowtube
```
3. Install dependencies
```
pip3 install -r requirements.txt
```
4. Establish "app.py"
```
export FLASK_APP=app.py
```
5. Run
```
flask run
```
#### Windows

1. Download the zip and create a virtual environment (venv) in the extracted directory
```
python3 -m venv c:path\to\shadowtube\venv
```
2. Activate virtual environment
```
venv\Scripts\activate.bat
```
3. Install dependencies
```
pip3 install -r requirements.txt
```
4. Establish "app.py"
```
set FLASK_APP=app.py
```
5. Run
```
python3 -m flask run
```
### Prerequisites

 - Python 3 | pip3 and latest python version
https://www.python.org/downloads/
 - Tor Browser | Required to be running during script execution
https://www.torproject.org/
 - virtualenv | Sandboxed environment creation
https://pypi.org/project/virtualenv/

### Known compatability issues (subject to change)

 - Video premieres
 - Geometric unicode characters in titles
 - Discussion posts
