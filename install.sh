#!/bin/bash

echo -e "\033[92m please wait..."
sleep 1
pkg install nano
pkg install python
pip install requests
python umbrella.py
