# ShadowTube

![alt text](https://github.com/danehobrecht/shadowtube/blob/main/static/images/shadowtube.png)

Analyzation features:

 - Video links
 - Complete comment history (alpha)

To be developed:
 - "Discussion", or, "Community" posts

### Sample Output

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
