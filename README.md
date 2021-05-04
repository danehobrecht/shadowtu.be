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
"Super clever, really like the use of chickens. The smaller scale interpretations seem to be popular as opposed to som..."
https://www.youtube.com/watch?v=Drx1DEXa0GM

Accessible in Germany (89.163.252.230)
Accessible in France (89.234.157.254)
Accessible in Austria (109.70.100.58)

[ ✓ ]

"This is good work. Feel your pain with the beatmap conversion."
https://www.youtube.com/watch?v=nWfF8wj19yk

Accessible in Switzerland (31.7.61.186)
Accessible in the United States (199.249.230.69)
Accessible in Denmark (185.38.175.71)

[ ✓ ]

"Doesn't look like failing to me. Glad you enjoyed the map."
https://www.youtube.com/watch?v=e_pyT5yFuYY

Accessible in the Netherlands (185.248.160.21)
Accessible in Czechia (45.153.160.133)
Accessible in Germany (185.220.102.249)

[ ✓ ]

"This video is seriously helping the beatmapping process for a personal Minecraft project of mine. Thank you."
https://www.youtube.com/watch?v=LDiylRToAGE

Non-accessible in Czechia (45.153.160.136)
Non-accessible in Austria (109.70.100.51)
Non-accessible in the United States (162.247.74.202)

[ ! ]

3/4 comments publicly accessible.
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
