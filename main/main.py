# -*- coding: utf-8 -*-
#Theme-Me/main/main.py
# Credit by Zidan IDz
import os, sys, time
from ..support.lib import runntxt, putih, hijau, merah, netral
from ..support.logo import theme-me, m_pg

def main():
	time.sleep(1)
	os.system("clear")
	runntxt(theme-me)
	print(m_pg)
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

def th1_sh():
	time.sleep(1)
	os.system("clear")
	running(theme-me)
	print(th1_pg)
	select = input(f"{white}select options {hijau}>{putih} ")
	if select in ["1","01"]:
		#Run
	elif select in ["2","02"]:
		#Run
	elif select in ["3","03"]:
		#Run
	elif select in ["4","04"]:
		#Run
	elif select in ["5","05"]:
		#Run
	elif select in ["6","06"]:
		#Run
	elif select in ["7","07"]:
		f#Run
	elif select in ["8","08"]:
		#Run
	elif select in ["9","09"]:
		#Run
	elif select in ["10"]:
		#Run
	elif select in ["77"]:
		next
	elif select in ["88"]:
		previous
	elif select in ["0","00"]:
		ex()
	else:
		msg()
		th1_sh()
		
def ex():
  	time.sleep(1.)
	print(f"\n{white} thank you for using Theme-Me ")
	time.sleep(1)
	print(f"\n{white} bye bye {netral}👋\n")
	time.sleep(1)
	os.system("clear")
	os.system("login")

def msg():
	time.sleep(0.3)
	print(f"\n{putih} please input the correct choice [{merah}!{putih}]")
	time.sleep(1)
	
if __name__ == "__main__":
