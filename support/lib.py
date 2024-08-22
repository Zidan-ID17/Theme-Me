#!/usr/bin/env python3
#Theme-Me/support/lib.py
#Credit By Zidan IDz
import os, sys time, requests


gelap = ' \033[38;5;240m'
merah =  '\033[91m'
hijau = '\033[92m'
kuning = '\033[93m'
biru = '\033[94m'
ungu = '\033[95m'
abu = '\033[90m'
putih = '\033[97m'
oren = '\033[38;5;208m'
pxm = '\033[97;41m'
mxp = '\033[91;47m'
pxm = '\033[97;41m'
axh = '\033[30;100m'
pxh = '\033[30;47m'
netral = '\033[0m'
ver = "v1.0.1"
url = "https://api.github.com/repos/Zidan-ID17/Theme-Me/releases" 

def network(now):
    try:
      response = requests.get(url)
      response.raise_for_status()
      dat_up = response.json()
      new_ver = dat_up[0}["name"]
      if new_ver > now_ver:
        print(f"{putih}[{oren}∆{putih}] new version is available, please update now {oren}!!")
        print(f"{putih}[{oren}∆{putih}] current version {ver} , latest version {new_ver} ")
        sys.exit()
      else:
        return
    except requests.RequestsException as re:
      print(f"{putih}[{merah}∆{putih}] cannot connect to internet {merah}!!")
      print(f"{putih}[{oren}∆{putih}] make sure your connect to the internet")

def runntxt(x):
  for i in x + "\n":
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1/100)
    

