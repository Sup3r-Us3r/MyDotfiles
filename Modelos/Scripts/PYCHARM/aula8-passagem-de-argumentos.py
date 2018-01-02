#!/usr/bin/env python3.6
#coding: utf-8

#A biblioteca sys nos permite utilizar algumas coisas do sistema operacional
#Argumento 0 sempre vai nos mostrar o caminho completo do arquivo

import sys

def help():
    print("""

    PROGRAMA DE SOMA & SUBTRAÇÃO

Use para SOMA: ./programa.py soma n1 n2
Use para SUB:  ./programa.py sub n1 n2

""")

argumentos = sys.argv #arg1 metodo // arg2 - n1 // arg3 - n2

def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2


if argumentos[1] == "help":
    ajuda = help()

elif argumentos[1] == "soma":
    resp = soma(float(argumentos[2]), float(argumentos[3]))
    print(resp)

elif argumentos[1] == "sub":
     resp = sub(float(argumentos[2]), float(argumentos[3]))
     print(resp)






