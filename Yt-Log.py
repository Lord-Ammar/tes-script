import os,sys,time,requests,json,random,string
from time import sleep
from bs4 import BeautifulSoup as bs
from colorama import init, Fore, Back
ip = requests.get('https://api.ipify.org').text
localtime = time.asctime(time.localtime(time.time()))

B = Fore.BLUE
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
print ("\t"+Fore.RED+"▄███████████▄  "  "\033[1;95m╦ ╦"+Fore.WHITE+"┌─┐┬ ┬""\033[1;95m╔╦╗"+Fore.WHITE+"┬ ┬┌┐ ┌─┐")
print ("\t"+Fore.RED+"█████"+Fore.WHITE+"░"+Fore.RED+"▀██████  "  "\033[1;95m╚╦╝"+Fore.WHITE+"│ ││ │""\033[1;95m ║"+Fore.WHITE+" │ │├┴┐├┤")
print ("\t"+Fore.RED+"█████"+Fore.WHITE+"░░░"+Fore.RED+"▀████  "  "\033[1;95m ╩"+Fore.WHITE+" └─┘└─┘""\033[1;95m ╩"+Fore.WHITE+" └─┘└─┘└─┘")
print ("\t"+Fore.RED+"█████"+Fore.WHITE+"░░░"+Fore.RED+"▄████  "  "\033[1;97m[\033[1;96m•\033[1;97m] Cretor: \033[1;92mAmmarBN")
print ("\t"+Fore.RED+"█████"+Fore.WHITE+"░"+Fore.RED+"▄██████  "  "\033[1;97m[\033[1;96m•\033[1;97m] Time: \033[1;92m"+localtime)
print ("\t"+Fore.RED+"█████████████  "  "\033[1;97m[\033[1;96m•\033[1;97m] Your IP: \033[1;92m"+ip)
print ("\t"+Fore.RED+"─▀▀▀▀▀▀▀▀▀▀▀─  ")
print("\t["+Back.WHITE+Fore.BLACK+"Copyright By ©AmmarBN ©2022 Sunday 20 Feb \033[00m"+Fore.RED+"]")
print("")
print("\033[1;97m[\033[1;96m•\033[1;97m] Example: \033[1;92mhttps://youtu.be/mrDhNbSVR40\n\033[1;97m[\033[1;96m•\033[1;97m] Convert: \033[1;92mmp4/mp3/combo")
