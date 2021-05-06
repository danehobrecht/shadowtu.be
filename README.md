# ShadowTube

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
pip3 install -r requirements.txt
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

"This video is seriously helping the beatmapping process for a personal Minecraft project of mine. Thank you."
https://www.youtube.com/watch?v=LDiylRToAGE

Accessible in Sweden (213.164.206.124)
Accessible in Canada (51.161.43.237)
Accessible in the United States (107.189.10.63)

[ ✓ ]

No abnormal behavior detected. All comments are publicly available.
```

### Hypothetical results

#### Video

```
"Me at the zoo"
https://www.youtube.com/watch?v=jNQXAC9IVRw

Non-accessible in the United States (199.249.230.78)
Non-accessible in the Republic of Moldova (178.17.174.164)
Non-accessible in Ukraine (193.218.118.183)
Non-accessible in Seychelles (37.228.129.5)
Non-accessible in the United States (199.249.230.158)

Alarming behavior detected.
```

#### Comments

```
"This video is seriously helping the beatmapping process for a personal Minecraft project of mine. Thank you."
https://www.youtube.com/watch?v=LDiylRToAGE

Non-accessible in Sweden (213.164.206.124)
Accessible in Canada (51.161.43.237)
Non-accessible in the United States (107.189.10.63)

[ ! ]

Questionable behavior detected in 1 of 1 comment(s).
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
