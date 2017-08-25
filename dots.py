#!/usr/bin/env python
#coding: utf-8

#Autor: Magno Tutor / Sup3r-Us3r

'''
dots
'''

from time import *
from platform import python_version
import os
import sys

if sys.version_info[0] < 3:
        versao = python_version()
        print("\n\033[32m Você está usando o python na versão\033[1;m \033[1m\033[31m%s\033[1;m \033[32me ela é inferior ao python3 em diante.\033[1;m" %(versao))
        print("\033[32m Por favor rode o dots.py com a versão superior ao python2.\033[1;m\n")
        exit(1)

#if os.geteuid() != 0:
#        sys.stderr.write("\n\033[32mDesculpe, é necessária a permissão de\033[1;m \033[1m\033[31mroot\033[1;m\n\n")
#        sys.stderr.close()
#        sys.exit(1)

def Menu():
    os.system("clear")
    arq = open("/etc/hostname", "r")
    hostname = arq.read()
    print("""\033[32m
          ██████╗  ██████╗ ████████╗███████╗
          ██╔══██╗██╔═══██╗╚══██╔══╝██╔════╝
          ██║  ██║██║   ██║   ██║   ███████╗
          ██║  ██║██║   ██║   ██║   ╚════██║
          ██████╔╝╚██████╔╝   ██║   ███████║\033[1;m

          \033[1;91mBEM VINDO AO MEU SCRIPT:\033[1;m \033[33m%s\033[1;m


                    \033[1;91m[\033[1;m\033[1;32m1\033[1;m\033[1;91m]\033[1;m I3WM
                    \033[1;91m[\033[1;m\033[1;32m2\033[1;m\033[1;91m]\033[1;m TERMITE
                    \033[1;91m[\033[1;m\033[1;32m3\033[1;m\033[1;91m]\033[1;m COMPTON
                    \033[1;91m[\033[1;m\033[1;32m4\033[1;m\033[1;91m]\033[1;m NEOFETCH
                    \033[1;91m[\033[1;m\033[1;32m5\033[1;m\033[1;91m]\033[1;m MPD - NCMPCPP
                    \033[1;91m[\033[1;m\033[1;32m6\033[1;m\033[1;91m]\033[1;m VIS
                    \033[1;91m[\033[1;m\033[1;32m7\033[1;m\033[1;91m]\033[1;m CONKY
                    \033[1;91m[\033[1;m\033[1;32m8\033[1;m\033[1;91m]\033[1;m .XINITRC

                    \033[1;91m[\033[1;m\033[1;32mq\033[1;m\033[1;91m]\033[1;m SAIR
          """ %(hostname))

    opcao1 = input("\n\033[32m↳\033[1;m ")
    if opcao1 == "1":
        Bloco1()
    elif opcao1 == "2":
        Bloco2()
    elif opcao1 == "3":
        Bloco3()
    elif opcao1 == "4":
        Bloco4()
    elif opcao1 == "5":
        Bloco5()
    elif opcao1 == "6":
        Bloco6()
    elif opcao1 == "7":
        Bloco7()
    elif opcao1 == "8":
        Bloco8()
    elif opcao1 == "q":
        exit(1)
    else:
        Menu()

def Banner1():
    os.system("clear")
    print("""\033[32m
          ╦╔╗╔╔═╗╔╦╗╔═╗╦  ╔═╗╔╗╔╔╦╗╔═╗  ╔╦╗╔═╗╔═╗╔═╗╔╗╔╔╦╗╔═╗╔╗╔╔═╗╦╔═╗
          ║║║║╚═╗ ║ ╠═╣║  ╠═╣║║║ ║║║ ║   ║║║╣ ╠═╝║╣ ║║║ ║║║╣ ║║║║  ║╠═╣
          ╩╝╚╝╚═╝ ╩ ╩ ╩╩═╝╩ ╩╝╚╝═╩╝╚═╝  ═╩╝╚═╝╩  ╚═╝╝╚╝═╩╝╚═╝╝╚╝╚═╝╩╩ ╩\033[1;m

          """)


def Banner2():
    os.system("clear")
    print("""\033[32m
          ╔═╗╔═╗╦  ╦╔═╗╔═╗╔╗╔╔╦╗╔═╗  ╔═╗╔═╗╔╗╔╔═╗╦╔═╗
          ╠═╣╠═╝║  ║║  ╠═╣║║║ ║║║ ║  ║  ║ ║║║║╠╣ ║║ ╦
          ╩ ╩╩  ╩═╝╩╚═╝╩ ╩╝╚╝═╩╝╚═╝  ╚═╝╚═╝╝╚╝╚  ╩╚═╝\033[1;m

          """)

def Bloco1():
    Banner1()
    os.system("sudo pacman -S i3 lm_sensors mpc feh hddtemp nitrogen zsh git")
    os.system("yaourt -S i3blocks ttf-inconsolata ttf-font-awesome ttf-dejavu ttf-fantasque-sans dmenu2 lemonbar-git i3-gaps-git")
    os.system("clear")
    Banner2()
    os.system("cp -r Blocks/ $HOME/Blocks")
    os.system("cp -r .config/i3 $HOME/.config/i3")
    sleep(2)
    Menu()

def Bloco2():
    Banner1()
    os.system("sudo pacman -S termite git")
    os.system("git clone https://github.com/powerline/fonts.git && sleep 2 && sh fonts/install.sh")
    Banner2()
    os.system("cp -r .config/termite $HOME/.config/termite")
    sleep(2)
    Menu()

def Bloco3():
    Banner1()
    os.system("sudo pacman -S compton")
    Banner2()
    os.system("cp .config/compton.conf $HOME/.config")
    sleep(2)
    Menu()

def Bloco4():
    Banner1()
    os.system("sudo pacman -S w3m")
    os.system("yaourt -S neofetch")
    Banner2()
    os.system("cp -r .config/neofetch $HOME/.config/neofetch")
    sleep(2)
    Menu()

def Bloco5():
    Banner1()
    os.system("sudo pacman -S mpd ncmpcpp")
    Banner2()
    os.system("sudo systemctl stop mpd && sudo systemctl disable mpd")
    os.system("mkdir -p $HOME/.mpd/playlists")
    os.system("touch $HOME/.mpd/{mpd.db,mpd.log,mpd.pid,mpdstate}")
    os.system("cp .mpd/mpd.conf $HOME/.mpd/mpd")
    os.system("clear")
    print("""\033[32m
          ┌─┐┬ ┌┬┐┌─┐┬─┐┌─┐  ┌─┐  ┬ ┬┌─┐┬ ┬┌─┐┬─┐┬┌─┐
          ├─┤│  │ ├┤ ├┬┘├┤   │ │  │ │└─┐│ │├─┤├┬┘││ │
          ┴ ┴┴─┘┴ └─┘┴└─└─┘  └─┘  └─┘└─┘└─┘┴ ┴┴└─┴└─┘\033[1;m
                        \033[1;91m┌─┐┬ ┬┌─┐┌─┐┌┬┐
                        │ ┬├─┤│ │└─┐ │
                        └─┘┴ ┴└─┘└─┘ ┴\033[1;m
                \033[32m┌─┐┌─┐┬─┐┌─┐  ┌─┐  ┌─┐┌─┐┬ ┬
                ├─┘├─┤├┬┘├─┤  │ │  └─┐├┤ │ │
                ┴  ┴ ┴┴└─┴ ┴  └─┘  └─┘└─┘└─┘\033[1;m

          """)
    editor = input("\033[32mDIGITE O NOME DO EDITOR DE TEXTO DE SUA PREFERÊNCIA:\033[1;m\n\033[1;91m↳\033[1;m ")
    os.system(editor + " $HOME/.mpd/mpd.conf")
    os.system("cp -r .ncmpcpp $HOME/.ncmpcpp")
    sleep(2)
    Menu()


def Bloco6():
    Banner1()
    os.system("yaourt -S cli-visualizer")
    Banner2()
    os.system("cp -r .config/vis $HOME/.config/vis")
    sleep(2)
    Menu()

def Bloco7():
    Banner1()
    os.system("sudo pacman -S conky perl-image-exiftool")
    Banner2()
    os.system("cp -r .conky-mpd $HOME/.conky-mpd")
    os.system("cp .conkyrc $HOME/.conkyrc")
    sleep(2)
    Menu()

def Bloco8():
    Banner2()
    os.system("cp .xinitrc $HOME/.xinitrc")
    sleep(2)
    Menu()

Menu()
