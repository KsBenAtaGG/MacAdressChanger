#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("apt-get install machanger")
os.system("clear")
os.system("figlet OTO MAC")
print("""
MAC Adresi Değiştirme Aracına Hoş Geldiniz. Lütfen bir değer giriniz.

1) MAC Adresini Rastgele Belirle
2) MAC Adresini Elle Belirle
3) MAC Adresini Orjinale Döndür

""")

islemno = raw_input("Sayı Değeri giriniz: ")

if(islemno == "1"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -r eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adresi Rastegele Belirlendi")

elif(islemno == "2"):
	macadres = raw_input("Yeni MAC adresinizi Giriniz: ")
	os.system("ifconfig eth0 down")
	os.system("macchanger --mac " + macadres + " eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mYeni MAC Adresiniz Elle Belirlendi.")

elif(islemno == "3"):
	os.system("ifconfig eth0 down")
	os.system("macchanger -p eth0")
	os.system("ifconfig eth0 up")
	print("\033[92mMAC Adresi Orjinale Döndürüldü")

else:
	print("Hatalı Sayı Değeri Girdiniz. Program Yeniden Başlatılıyor")
	os.system("python mac.py")
