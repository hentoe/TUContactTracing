# README

This script fills in your data to TU Dresden's contact tracing website using python3 with selenium.

Tested on Ubuntu 20.10

## How to use:
- create environment variable "PATHTOPROGRAMFOLDER" which points to the directory, in which all the files are stored
- create a python virtual environment called "venv" inside of this directory and install requirements
- discard ".template" suffix from files in "personal_data" directory
- fill in your data in data.py
- add run.sh to autostart or create a cronjob or create a systemd daemon
