#!/bin/bash

echo -e "\033[92m please wait..."
sleep 1
pkg install nano -y
pkg install python -y

while ! python -c "import requests" &> /dev/null; do
    echo -e "\033[91m 'requests' module not found. Installing..."
    pip install requests
    sleep 1
done

echo -e "\033[92m Requests module is installed!"

echo -e "\033[92m entering the tools..."
sleep 2
python umbrella.py
