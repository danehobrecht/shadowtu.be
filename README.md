![alt text](https://github.com/danehobrecht/shadowtu.be/blob/main/static/images/shadowtube.png)

Analyzation features:

 - Video links
 - Complete comment history (alpha)
 - "Discussion", or, "Community" posts (under development)

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
pip3 install -r requirements.txt --no-warn-script-location
```
4. Establish "app.py"
```
export FLASK_APP=app.py
```
5. Run
```
python3 -m flask run
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

### Sample results
#### Video

```
"Me at the zoo"
https://www.youtube.com/watch?v=jNQXAC9IVRw

Accessible in the United States (199.249.230.78)
Accessible in Republic of Moldova (178.17.174.164)
Accessible in Ukraine (193.218.118.183)
Accessible in Seychelles (37.228.129.5)
Accessible in the United States (199.249.230.158)

No abnormal behavior detected.
```

#### Comments

```
"Super clever, really like the use of chickens. The smaller scale interpretations seem to be popular as opposed to som..."
https://www.youtube.com/watch?v=Drx1DEXa0GM

Accessible in Germany (185.220.102.8)
Accessible in Seychelles (37.228.129.5)
Accessible in Germany (185.220.101.213)

[ ✓ ]

"This is good work. Feel your pain with the beatmap conversion."
https://www.youtube.com/watch?v=nWfF8wj19yk

Accessible in Germany (185.220.100.249)
Accessible from an unknown location.
Accessible in Austria (109.70.100.50)

[ ✓ ]

"Doesn't look like failing to me. Glad you enjoyed the map."
https://www.youtube.com/watch?v=e_pyT5yFuYY

Accessible in Switzerland (176.10.104.240)
Accessible in Germany (185.220.101.144)
Accessible in China (23.154.177.131)

[ ✓ ]

No abnormal behavior detected. All comments are publicly available.
```

### Prerequisites

 - Python 3.7.3+ & pip3
https://www.python.org/downloads/
 - Tor Browser
https://www.torproject.org/
 - virtualenv
https://pypi.org/project/virtualenv/

### Known compatability issues (subject to change)

 - Video premieres
 - Geometric unicode characters in titles
 - Discussion posts
