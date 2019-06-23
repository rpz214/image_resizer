# image_resizer
CS-GY 9163 assignment.

# What it does
Resize an image into a square. 

# Requirements
* Python 3.7
* Pip 3

Windows or Linux. On windows, ensure `set-executionpolicy unrestricted` is run with admin privileges in powershell

# How to Install
Retrieve from git by gui or run the command below:
```
git clone https://github.com/rpz214/image_resizer.git
```
Run the following to install image resizer (relative to image_resizer directory):
```
pip install virtualenv
python -m virtualenv env
./env/scripts/activate
pip install image_resizer
```

# How to Run
```
usage: main.py [-h] src dst size

Resize source image to a square and write to destination

positional arguments:
  src         Path to source file
  dst         Path to destination directory
  size        Size of destination file

optional arguments:
  -h, --help  show this help message and exit
```