# -*- coding: utf-8 -*-
# Theme-Me/support/lib.py
# Credit By Zidan IDz
import os, sys, time, requests, getpass
from .echo import theme_me
from .echo import merah, putih, pxh, hijau, oren, netral, kuning, abu


now = "v0.3.5"
url = "https://api.github.com/repos/Zidan-ID17/Theme-Me/releases" 

def version(now):
    try:
      response = requests.get(url)
      response.raise_for_status()
      dat_up = response.json()
      new_ver = dat_up[0]["name"]
      if new_ver > now:
        print(f"{putih}[{oren}∆{putih}] new version is available, please update now {oren}!!")
        print(f"{putih}[{oren}∆{putih}] current version {now} , latest version {new_ver} \n")
        ask = input(f"{abu}do you want to read update help? (y/n) > ").lower()
        if ask == "y":
           os.system("nano update.txt")
        else:
           sys.exit()
      else:
        return
    except requests.exceptions.RequestException as re:
      print(f"{putih}[{merah}∆{putih}] cannot connect to internet {merah}!!")
      print(f"{putih}[{oren}∆{putih}] make sure your connect to the internet")

def message():
	time.sleep(0.3)
	print(f"\n{putih} please input the correct choice [{merah}!{putih}]")
	time.sleep(1.5)
   
def runntxt(x):
  for i in x + "\n":
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(0.1/100)

def entry():
    while True:
      time.sleep(1)
      os.system("clear")
      runntxt(theme_me)
      print(f"\n{pxh} for Tokens, you can check YouTube Zeyshyy {netral}")
      code = getpass.getpass(f"{putih}enter token {hijau}>{putih} ").lower()
      if code == "emotebangga":
          time.sleep(1)
          print(f"\n{putih} login successfully [{hijau}✓{putih}]")
          time.sleep(1)
          break
      else:
          time.sleep(1)
          print(f"\n{putih} login failed [{merah}X{putih}]")
          time.sleep(1)
          ask = input(f" \n{putih} want to try again ? {kuning}(Y/N) > ").lower()
          if ask == "n":
              time.sleep(1)
              print(f"\n{putih} bye bye 👋\n")
              time.sleep(1)
              sys.exit()
