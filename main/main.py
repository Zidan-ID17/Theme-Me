# -*- coding: utf-8 -*-
#Theme-Me/main/main.py
import os, sys, time
from ..support.lib import runntxt, putih, hijau, merah, netral
from ..support.logo import theme-me, m_pg

def main():
	time.sleep(1)
	os.system("clear")
	runntxt(icon)
	print(main_mark)
	select = input(f"{putih}[select options]{hijau} > ").lower()
	if select == "theme":
		sheet1_theme()
	elif select == "font":
		sheet1_font()
	elif select == "background":
		sheet1_background()
	elif select == "restore":
		message()
	elif select == "about":
		about()
	elif select == "exit":
    ex()
	else:
		time.sleep(0.3)
		print(f"\n{putih} please input the correct choice [{merah}!{putih}]")
		time.sleep(1)
		main()

def ex():
  	time.sleep(1.)
		print(f"\n{white} thank you for using Theme-Me ")
		time.sleep(1)
		print(f"\n{white} bye bye {netral}👋\n")
		time.sleep(1)
		os.system("clear")
		os.system("login")

if __name__ == "__main__":
