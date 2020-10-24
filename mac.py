#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install machanger")
os.system("clear")
os.system("figlet AUTO MAC")
print("""
Welcome to the mac address change tool. Please enter a value.

1) Randomize MAC Address
2) Set MAC Address Manually
3) Return MAC Address to Original

""")

islemno = raw_input("Enter Number Value: ")

if(islemno == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Address Is Randomly Determined.")

elif(islemno == "2"):
	macadres = raw_input("Enter your new MAC address: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYour new MAC Address was Set Manually.")

elif(islemno == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Address Reverted to Original")

else:
	print("You entered an incorrect number value. Program Restarting ... ")
	os.system("python mac.py")
