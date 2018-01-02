#!/usr/bin/env python2
#coding: utf-8

from time import sleep
import urllib
import os

print("""\033[35m

 █    ██  ██▀███   ██▓          ██▓███ ▓██   ██▓
 ██  ▓██▒▓██ ▒ ██▒▓██▒         ▓██░  ██▒▒██  ██▒
▓██  ▒██░▓██ ░▄█ ▒▒██░         ▓██░ ██▓▒ ▒██ ██░
▓▓█  ░██░▒██▀▀█▄  ▒██░         ▒██▄█▓▒ ▒ ░ ▐██▓░
▒▒█████▓ ░██▓ ▒██▒░██████▒ ██▓ ▒██▒ ░  ░ ░ ██▒▓░
░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░░ ▒░▓  ░ ▒▓▒ ▒▓▒░ ░  ░  ██▒▒▒ 
░░▒░ ░ ░   ░▒ ░ ▒░░ ░ ▒  ░ ░▒  ░▒ ░     ▓██ ░▒░ 
 ░░░ ░ ░   ░░   ░   ░ ░    ░   ░░       ▒ ▒ ░░  
   ░        ░         ░  ░  ░           ░ ░     
                            ░           ░ ░\033[1;m

""")
sleep(3)


try:
    url = "https://sup3r-us3r.github.io/files/niveis/nivel2.txt"
    os.system("clear")
    while True and not url.startswith("https://"):
        os.system("clear")
    else:
        print("\033[31mAguarde\033[1;m\033[32m...\033[1;m")
        sleep(2)
        x = urllib.urlopen(url)
        print(x.read())
except KeyboardInterrupt:
    os.system("clear")
    print ("Control -C Pressionado fim do programa")

print("""
|----------------------------------------------------------------------------|

[\033[1;32m*\033[1;m] Acima está o código-fonte, apenas ache a senha.

""")