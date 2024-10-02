# -*- coding: utf-8 -*-
# Theme-Me/support/lib.py
# Credit By Zidan IDz
import os, sys, time, requests, getpass
from .echo import theme_me, note
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
            print(f"{putih}[{oren}∆{putih}] New version is available, please update now {oren}!!")
            print(f"{putih}[{oren}∆{putih}] Current version {now}, latest version {new_ver} \n")
            ask = input(f"{abu}Do you want to read update help? (y/n) > ").lower()
            if ask == "y":
                os.system("nano update.txt")
            else:
                sys.exit()
        else:
            return
    except requests.exceptions.RequestException:
        print(f"{putih}[{merah}∆{putih}] Cannot connect to the internet {merah}!!")
        print(f"{putih}[{oren}∆{putih}] Make sure you are connected to the internet")
        sys.exit()


def message():
    print(f"\n{putih}Please input the correct choice [{merah}!{putih}]")
    time.sleep(1.5)


def ext():
    time.sleep(1)
    print(f"\n{putih}Thank you for using Theme-Me")
    time.sleep(1)
    print(f"\n{putih}Bye bye {netral}👋\n")
    time.sleep(1)
    os.system("clear")
    os.system("login")
    sys.exit()


def runntxt(x):
    for i in x + "\n":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


def entry():
    while True:
        time.sleep(1)
        os.system("clear")
        runntxt(theme_me)
        print(f"\n{pxh}For Tokens, you can check YouTube Zeyshyy {netral}")
        code = getpass.getpass(f"{putih}Enter token {hijau}>{putih} ").lower()
        if code == "emotebangga":
            time.sleep(1)
            print(f"\n{putih}Login successfully [{hijau}✓{putih}]")
            time.sleep(1)
            break
        else:
            time.sleep(1)
            print(f"\n{putih}Login failed [{merah}X{putih}]")
            time.sleep(1)
            ask = input(f"\n{putih}Want to try again? {kuning}(Y/N) > ").lower()
            if ask == "n":
                ext()


def about():
    os.system("clear")
    print(note)
    os.system("pause")
