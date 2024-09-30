#!/bin/bash

cd "$(dirname "$0")" || exit

if [ -d "../Theme-Me" ]; then
    rm -rf ../Theme-Me
fi

git clone https://github.com/Zidan-ID17/Theme-Me ../Theme-Me || { echo "Failed to clone repository"; exit 1; }

cd ../Theme-Me || { echo "Failed to enter Theme-Me directory"; exit 1; }
