#!/bin/bash

if [ -d "../Theme-Me" ]; then
    rm -rf ../Theme-Me
fi
git clone https://github.com/Zidan-ID17/Theme-Me ../Theme-Me
cd ../Theme-Me || { echo "Failed to enter Theme-Me directory"; exit 1; }
