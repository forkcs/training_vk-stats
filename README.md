# vk-stats

**vk-stats** is a script for vk.com that display statistics of messages in the dialog.

## Installation
Download the project
``` 
git clone https://github.com/forkcs/vk-stats.git
cd vk-stats
```
Create virtual environment and install requirements
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
With activated virtual environment:
```
python main.py [-h] [--login LOGIN] [--pwd PWD] [--user-id USER_ID] [--json-filename JSON_FILENAME]

optional arguments:
  -h, --help            show this help message and exit
  --login LOGIN         Login or phone number.
  --pwd PWD             Password.
  --user-id USER_ID     Id of the user, to analyze conversation history to.
  --json-filename JSON_FILENAME
                        Filename to write json-formatted data in.
```

## Requirements
```
Python 3.6+

vk_api==11.8.0
progressbar==2.5
```