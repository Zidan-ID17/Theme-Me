#!/bin/bash

echo -e "\033[92m please wait..."
sleep 1
pkg install nano
pkg install python
pip install requests
echo -e "\033[92m entering the tools..."
sleep 2
python umbrella.py
